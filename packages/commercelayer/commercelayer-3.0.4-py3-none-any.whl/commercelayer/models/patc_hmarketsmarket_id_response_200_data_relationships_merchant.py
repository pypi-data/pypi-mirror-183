from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hmarketsmarket_id_response_200_data_relationships_merchant_data import (
        PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData,
    )
    from ..models.patc_hmarketsmarket_id_response_200_data_relationships_merchant_links import (
        PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks,
    )


T = TypeVar("T", bound="PATCHmarketsmarketIdResponse200DataRelationshipsMerchant")


@attr.s(auto_attribs=True)
class PATCHmarketsmarketIdResponse200DataRelationshipsMerchant:
    """
    Attributes:
        links (Union[Unset, PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks]):
        data (Union[Unset, PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData]):
    """

    links: Union[Unset, "PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks"] = UNSET
    data: Union[Unset, "PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData"] = UNSET
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
        from ..models.patc_hmarketsmarket_id_response_200_data_relationships_merchant_data import (
            PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData,
        )
        from ..models.patc_hmarketsmarket_id_response_200_data_relationships_merchant_links import (
            PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHmarketsmarketIdResponse200DataRelationshipsMerchantLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHmarketsmarketIdResponse200DataRelationshipsMerchantData.from_dict(_data)

        patc_hmarketsmarket_id_response_200_data_relationships_merchant = cls(
            links=links,
            data=data,
        )

        patc_hmarketsmarket_id_response_200_data_relationships_merchant.additional_properties = d
        return patc_hmarketsmarket_id_response_200_data_relationships_merchant

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
