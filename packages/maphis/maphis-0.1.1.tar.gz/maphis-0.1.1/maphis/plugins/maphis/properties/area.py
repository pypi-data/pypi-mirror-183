import copy
import typing
from typing import List, Optional

import numpy as np
import skimage
from common.user_param import Param, IntParamBuilder, ParamBuilder, StringParamBuilder, BoolParamBuilder
from skimage import io

from maphis.common.common import Info
from maphis.common.label_image import RegionProperty, PropertyType
from maphis.common.photo import Photo
from maphis.common.plugin import PropertyComputation
from maphis.common.regions_cache import RegionsCache, Region
from maphis.common.units import Value
from maphis.common.user_params import UserParam


class Area(PropertyComputation):
    """
    GROUP: Length & area measurements
    NAME: Area
    DESCRIPTION: Area of the region (px or mm\u00b2)
    KEY: area
    """
    def __init__(self, info: Optional[Info] = None):
        super().__init__(info)

    def _setup_params(self):
        self.__user_params: typing.List[Param] = [
            ParamBuilder().int_param().min_value(0).max_value(40).default_value(42).name('Magic number').key('magic_number').build(),
            ParamBuilder().string_param().name('Magic word').key('magic_word').default_value('please').build(),
            ParamBuilder().name('Yes/No').key('magic_bool').bool_param().true().build()
        ]

    def __call__(self, photo: Photo, region_labels: typing.List[int], regions_cache: RegionsCache, prop_names: typing.List[str]) -> \
    typing.List[RegionProperty]:

        props: typing.List[RegionProperty] = []

        for region_label in region_labels:
            if region_label not in regions_cache.regions:
                continue
            region: Region = regions_cache.regions[region_label]

            prop = self.example('area')
            prop.label = region.label
            prop.info = copy.deepcopy(self.info)
            # prop.value = int(np.count_nonzero(lab_img == label))
            value = Value(int(np.count_nonzero(region.mask)), self._px_unit * self._px_unit)
            if photo.image_scale is not None and photo.image_scale.value > 0:
                prop.value = value / (photo.image_scale * photo.image_scale)
                # prop.unit = 'mm\u00b2'  # TODO sync unit with the units in Photo
            else:
                prop.value = value
            prop.prop_type = PropertyType.Scalar
            prop.val_names = ['Area']
            prop.num_vals = 1
            props.append(prop)
        return props

    @property
    def user_params(self) -> List[UserParam]:
        return super().user_params

    @property
    def region_restricted(self) -> bool:
        return super().region_restricted

    @property
    def computes(self) -> typing.Dict[str, Info]:
        return {'area': self.info}

    def example(self, prop_name: str) -> RegionProperty:
        prop = RegionProperty()
        prop.label = 0
        prop.info = copy.deepcopy(self.info)
        # prop.info.name = prop_name
        # prop.value = int(np.count_nonzero(lab_img == label))
        prop.value = Value(0, self._px_unit * self._px_unit)
        prop.prop_type = PropertyType.Scalar
        prop.val_names = ['Area']
        prop.num_vals = 1
        prop.prop_comp_key = prop.info.key
        prop.local_key = prop_name
        return prop

    def target_worksheet(self, prop_name: str) -> str:
        return super().target_worksheet('area')

    @property
    def group(self) -> str:
        return super().group
