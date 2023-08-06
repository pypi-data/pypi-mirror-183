import copy
import dataclasses
import logging
import math
import re
import typing
from pathlib import Path

import PySide6
import cv2
import numpy as np

from PySide6 import QtGui, QtCore
from PySide6.QtCore import Qt, Signal, QPoint, QObject, QRect
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox, QPushButton, QComboBox, QDoubleSpinBox, QDialog, \
    QDialogButtonBox, QVBoxLayout, QStyleOptionViewItem, QGroupBox

from maphis import qimage2ndarray
from maphis.common.blocking_operation import BlockingOperation
from maphis.common.image_operation_binding import ImageOperation
from maphis.common.photo import Photo, UpdateContext, UpdateEvent, PhotoUpdate, PhotoUpdateType
from maphis.common.photo_layer import PhotoLayer
from maphis.common.state import State
from maphis.common.storage import Storage, StorageUpdate
from maphis.common.units import SIPrefix, Unit, BaseUnit, Value, UnitStore
from maphis.common.utils import ScaleSetting, ScaleLineInfo, get_scale_marker_roi, get_reference_length, \
    get_scale_line_ends
from maphis.common.visualization_layer import VisualizationLayer
from maphis.image_viewer import ImageViewer
from maphis.thumbnail_storage import ThumbnailDelegate, ThumbnailStorage_
from maphis.tools.ruler import Tool_Ruler


@dataclasses.dataclass
class ScaleExtractionResult:
    photo_idx: int
    image_scale: Value
    reference_length: Value
    px_length: Value
    scale_line_p1: typing.Tuple[int, int]
    scale_line_p2: typing.Tuple[int, int]
    scale_marker: typing.Optional[np.ndarray]
    scale_marker_bbox: typing.Optional[typing.Tuple[int, int, int, int]]


@dataclasses.dataclass
class ScaleSettingTuple:
    old_scale_set: ScaleSetting
    new_scale_set: ScaleSetting


class ScaleSettingWidget(QWidget):
    scale_set = Signal(list)
    accepted = Signal(list)
    cancelled = Signal()

    def __init__(self, state: State, parent: typing.Optional[PySide6.QtWidgets.QWidget] = None,
                 f: PySide6.QtCore.Qt.WindowFlags = Qt.WindowFlags()):
        super().__init__(parent, f)

        self.state = state
        self._state = self.state
        self.photo: typing.Optional[Photo] = None
        self._storage: typing.Optional[Storage] = None

        self.units = UnitStore()
        self.line_length: typing.Optional[Value] = None

        # self.setLayout(self._layout)
        # self.line_length: Value = Value(0, self.state.units.units['px'])
        # self.ref_length: Value = Value(0, self._cmbUnits.itemData(self._cmbUnits.currentIndex()))
        # self.scale: Value = Value(0, self.state.units.units['px'] / self.ref_length.unit)

        self._setup_controls()
        self._setup_viewer()

        self.image_op: ImageOperation = ImageOperation(self)

        self.scale_settings: typing.Dict[Path, ScaleSettingTuple] = {}
        self.setWindowTitle('Set scale')
        self.setWindowModality(Qt.ApplicationModal)

    def _setup_controls(self):
        self._layout = QHBoxLayout()

        self._ref_label = QLabel("Reference length: ")

        self._spboxReference_mm = QSpinBox()
        # self._spboxReference_mm.setSuffix(' mm')
        self._spboxReference_mm.setMinimum(1)
        self._spboxReference_mm.setMaximum(9999)
        self._spboxReference_mm.setMaximumWidth(150)
        self._spboxReference_mm.setAlignment(Qt.AlignLeft)
        self._spboxReference_mm.valueChanged.connect(self._new_reference_length)

        self._cmbUnits = QComboBox()
        self._cmbResUnits = QComboBox()
        default_idx = 0
        for i, prefix in enumerate(list(SIPrefix)):
            unit = Unit(BaseUnit.m, prefix=prefix, dim=1)
            self._cmbUnits.addItem(str(unit), unit)
            self._cmbResUnits.addItem(str(unit), unit)
            if prefix == SIPrefix.m:
                default_idx = i
        self._cmbUnits.setCurrentIndex(default_idx)
        self._cmbUnits.currentIndexChanged.connect(self._handle_reference_unit_changed)

        self._lblPixels = QLabel('Line length: 0 px')
        self._lblResolution = QLabel('Scale:')

        self._lblScaleValue = QLabel()

        self._groupAutoScaleExtraction = QGroupBox("Automatic scale extraction from markers")
        self._groupAutoScaleExtraction.setLayout(QHBoxLayout())

        self._btnExtractScalesAllPhotos = QPushButton(text="Apply to all photos")
        self._btnExtractScalesAllPhotos.clicked.connect(self._extract_scale_for_all)

        self._btnExtractScalesCurrentPhoto = QPushButton(text="Apply to this photo")
        self._btnExtractScalesCurrentPhoto.clicked.connect(self._extract_scale_for_current)

        self._groupAutoScaleExtraction.layout().addWidget(self._btnExtractScalesCurrentPhoto)
        self._groupAutoScaleExtraction.layout().addWidget(self._btnExtractScalesAllPhotos)

        self._btnSetManually = QPushButton(text="Enter scale numerically")
        self._btnSetManually.clicked.connect(self._get_scale_from_user)

        self._btnAcceptAll = QPushButton(text="Accept changes for all photos")
        self._btnAcceptAll.clicked.connect(self._accept_changes_all)
        self._btnAcceptAll.setEnabled(True)

        self._btnAcceptCurrent = QPushButton(text="Accept changes for this photo")
        self._btnAcceptCurrent.clicked.connect(self._accept_changes_current)
        self._btnAcceptCurrent.setEnabled(True)

        self._btnResolutionGlobal = QPushButton()
        self._btnResolutionGlobal.setText("Assign scale value to all photos")
        self._btnResolutionGlobal.clicked.connect(self._set_global_resolution)
        self._btnResolutionGlobal.setEnabled(True)

        self._btnCancel = QPushButton(text="Cancel")
        self._btnCancel.clicked.connect(self.cancelled.emit)
        self._btnCancel.setEnabled(True)

        self._groupScaleInfo = QGroupBox("Scale info")
        self._groupScaleInfo.setLayout(QHBoxLayout())

        self._groupScaleInfo.layout().setSpacing(2)
        self._groupScaleInfo.layout().addWidget(self._ref_label)
        self._groupScaleInfo.layout().addWidget(self._spboxReference_mm)
        self._groupScaleInfo.layout().addWidget(self._cmbUnits)
        _lay: QHBoxLayout = self._groupScaleInfo.layout()
        _lay.addSpacing(20)
        self._groupScaleInfo.layout().addWidget(self._lblPixels)
        _lay.addSpacing(20)
        self._groupScaleInfo.layout().addWidget(self._lblResolution)
        self._groupScaleInfo.layout().addWidget(self._lblScaleValue)
        self._groupScaleInfo.layout().addWidget(self._btnSetManually)
        self._groupScaleInfo.layout().addWidget(self._btnResolutionGlobal)

        self._layout.setSpacing(5)
        self._layout.addWidget(self._groupScaleInfo)
        self._layout.addWidget(self._groupAutoScaleExtraction)
        self._layout.addStretch()
        self._layout.addWidget(self._btnAcceptCurrent)
        self._layout.addWidget(self._btnAcceptAll)
        # self._layout.addWidget(self._btnResolutionGlobal)
        self._layout.addWidget(self._btnCancel)

    def _setup_viewer(self):
        self.image_viewer = ImageViewer(self.state)

        self.image_viewer.first_photo_requested.connect(self._fetch_first_photo)
        self.image_viewer.prev_photo_requested.connect(self._fetch_prev_photo)
        self.image_viewer.next_photo_requested.connect(self._fetch_next_photo)
        self.image_viewer.last_photo_requested.connect(self._fetch_last_photo)
        self.image_viewer.ui.tbtnRotateCW.hide()
        self.image_viewer.ui.tbtnRotateCCW.hide()

        #self.image_viewer.rotate_cw_requested.connect(self._rotate_cw)
        #self.image_viewer.rotate_ccw_requested.connect(self._rotate_ccw)

        self.image_viewer.rotate_cw_requested.connect(lambda: self.image_op.rotate(clockwise=True))
        self.image_viewer.rotate_ccw_requested.connect(lambda: self.image_op.rotate(clockwise=False))

        self.image_viewer.photo_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.image_viewer.photo_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.image_viewer.photo_switched.connect(self.set_photo)

        self.image_viewer.add_layer(PhotoLayer(self.state))
        self.viz_layer = VisualizationLayer()
        self.viz_layer.initialize()
        self.viz_layer.setOpacity(.90)

        self.image_viewer.add_layer(self.viz_layer)

        self.image_viewer.hide()

        # self.ruler_tool: typing.Optional[Tool_Ruler] = None  # Tool_Ruler(self._state)
        self.ruler_tool: Tool_Ruler = Tool_Ruler(self._state)
        self.ruler_tool.show_real_units(False)
        self.ruler_tool.current_value.connect(self.compute_resolution)

        self.ruler_tools: typing.List[Tool_Ruler] = []

        self.image_viewer.set_tool(self.ruler_tool)
        self.image_viewer.ui.controlBar.addItem(self._layout)
        self.setLayout(self.image_viewer.layout())

    def _fetch_photo(self, idx):
        idx = min(max(idx, 0), self._storage.image_count - 1)
        # TODO: Is there any difference between self.temp_storage and self._state.storage?
        # _fetch_photo() now serves as a single image fetching function, but some
        # of the functions it replaced seemed to use self.temp_storage, and some
        # seemed to use self._state.storage in some places.
        # if self.temp_storage == self._state.storage:
        #     print('self.temp_storage == self._state.storage')
        # else:
        #     print('!!! self.temp_storage != self._state.storage')
        # self.image_viewer.enable_navigation_buttons(idx) # TODO: or should this work with temp_storage? (in that case, pass the appropriate storage as a parameter of enable_navigation_buttons()?)
        photo = self._storage.get_photo_by_idx(idx)

        scale_set = self.scale_settings[photo.image_path]

        self.setWindowTitle(f'{photo.image_name} - Set scale')

        # self.image_viewer.setWindowTitle(f"Please delineate scale line for {photo.image_name}")
        self.image_viewer.set_photo(photo, reset_view=True, reset_tool=False)

        # self.ruler_tool = self.ruler_tools[idx]
        # value_mm: Optional[int] = None
        # dig_re = re.compile(r'([0-9]+)\s*([a-zA-Z]m)')
        # if self.ruler_tool._measurement <= 0:
        #     scale_marker, (left, top, width, height) = get_scale_marker_roi(photo.image)
        #     p1x, p1y, p2x, p2y = get_scale_line_ends(scale_marker)
        #     scale_text, scale_roi = get_reference_length(scale_marker)
        #     print(scale_text)
        #     if len(scale_text) > 0:
        #         match = dig_re.match(scale_text)
        #         for group in match.groups():
        #             print(group)
        #         print(scale_text)
        #     self.ruler_tool.set_line(QPoint(p1x+left, p1y+top), QPoint(p2x+left, p2y+top), reset_others=True)

        # self.set_photo(photo)


        # res = self.temp_storage.image_scales[idx]
        # res = self.temp_storage.get_photo_by_idx(idx).image_scale
        # if res is not None and res.value > 0:
        #     self._lblResolution.setText(f'Scale: {res}')
        # else:
        #     self._lblResolution.setText('Scale: n/a')
        #
        # if self.ruler_tool.value_storage is not None and len(self.ruler_tool.value_storage) > 0:
        #     self._lblPixels.setText(f'Line length: {self.ruler_tool.value_storage[0]} px')
        # else:
        #     self._lblPixels.setText('Line length: 0 px')

        # self._scale_set_widget.set_photo(photo)

        # if self.ruler_tool.value_storage is not None and len(self.ruler_tool.value_storage) > 0:
        #     # self._scale_set_widget.set_line_length(Value(self.ruler_tool.value_storage[0], self._state.units.units['px']))
        #     self.set_line_length(self.ruler_tool.value_storage[0])
        # else:
        #     self.set_line_length(Value(0, self._state.units.units['px']))

    def _fetch_first_photo(self):
        self._fetch_photo(0)

    def _fetch_prev_photo(self):
        self._fetch_photo(self._state.storage.image_names.index(self._state.current_photo.image_name) - 1) # TODO: or should this work with temp_storage?

    def _fetch_next_photo(self):
        self._fetch_photo(self._state.storage.image_names.index(self._state.current_photo.image_name) + 1) # TODO: or should this work with temp_storage?

    def _fetch_last_photo(self):
        self._fetch_photo(self._state.storage.image_count - 1) # TODO: or should this work with temp_storage?

    def _new_reference_length(self, value: int):
        self.compute_resolution(self.scale_settings[self.photo.image_path].new_scale_set.scale_line.length)

    def _set_global_resolution(self):
        idx = self.state.storage.image_names.index(self.state.current_photo.image_name)
        photo_ = self.state.storage.get_photo_by_idx(idx, load_image=False)

        # for i in range(self.state.storage.image_count):
        #     photo = self.state.storage.get_photo_by_idx(i, load_image=False)
        #     photo.image_scale = photo_.image_scale

        scale_setting = self.scale_settings[photo_.image_path].new_scale_set

        for img_path, scale_tup in self.scale_settings.items():
            if img_path == photo_.image_path:
                continue
            scale_tup.new_scale_set.scale = scale_setting.scale
            scale_tup.new_scale_set.scale_line = None #ScaleLineInfo((0, 0), (0, 0), Value(0, self.ruler_tool._px_unit))
            scale_tup.new_scale_set.reference_length = None

        # self.scale_set.emit([i for i in range(self.state.storage.image_count)])
        self.accepted.emit()

    def _accept_changes_current(self):
        self.accepted.emit([self.state.current_photo])

    def _accept_changes_all(self):
        self.accepted.emit(self.state.storage.images)

    def compute_resolution(self, pixels: typing.Optional[Value]):
        if pixels is None:
            self.unset_line()
            return
        self.line_length = pixels
        self._lblPixels.setText(f'Line length: {pixels}')

        if pixels.value > 0:
            self._cmbUnits.setEnabled(True)
            self._spboxReference_mm.setEnabled(True)
        else:
            self.unset_line()
            return

        idx = self.state.storage.image_names.index(self.state.current_photo.image_name)
        photo = self.state.storage.get_photo_by_idx(idx, load_image=False)
        ref_length = Value(self._spboxReference_mm.value(), self._cmbUnits.itemData(self._cmbUnits.currentIndex()))
        res = pixels / ref_length
        # if photo.image_scale is None:
        #     unit = self.state.units.units['px'] / self._cmbUnits.itemData(self._cmbUnits.currentIndex())
        #     photo.image_scale = Value(value=res, unit=unit)
        self.scale = res
        scale_setting = self.scale_settings[photo.image_path]
        scale_setting.new_scale_set.scale = res
        if pixels.value == 0:
            scale_setting.new_scale_set.scale = None
        if scale_setting.new_scale_set.scale_line is None:
            if len(self.ruler_tool.endpoints) >= 2:
                scale_setting.new_scale_set.scale_line = ScaleLineInfo(
                    p1=self.ruler_tool.endpoints[0].toTuple(),
                    p2=self.ruler_tool.endpoints[1].toTuple(),
                    length=pixels
                )
            else:
                scale_setting.new_scale_set.scale_line = ScaleLineInfo(
                    p1=(0, 0),
                    p2=(0, 0),
                    length=Value(0, self.ruler_tool._px_unit)
                )
        scale_setting.new_scale_set.scale_line.length = pixels
        scale_setting.new_scale_set.reference_length = ref_length
        self.ruler_tool.set_scale(res)

        if len(self.ruler_tool.endpoints) > 1:
            scale_setting.new_scale_set.scale_line.p1 = self.ruler_tool.endpoints[0].toTuple()
            scale_setting.new_scale_set.scale_line.p2 = self.ruler_tool.endpoints[1].toTuple()

        # photo.image_scale = res
        # photo.image_scale.unit = self.state.units.units['px'] / self._cmbUnits.itemData(self._cmbUnits.currentIndex())
        # self._lblResolution.setText(f'Scale: {scale_setting.new_scale_set.scale}')
        # self._lblScaleValue.setText(str(scale_setting.new_scale_set.scale))
        self._set_lbl_scale_value_text(str(scale_setting.new_scale_set.scale))
        # self._lblScaleValue.setSuffix(f' {res.unit}')
        self._btnAcceptAll.setEnabled(True)
        self._btnResolutionGlobal.setEnabled(True)
        self.set_line(scale_setting.new_scale_set.scale_line, scale_setting.new_scale_set.reference_length)
        # self.scale_set.emit([idx])

    def set_photo(self, photo: Photo):
        self.photo = photo

        self.image_op.init(photo)
        self._state.current_photo = photo

        res = photo.scale_setting.scale
        scale_setting = self.scale_settings[photo.image_path].new_scale_set
        self.ruler_tool.set_scale(scale_setting.scale)
        scale_line = scale_setting.scale_line
        if scale_line is not None:
            # self.ruler_tool.set_line(QPoint(*scale_line.p1),
            #                          QPoint(*scale_line.p2),
            #                          reset_others=True)
            # self.set_line_length(scale_line.length)
            # self._spboxReference_mm.setEnabled(True)
            # self._cmbUnits.setEnabled(True)
            # if (ref_length := scale_setting.reference_length) is not None:
            #     self._spboxReference_mm.setValue(ref_length.value)
            #     self._cmbUnits.setCurrentIndex(list(SIPrefix).index(ref_length.unit.prefix))
            self.set_line(scale_line, scale_setting.reference_length)
        else:
            self.unset_line()
            # self.ruler_tool.reset_tool()
            # self._lblPixels.setText('Line length: no line drawn')
            # # if there is not scale line yet, disable referene length spinner and units combobox
            # # self.set_line_length(Value(0, self.state.units.units['px']))
            # self._spboxReference_mm.setEnabled(False)
            # self._cmbUnits.setEnabled(False)
        if res is not None and res.value > 0:
            # self._lblResolution.setText(f'Scale: {scale_setting.scale}')
            # self._lblScaleValue.setText(str(scale_setting.scale))
            self._set_lbl_scale_value_text(str(scale_setting.scale))
            # self._lblScaleValue.setSuffix(f' {scale_setting.scale.unit}')
            # idx = list(SIPrefix).index(scale_setting.reference_length.unit.prefix)
            # self._cmbUnits.setCurrentIndex(idx)
            # ref_length = scale_setting.reference_length
            # self._spboxReference_mm.setValue(ref_length.value)
        else:
            self._set_lbl_scale_value_text('not set')
            # self._lblResolution.setText('Scale')
            # self._lblScaleValue.setText('not set')
        self.setWindowTitle(f'{photo.image_name} - Set scale')
        self.image_viewer.set_tool(self.ruler_tool, reset_current=False)
        self.viz_layer.paint_commands = self.ruler_tool.viz_commands
        self.viz_layer.update()

    def set_line_length(self, length: Value):
        self.line_length = length
        if length.value > 0:
            self._cmbUnits.setEnabled(True)
            self._spboxReference_mm.setEnabled(True)
        self._lblPixels.setText(f'Line length: {self.line_length}')
        if self.photo.scale_setting.reference_length is not None:
            self._spboxReference_mm.setValue(self.photo.scale_setting.reference_length.value)
        else:
            if length.value > 0 and self.photo.image_scale is not None and self.photo.image_scale.value > 0:
                self._spboxReference_mm.setValue(round(length.value / self.photo.image_scale.value))
        self.compute_resolution(self.line_length)

    def _handle_reference_unit_changed(self, idx: int):
        # self._lblScaleValue.setSuffix(f' px / {self._cmbUnits.itemData(idx)}')
        self.compute_resolution(self.line_length)
        # self._lblScaleValue.setText(str(self.scale_settings[self.photo.image_path].new_scale_set.scale))
        self._set_lbl_scale_value_text(str(self.scale_settings[self.photo.image_path].new_scale_set.scale))

    def initialize(self, storage: Storage):
        logging.info(f'Scale setting: initializing storage {storage.location}')
        self.image_viewer.set_storage(storage)
        if self._storage is not None:
            self._storage.update_photo.disconnect(self._handle_update_photo)
        self._storage = storage
        self._storage.update_photo.connect(self._handle_update_photo)
        self._storage.storage_update.connect(self._handle_storage_update)
        self.scale_settings.clear()
        self.ruler_tool.reset_tool()
        for idx in range(self._storage.image_count):
            photo = self._storage.get_photo_by_idx(idx, load_image=False)
            self.scale_settings[photo.image_path] = ScaleSettingTuple(
                old_scale_set=photo.scale_setting,
                new_scale_set=copy.deepcopy(photo.scale_setting)
            )

    # def _handle_update_photo(self, img_name: str, ctx: UpdateContext, data):
    def _handle_update_photo(self, update: UpdateEvent):
        if self.photo is None or update.photo.image_name != self.photo.image_name:
            return
        # photo = self._storage.get_photo_by_name(img_name)
        scale_setting = self.scale_settings[update.photo.image_path].new_scale_set
        self.ruler_tool.set_scale(scale_setting.scale)
        scale_line = scale_setting.scale_line
        if (ref_length := scale_setting.reference_length) is not None:
            self._spboxReference_mm.setValue(ref_length.value)
            self._cmbUnits.setCurrentIndex(list(SIPrefix).index(ref_length.unit.prefix))
        event_obj: PhotoUpdate = update.update_obj
        if scale_line is not None: #and 'operation' in data:
            # if data['operation'].startswith('rot'):
            if event_obj.update_type in {PhotoUpdateType.Rotate90CCW, PhotoUpdateType.Rotate90CW}:
                scale_line.rotate(event_obj.update_type == PhotoUpdateType.Rotate90CCW,
                                  (round(0.5 * update.photo.image_size[1]),
                                    round(0.5 * update.photo.image_size[0])))
            # elif data['operation'] == Photo:
            #     f = data['factor']
            #     # scale_line.p1 = (round(f * scale_line.p1[0]),
            #     #                  round(f * scale_line.p1[1]))
            #     # scale_line.p2 = (round(f * scale_line.p2[0]),
            #     #                  round(f * scale_line.p2[1]))
            #     # scale_line.scale(f, (round(0.5 * photo.image_size[0]),
            #     #                      round(0.5 * photo.image_size[1])))
            #     pass
            # self.ruler_tool.set_line(QPoint(*scale_line.p1),
            #                          QPoint(*scale_line.p2),
            #                          reset_others=True)
            # self.set_line_length(scale_line.length)
            self.set_line(scale_line, scale_setting.reference_length)
        else:
            # self.set_line_length(Value(0, self.state.units.units['px']))
            self.unset_line()
        self.viz_layer.paint_commands = self.ruler_tool.viz_commands
        self.viz_layer.update()

    def _handle_storage_update(self, update: StorageUpdate):
        for photo_name in update.photos_included:
            photo = self._storage.get_photo_by_name(photo_name, load_image=False)
            self.scale_settings[photo.image_path] = ScaleSettingTuple(
                old_scale_set=photo.scale_setting,
                new_scale_set=copy.deepcopy(photo.scale_setting)
            )

    def _set_unit_to_cmbUnits(self, unit: Unit):
        self._cmbUnits.setCurrentIndex(list(SIPrefix).index(unit.prefix))

    def set_line(self, scale_line: ScaleLineInfo, ref_length: Value):
        scale_setting = self.scale_settings[self.photo.image_path].new_scale_set
        self._spboxReference_mm.setEnabled(True)
        self._spboxReference_mm.blockSignals(True)
        self._spboxReference_mm.setValue(ref_length.value)
        self._spboxReference_mm.blockSignals(False)
        self._cmbUnits.setEnabled(True)
        self._set_unit_to_cmbUnits(ref_length.unit)
        self.ruler_tool.set_line(QPoint(*scale_line.p1), QPoint(*scale_line.p2), reset_others=True)
        # self.set_line_length(scale_line.length)
        # self._lblScaleValue.setValue((scale_line.length / ref_length).value)
        # self._lblScaleValue.setText(str(scale_line.length / ref_length))
        self._set_lbl_scale_value_text(str(scale_line.length / ref_length))
        self._lblPixels.setText(f'Line length: {scale_line.length}')
        self.viz_layer.paint_commands = self.ruler_tool.viz_commands
        self.viz_layer.update()

    def unset_line(self):
        self._spboxReference_mm.setEnabled(False)
        self._cmbUnits.setEnabled(False)
        self._lblPixels.setText('Line length: no line drawn')
        # self._lblScaleValue.setText('not set')
        self._set_lbl_scale_value_text('not set')
        self.ruler_tool.reset_tool()

    def _get_scale_from_user(self):
        dialog = QDialog()
        dialog.setWindowTitle("Enter scale numerically")
        spbox = QDoubleSpinBox()
        spbox.setRange(0, 999)
        spbox.setSpecialValueText('0 (invalid value)')
        if self.scale_settings[self.photo.image_path].new_scale_set.scale is not None:
            spbox.setValue(self.scale_settings[self.photo.image_path].new_scale_set.scale.value)

        cmbUnits = QComboBox()
        scale_setting = self.scale_settings[self.photo.image_path].new_scale_set
        default_idx = 0
        for i, prefix in enumerate(list(SIPrefix)):
            unit = self.units.units['px'] / Unit(BaseUnit.m, prefix=prefix, dim=1)
            cmbUnits.addItem(str(unit), unit)
            if scale_setting.scale is not None and scale_setting.scale.unit == unit:
                default_idx = i

        cmbUnits.setCurrentIndex(default_idx)

        diag_buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        diag_buttons.accepted.connect(dialog.accept)
        diag_buttons.rejected.connect(dialog.reject)

        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Scale: '))
        hbox.addWidget(spbox)
        hbox.addWidget(cmbUnits)

        vbox.addLayout(hbox)
        vbox.addWidget(diag_buttons)

        dialog.setLayout(vbox)

        if dialog.exec_() == QDialog.Accepted:
            scale_setting.scale = Value(spbox.value(), cmbUnits.currentData())
            scale_setting.scale_line = None
            scale_setting.reference_length = None
            self.unset_line()
            # self._lblScaleValue.setText(str(scale_setting.scale))
            self._set_lbl_scale_value_text(str(scale_setting.scale))

    def _extract_scale_for_current(self):
        idxs = [self.state.storage.image_names.index(self.state.current_photo.image_name)]
        block_op = BlockingOperation(self.state.storage, idxs,
                                     operation=self._scale_extraction_operation,
                                     result_handler=self._scale_extraction_result_processing,
                                     parent=self)
        block_op.start()

    def _extract_scale_for_all(self):
        block_op = BlockingOperation(self.state.storage, list(range(self.state.storage.image_count)),
                                     operation=self._scale_extraction_operation,
                                     result_handler=self._scale_extraction_result_processing,
                                     parent=self)
        block_op.start()

    def _scale_extraction_operation(self, storage: Storage, idx: int) -> typing.Optional[ScaleExtractionResult]:
        dig_re = re.compile(r'([0-9]+)\s*([a-zA-Z]m)')
        unit_store = UnitStore()

        img_path = storage.image_paths[idx]
        image = cv2.imread(str(img_path))
        scale_marker, (left, top, width, height) = get_scale_marker_roi(image)
        ref_length, scale_rotated = get_reference_length(scale_marker)
        p1x, p1y, p2x, p2y = get_scale_line_ends(scale_marker)
        if p1x < 0:
            return None
        if len(ref_length) > 0:
            match = dig_re.match(ref_length)
            length = int(match.groups()[0])
            unit_str = match.groups()[1]
            unit = unit_store.units[unit_str]
            ref_length = Value(length, unit)
            px_length = Value(round(math.sqrt(((p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y)))),
                              unit_store.units['px'])
            image_scale = px_length / ref_length
        else:
            ref_length = None
            image_scale = None
            px_length = None
        p1x_, p1y_, p2x_, p2y_ = get_scale_line_ends(scale_rotated)
        scale_rotated = cv2.cvtColor(scale_rotated, cv2.COLOR_GRAY2RGB)
        scale_rotated = cv2.line(scale_rotated, (p1x_, p1y_ - 10), (p1x_, p1y_ + 10), [0, 255, 0], thickness=2)
        scale_rotated = cv2.line(scale_rotated, (p2x_, p1y_ - 10), (p2x_, p1y_ + 10), [0, 255, 0], thickness=2)
        scale_rotated = cv2.resize(scale_rotated, (154, 26), interpolation=cv2.INTER_LINEAR)
        # pixmap = QPixmap.fromImage(qimage2ndarray.array2qimage(scale_rotated))
        scale_marker = scale_rotated

        return ScaleExtractionResult(idx, image_scale, ref_length, px_length,
                                     (p1x+left, p1y+top),
                                     (p2x+left, p2y+top),
                                     scale_marker,
                                     (left, top, width, height))

    def _scale_extraction_result_processing(self, storage: Storage, idx: int, result: typing.Optional[ScaleExtractionResult]):
        if result is None or result.reference_length is None:
            return
        path = storage.image_paths[idx]
        sc_info = self.scale_settings[path].new_scale_set
        sc_info.scale = result.image_scale
        if sc_info.scale_line is None:
            sc_info.scale_line = ScaleLineInfo(p1=(-1, -1), p2=(-1, -1), length=Value(0, self.units.units['px']))
        sc_info.reference_length = result.reference_length
        sc_info.scale_line.p1 = result.scale_line_p1
        sc_info.scale_line.p2 = result.scale_line_p2
        sc_info.scale_line.length.value = np.sqrt(np.sum(np.square(np.array(sc_info.scale_line.p1) - np.array(sc_info.scale_line.p2))))
        sc_info.scale_marker_bbox = result.scale_marker_bbox
        sc_info.scale_marker_img = QPixmap.fromImage(qimage2ndarray.array2qimage(result.scale_marker))

        if path == self.state.current_photo.image_path:
            self.set_line(sc_info.scale_line, sc_info.reference_length)
        self._btnAcceptAll.setEnabled(True)

    def closeEvent(self, event:PySide6.QtGui.QCloseEvent):
        super().closeEvent(event)
        self.cancelled.emit()

    def _set_lbl_scale_value_text(self, text: str):
        # self._lblScaleValue.setText(f"<a href='scale_value'>{text}</a>")
        self._lblScaleValue.setText(text)

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        self.image_viewer.show_whole_image()


class ScaleItemDelegate(ThumbnailDelegate):
    def __init__(self, thumbnails: ThumbnailStorage_, scale_set_widget: ScaleSettingWidget,
                 parent: QObject = None):
        super().__init__(thumbnails, parent)
        self.scale_set_widget = scale_set_widget

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        super().paint(painter, option, index)
        path = index.data(Qt.UserRole + 8)
        scale_marker: typing.Optional[QPixmap] = self.scale_set_widget.scale_settings[path].new_scale_set.scale_marker_img  # TODO replace 7 with a named constant
        thumbnail: QImage = index.data(Qt.UserRole + 3)
        rect: QRect = option.rect
        if scale_marker is None:
            return
        scale_rect = QRect(rect.center().x() - 0.5 * scale_marker.width(), rect.bottom() - 32 - scale_marker.height(),
                           scale_marker.width(), scale_marker.height())
        painter.save()
        painter.setRenderHint(painter.SmoothPixmapTransform, True)
        # painter.drawImage(scale_rect, scale_marker)
        painter.drawPixmap(scale_rect, scale_marker)
        painter.restore()
