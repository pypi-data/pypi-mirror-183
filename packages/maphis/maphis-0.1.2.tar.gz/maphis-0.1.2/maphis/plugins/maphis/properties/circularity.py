import copy
import typing
from typing import List, Optional

import numpy as np
import skimage

from maphis.common.common import Info
from maphis.common.label_image import RegionProperty, PropertyType
from maphis.common.photo import Photo
from maphis.common.plugin import PropertyComputation
from maphis.common.regions_cache import RegionsCache, Region
from maphis.common.units import Value, Unit, BaseUnit, SIPrefix
from maphis.common.user_params import UserParam


class Circularity(PropertyComputation):
    """
    GROUP: Shape measurements
    NAME: Circularity
    DESCRIPTION: Circularity (0.0 to 1.0, where 1.0 = perfect circle)
    KEY: circularity
    """
    def __init__(self, info: Optional[Info] = None):
        super().__init__(info)

    def __call__(self, photo: Photo, region_labels: typing.List[int], regions_cache: RegionsCache, prop_names: typing.List[str]) -> \
            typing.List[RegionProperty]:

        # lab_img = photo['Labels']
        # reg_props = skimage.measure.regionprops_table(lab_img.label_image, photo.image,
        #                                               properties=['label', 'perimeter'])  #perimeter_measurement_flavor])
        props: List[RegionProperty] = []

        # for idx, label in enumerate(reg_props['label']):
        for label in region_labels:
            # if label not in region_labels:
            #     continue
            if label not in regions_cache.regions:
                continue
            region_obj = regions_cache.regions[label]
            reg_perimeter_prop = skimage.measure.regionprops_table(1 * region_obj.mask, region_obj.image,
                                                                   properties=['perimeter'])
            # perimeter = reg_props['perimeter'][idx]#[perimeter_measurement_flavor][idx]
            perimeter = reg_perimeter_prop['perimeter'][0]
            # area = int(np.count_nonzero(lab_img == label))
            # area = int(np.count_nonzero(lab_img.mask_for(label)))
            area = int(np.count_nonzero(region_obj.mask))
            if perimeter == 0:
                circularity = 0 # TODO: Careful about division by zero (can we somehow return N/A here?)
            else:
                circularity = np.clip((4 * np.pi * area) / (perimeter ** 2), 0.0, 1.0)
            #print(f'idx: {idx}, label: {label}')
            #print(f'  perimeter: {perimeter}')
            #print(f'  area: {area}')
            #print(f'  circularity: {circularity}')

            prop = self.example('circularity')
            prop.label = int(label)
            prop.info = copy.deepcopy(self.info)
            prop.value = Value(float(circularity), self._no_unit)
            # prop.unit = '' # TODO: Is this ok for a unitless property?
            prop.prop_type = PropertyType.Scalar
            prop.val_names = [self.info.name]
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
        return {self.info.key: self.info}

    def example(self, prop_name: str) -> RegionProperty:
        prop = super().example(prop_name)
        prop.label = 0
        prop.info = copy.deepcopy(self.info)
        prop.info.name = prop_name
        # prop.value = int(np.count_nonzero(lab_img == label))
        prop.value = Value(0, self._no_unit)
        prop.prop_type = PropertyType.Scalar
        prop.val_names = [self.info.name]
        prop.num_vals = 1
        return prop

    def target_worksheet(self, prop_name: str) -> str:
        return super().target_worksheet(self.info.key)

    @property
    def group(self) -> str:
        return super().group
