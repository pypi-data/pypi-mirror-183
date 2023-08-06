import os
import platform
import subprocess
import typing
from pathlib import Path

import numpy as np
from PySide6.QtWidgets import QMessageBox

from maphis.common.label_hierarchy import LabelHierarchy
from maphis.common.label_image import PropertyType, RegionProperty
from maphis.common.plugin import ActionContext
from maphis.common.storage import Storage
from maphis.common.units import Unit, CompoundUnit, Value, convert_value


def _ndarray_export_routine(prop_list: typing.List[typing.Tuple[int, str, str, str]], append_row, context: ActionContext):
    row = []
    prop_list = list(sorted(prop_list, key=lambda tup: tup[0]))
    for i in range(context.storage.image_count):
        photo = context.storage.get_photo_by_idx(i, load_image=False)
        # lab_img = photo['Labels']
        lab_img = photo[context.current_label_name]
        row = [photo.image_name]
        for label, prop_comp_key, local_key, prop_name in prop_list:
            prop_key = f'{prop_comp_key}.{local_key}'
            if lab_img.get_region_props(label) is None:
                continue
            reg_props = lab_img.get_region_props(label)

            if prop_key not in reg_props:
                continue
            prop = reg_props[prop_key]
            region_name = lab_img.label_hierarchy.nodes[label].name

            for j in range(prop.num_vals):
                if j == 0:
                    row.append(f'{region_name}:{prop.info.name} {prop.val_names[j]}')
                else:
                    row = ['', f'{region_name}:{prop.info.name} {prop.val_names[j]}']
                for col in prop.col_names:
                    row.append(col)
                append_row(row)
                matrix2d: np.ndarray = prop.value[0][j]
                for r in range(matrix2d.shape[0]):
                    row = ['', prop.row_names[r]]
                    for c in range(matrix2d.shape[1]):
                        row.append(f'{matrix2d[r, c]:.3f}')
                    append_row(row)
                row = ['']
                append_row(row)
            append_row([''])


def _filter_by_NDArray(prop_tuple_list: typing.List[typing.Tuple[int, str, str, str]], context: ActionContext) -> \
        typing.Tuple[typing.List[typing.Tuple[int, str, str, str]], typing.List[typing.Tuple[int, str, str, str]]]:
    ndarray_props: typing.List[typing.Tuple[int, str, str, str]] = []
    other_props: typing.List[typing.Tuple[int, str, str, str]] = []

    for label, prop_comp_key, local_key, prop_name in prop_tuple_list:
        # dot_split = prop_key.split('.')
        prop_key = f'{prop_comp_key}.{local_key}'
        # comp_key = '.'.join(dot_split[:-1])
        # computation = self.computation_widget.computations_model.computations_dict[comp_key]
        if prop_comp_key not in context.property_computations: #self.computation_widget.computations_model.computations_dict:
            continue
        # computation = self.computation_widget.computations_model.computations_dict[prop_key]
        computation = context.property_computations[prop_comp_key]
        if computation.example(local_key).prop_type == PropertyType.NDArray:
            ndarray_props.append((label, prop_comp_key, local_key, prop_name))
        else:
            other_props.append((label, prop_comp_key, local_key, prop_name))
    return ndarray_props, other_props


def get_prop_tuple_list(context: ActionContext) -> typing.List[typing.Tuple[int, str, str, str]]:
    Label = int
    PropCompKey = str
    PropName = str
    PropKey = str

    prop_tuple_set: typing.Set[typing.Tuple[Label, PropCompKey, PropKey, PropName]] = set()
    for i in range(context.storage.image_count):
        photo = context.storage.get_photo_by_idx(i, load_image=False)
        for prop in photo[context.current_label_name].prop_list:
            #prop_tuple = (prop.info.key, prop.label, prop.info.name)
            prop_tuple = (prop.label, prop.prop_comp_key, prop.local_key, prop.info.name)
            prop_tuple_set.add(prop_tuple)
    return list(sorted(prop_tuple_set, key=lambda tup: tup[:3]))


def _group_measurements_by_sheet(prop_tup_list: typing.List[typing.Tuple[int, str, str, str]], context: ActionContext) \
        -> typing.Dict[str, typing.List[typing.Tuple[int, str, str, str]]]:
    sheet_grouped_props: typing.Dict[str, typing.List[typing.Tuple[int, str, str, str]]] = {}

    for label, prop_comp_key, local_key, prop_name in prop_tup_list:
        # dot_split = prop_key.split('.')
        # comp_key = '.'.join(dot_split[:-1])
        # computation = self.computation_widget.computations_model.computations_dict[prop_key]
        # prop_key = f'{prop_comp_key}.{local_key}'
        computation = context.property_computations[prop_comp_key]
        # prop_key_local = dot_split[-1]
        sheet_grouped_props.setdefault(computation.target_worksheet(local_key), []).append((label,
                                                                                                 prop_comp_key,
                                                                                                 local_key,
                                                                                                 prop_name))

    return sheet_grouped_props


def _tabular_export_routine(prop_tuple_list: typing.List[typing.Tuple[int, str, str, str]],
                            append_row: typing.Callable[[typing.List[typing.Any]], None], context: ActionContext):
    example_props: typing.Dict[str, RegionProperty] = {}
    column_names = ['photo_name']
    lab_hier: LabelHierarchy = context.storage.get_label_hierarchy(context.current_label_name)
    for label, prop_comp_key, local_key, prop_name in prop_tuple_list:
        prop_key = f'{prop_comp_key}.{local_key}'
        # dot_split = prop_key.split('.')
        # comp_key = '.'.join(dot_split[:-1])
        # computation = self.computation_widget.computations_model.computations_dict[prop_key]
        computation = context.property_computations[prop_comp_key]
        prop = computation.example(local_key)
        example_props[prop_key] = prop
        # if prop.prop_type == PropertyType.Vector or prop.num_vals > 1:
        if prop.num_vals > 1:
            if len(prop.val_names) != prop.num_vals:
                col_names = [str(i) for i in range(prop.num_vals)]
            else:
                col_names = prop.val_names
            for i in range(prop.num_vals):
                #column_names.append(f'{prop.info.key}_{prop.val_names[i]}:{self.state.colormap.label_names[label]}')
                # column_names.append(f'{prop.info.key}_{prop.val_names[i]}:{self.state.label_hierarchy.nodes[label].name}')
                column_names.append(f'{lab_hier.nodes[label].name}:{prop.info.name}_{col_names[i]}')
        else:
            #column_names.append(f'{prop.info.key}:{self.state.colormap.label_names[label]}')
            # column_names.append(f'{prop.info.key}:{self.state.label_hierarchy.nodes[label].name}')
            column_names.append(f'{lab_hier.nodes[label].name}:{prop.info.name}')
    append_row(column_names)
    for i in range(context.storage.image_count):
        photo = context.storage.get_photo_by_idx(i, load_image=False)
        row = [photo.image_name]
        # label_img = photo['Labels']
        label_img = photo[context.current_label_name]
        for label, prop_comp_key, local_key, prop_name in prop_tuple_list:
            prop_key = f'{prop_comp_key}.{local_key}'
            if label_img.get_region_props(
                    label) is None:  # So this LabelImg does not have props for `label`, insert a sequence of 'missing value' symbols (-1)
                ex_prop = example_props[prop_key]
                for _ in range(ex_prop.num_vals):
                    row.append('N/A')
            else:
                reg_props = label_img.get_region_props(label)
                if prop_key not in reg_props:  # This label region does not have property with `prop_key`, insert a sequence of `missing value` symbols (-1)
                    ex_prop = example_props[prop_key]
                    for _ in range(ex_prop.num_vals):
                        row.append('N/A')
                else:  # Finally, insert actual values for present property
                    reg_prop: RegionProperty = reg_props[prop_key]
                    if reg_prop.num_vals > 1:
                        unit_: typing.Union[Unit, CompoundUnit] = reg_prop.value[1]
                        targ_unit = context.units.get_default_unit(unit_)
                        # mult = (10 ** (int(reg_prop.value[1].prefix) - int(targ_unit.prefix))) ** reg_prop.value[1].dim
                        val_ = Value(reg_prop.value[0][0], unit_)
                        for val in reg_prop.value[0]:
                            val_.value = val
                            n_val = convert_value(val_, targ_unit)
                            row.append(n_val.value)
                            # break  # TODO how to handle exporting vector of values to CSV?
                    else:
                        targ_unit = context.units.get_default_unit(reg_prop.value.unit)
                        conv_val = convert_value(reg_prop.value, targ_unit)
                        row.append(conv_val.value)
        append_row(row)


def open_project_folder_in_explorer(context: ActionContext):
    if context.storage is None:  # Shouldn't even be necessary, as the QAction shouldn't be enabled in that case
        return
    if platform.system() == "Windows":
        os.startfile(context.storage.location)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", str(context.storage.location)])
    else:
        subprocess.Popen(["xdg-open", str(context.storage.location)])


def show_export_success_message(folder: Path, filenames: typing.List[str], context: ActionContext):
    filenames_in_rows = '\n'.join(filenames)
    if QMessageBox.information(None, 'Export finished',
                               f'The results were saved in the folder {folder} as files:\n{filenames_in_rows}\nDo you want to open the folder?',
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
        open_project_folder_in_explorer(context)
