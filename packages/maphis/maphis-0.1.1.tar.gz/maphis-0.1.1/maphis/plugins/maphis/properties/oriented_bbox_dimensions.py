import copy
import typing
from typing import Optional

import cv2
import numpy as np
from PySide6.QtWidgets import QWidget

from maphis.common.common import Info
from maphis.common.label_image import RegionProperty, PropertyType
from maphis.common.photo import Photo
from maphis.common.plugin import PropertyComputation
from maphis.common.regions_cache import RegionsCache
from maphis.common.units import Value
from maphis.common.user_params import UserParam, ParamType
from common.param_widget import ParamWidget
from common.user_param import ParamBuilder, Param


class OBBoxDims(PropertyComputation):
    """
    GROUP: Length & area measurements
    NAME: Oriented bounding box dimensions
    DESCRIPTION: Width and heigth of the oriented bounding box of a region
    KEY: oriented_bbox
    """

    def __init__(self, info: Optional[Info] = None):
        super().__init__(info)
        # self._user_params = {
        #     'width': UserParam(name='Width', param_type=ParamType.BOOL, default_value=True, key='width'),
        #     'length': UserParam(name='Length', param_type=ParamType.BOOL, default_value=True, key='length')
        # }
        self._user_params: typing.Dict[str, Param] = {
            'width': ParamBuilder().bool_param().true().name('Width').key('width').build(),
            'length': ParamBuilder().bool_param().true().name('Length').key('length').build()
        }

        self._setting_widget: ParamWidget = ParamWidget(list(self._user_params.values()))

    def __call__(self, photo: Photo, region_labels: typing.List[int], regions_cache: RegionsCache, prop_names: typing.List[str]) -> \
            typing.List[RegionProperty]:
        props: typing.List[RegionProperty] = []

        # if regions_cache.data_storage.setdefault('key', -1) == ord('q'):
        #     return []

        for label in region_labels:
            if label not in regions_cache.regions:
                continue
            # bin_img = lab_img.mask_for(label)
            # if not np.any(bin_img):
            #     continue

            reg_obj = regions_cache.regions[label]

            mask = (255 * reg_obj.mask.copy()).astype(np.uint8)
            mask = cv2.copyMakeBorder(mask, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=0)

            points = np.argwhere(mask != 0)[:, ::-1]
            rot_rect = cv2.minAreaRect(points)

            # vis = cv2.cvtColor((mask).astype(np.uint8), cv2.COLOR_GRAY2BGR)

            rect_points = np.round(cv2.boxPoints(rot_rect)).astype(np.int32)

            # clrs = [
            #     [255, 0, 0],
            #     [0, 255, 0],
            #     [0, 0, 255],
            #     [0, 255, 255]
            # ]

            # centroid = np.round(np.mean(rect_points, axis=0)).astype(np.int32)

            # for i in range(4):
            #     vis = cv2.line(vis, tuple(rect_points[i - 1]), tuple(rect_points[i]), [0, 255, 0], 2)
            #     vec = rect_points[i - 1] - rect_points[i]
            #     vec = vec / (np.linalg.norm(vec) + 1e-9)
            #     # vis = cv2.line(vis, tuple(centroid), tuple(np.round((centroid + 50 * vec)).astype(np.int32)), clrs[i])
            #     # vis = cv2.circle(vis, tuple(rect_points[i]), 10, clrs[i])
            # for i in range(4):
            #     vis = cv2.circle(vis, tuple(rect_points[i]), 10, clrs[i], thickness=-1)
            ax1 = rect_points[0] - rect_points[-1]
            ax1_n = np.linalg.norm(ax1)
            ax1 = ax1 / (np.linalg.norm(ax1) + 1e-9)
            ax2 = rect_points[-1] - rect_points[2]
            ax2_n = np.linalg.norm(ax2)
            ax2 = ax2 / (np.linalg.norm(ax2) + 1e-9)

            # if np.abs(np.dot(ax1, np.array([1.0, 0]))) > np.abs(np.dot(ax2, np.array([1.0, 0]))):
            #     vis = cv2.line(vis, tuple(centroid), tuple(np.round(centroid + 0.5 * ax1_n * ax1).astype(np.int32)), [255, 255, 0])
            #     vis = cv2.line(vis, tuple(centroid), tuple(np.round(centroid - 0.5 * ax1_n * ax1).astype(np.int32)), [255, 255, 0])
            # else:
            #     vis = cv2.line(vis, tuple(centroid), tuple(np.round(centroid + 0.5 * ax2_n * ax2).astype(np.int32)), [255, 255, 0])
            #     vis = cv2.line(vis, tuple(centroid), tuple(np.round(centroid - 0.5 * ax2_n * ax2).astype(np.int32)), [255, 255, 0])
            #
            # #
            # # vis = cv2.line(vis, tuple(centroid), tuple(np.round((centroid + 10 * ax1)).astype(np.uint8)), [255, 0, 0])
            # # vis = cv2.line(vis, tuple(centroid), tuple(np.round((centroid + 10 * ax2)).astype(np.uint8)), [0, 0, 255])
            # vis = cv2.circle(vis, tuple(centroid), 5, [255, 128, 0])
            #
            # cv2.imshow('vis', vis)
            # key = cv2.waitKey(0)
            # cv2.destroyAllWindows()
            #
            # regions_cache.data_storage['key'] = key

            dims = {
                'width': 0.0,
                'length': 0.0
            }
            if np.abs(np.dot(ax1, np.array([1.0, 0]))) > np.abs(np.dot(ax2, np.array([1.0, 0]))):
                dims['width'] = ax1_n
                dims['length'] = ax2_n
                # width = ax1_n
                # length = ax2_n
            else:
                dims['width'] = ax2_n
                dims['length'] = ax1_n
                # width = ax2_n
                # height = ax1_n
            for prop_name in prop_names:
                prop = self.example(prop_name)
                prop.prop_type = PropertyType.Scalar
                prop.label = label
                if photo.image_scale is not None:
                    prop.value = Value(float(dims[prop_name]), self._px_unit) / photo.image_scale
                else:
                    prop.value = Value(float(dims[prop_name]), self._px_unit)
                prop.num_vals = 1
                # prop.val_names = ['']
                props.append(prop)
            # if self._user_params['width'].value:
            #     prop = self.example('width')
            #     # prop.info = copy.deepcopy(self.info)
            #     prop.prop_type = PropertyType.Scalar
            #     prop.label = label
            #     if photo.image_scale is not None:
            #         prop.value = Value(float(width), self._px_unit) / photo.image_scale
            #     else:
            #         prop.value = Value(float(width), self._px_unit)
            #     prop.num_vals = 1
            #     prop.val_names = ['Width']
            #     props.append(prop)
        return props

    @property
    def user_params(self) -> typing.List[UserParam]:
        return super().user_params

    @property
    def region_restricted(self) -> bool:
        return super().region_restricted

    @property
    def computes(self) -> typing.Dict[str, Info]:
        return {self.info.key: self.info}

    def example(self, prop_name: str) -> RegionProperty:
        prop = super().example(prop_name)
        prop.label = 0
        prop.info = copy.deepcopy(self.info)
        prop.info.name = prop_name
        prop.value = None
        prop.num_vals = 1
        prop.prop_type = PropertyType.Scalar
        prop.val_names = [prop_name.capitalize()]
        return prop

    def target_worksheet(self, prop_name: str) -> str:
        return super().target_worksheet(self.info.key)

    @property
    def group(self) -> str:
        return super().group

    @property
    def requested_props(self) -> typing.List[str]:
        return [par.key for par in self._user_params.values() if par.value]

    @property
    def setting_widget(self) -> typing.Optional[QWidget]:
        return self._setting_widget.widget
