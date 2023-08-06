import copy
import typing
from typing import Optional

import skimage.io
from skimage.morphology import skeletonize, medial_axis

from maphis.common.common import Info
from maphis.common.label_image import RegionProperty, PropertyType
from maphis.common.photo import Photo
from maphis.common.plugin import PropertyComputation
from maphis.common.regions_cache import RegionsCache, Region
from maphis.common.units import Value
from maphis.common.user_params import UserParam
from maphis.plugins.maphis.properties.geodesic_utils import compute_longest_geodesic, \
    compute_longest_geodesic_perf


class GeodesicLength(PropertyComputation):
    """
    GROUP: Length & area measurements
    NAME: Geodesic length
    DESCRIPTION: Geodesic length (px or mm)
    KEY: geodesic_length
    """

    def __init__(self, info: Optional[Info] = None):
        super().__init__(info)

    def __call__(self, photo: Photo, region_labels: typing.List[int], regions_cache: RegionsCache, prop_names: typing.List[str]) -> \
            typing.List[RegionProperty]:
        # lab_img = photo['Labels'].label_image
        props: typing.List[RegionProperty] = []
        for label in region_labels:
            # _, length = get_longest_geodesic(lab_img, label)
            if label not in regions_cache.regions:
                continue
            region_obj = regions_cache.regions[label]
            # length, _, _ = compute_longest_geodesic(region_obj.mask)
            # skeleton = skeletonize(region_obj.mask)
            length = compute_longest_geodesic_perf(region_obj.mask)
            # compute_longest_geodesic(lab_img == label)
            if length < 0:
                continue
            prop = self.example('geodesic_length')
            prop.label = int(label)
            prop.info = copy.deepcopy(self.info)
            value = Value(float(length), self._px_unit)
            if photo.image_scale is not None:
                # prop.unit = 'mm'
                prop.value = value / photo.image_scale
            else:
                prop.value = value
            prop.val_names = ['Geodesic length']
            prop.num_vals = 1
            props.append(prop)
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
        prop.value = None
        prop.num_vals = 1
        prop.prop_type = PropertyType.Scalar
        prop.val_names = []
        return prop

    def target_worksheet(self, prop_name: str) -> str:
        return super().target_worksheet(self.info.key)

    @property
    def group(self) -> str:
        return super().group
