from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method_data import (
        GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData,
    )
    from ..models.ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method_links import (
        GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks,
    )


T = TypeVar("T", bound="GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod")


@attr.s(auto_attribs=True)
class GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethod:
    """
    Attributes:
        links (Union[Unset, GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks]):
        data (Union[Unset, GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData]):
    """

    links: Union[
        Unset, "GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks"
    ] = UNSET
    data: Union[
        Unset, "GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method_data import (
            GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData,
        )
        from ..models.ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method_links import (
            GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsShippingMethodData.from_dict(
                _data
            )

        ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method = cls(
            links=links,
            data=data,
        )

        ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method.additional_properties = (
            d
        )
        return ge_tshipping_weight_tiersshipping_weight_tier_id_response_200_data_relationships_shipping_method

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
