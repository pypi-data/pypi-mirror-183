from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers_data import (
        PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData,
    )
    from ..models.patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers_links import (
        PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks,
    )


T = TypeVar("T", bound="PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiers")


@attr.s(auto_attribs=True)
class PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiers:
    """
    Attributes:
        links (Union[Unset, PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks]):
        data (Union[Unset, PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData]):
    """

    links: Union[Unset, "PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks"] = UNSET
    data: Union[Unset, "PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData"] = UNSET
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
        from ..models.patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers_data import (
            PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData,
        )
        from ..models.patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers_links import (
            PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHpricespriceIdResponse200DataRelationshipsPriceVolumeTiersData.from_dict(_data)

        patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers = cls(
            links=links,
            data=data,
        )

        patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers.additional_properties = d
        return patc_hpricesprice_id_response_200_data_relationships_price_volume_tiers

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
