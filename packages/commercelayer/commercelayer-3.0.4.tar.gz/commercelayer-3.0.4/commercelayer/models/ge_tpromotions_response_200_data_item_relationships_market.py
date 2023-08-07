from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpromotions_response_200_data_item_relationships_market_data import (
        GETpromotionsResponse200DataItemRelationshipsMarketData,
    )
    from ..models.ge_tpromotions_response_200_data_item_relationships_market_links import (
        GETpromotionsResponse200DataItemRelationshipsMarketLinks,
    )


T = TypeVar("T", bound="GETpromotionsResponse200DataItemRelationshipsMarket")


@attr.s(auto_attribs=True)
class GETpromotionsResponse200DataItemRelationshipsMarket:
    """
    Attributes:
        links (Union[Unset, GETpromotionsResponse200DataItemRelationshipsMarketLinks]):
        data (Union[Unset, GETpromotionsResponse200DataItemRelationshipsMarketData]):
    """

    links: Union[Unset, "GETpromotionsResponse200DataItemRelationshipsMarketLinks"] = UNSET
    data: Union[Unset, "GETpromotionsResponse200DataItemRelationshipsMarketData"] = UNSET
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
        from ..models.ge_tpromotions_response_200_data_item_relationships_market_data import (
            GETpromotionsResponse200DataItemRelationshipsMarketData,
        )
        from ..models.ge_tpromotions_response_200_data_item_relationships_market_links import (
            GETpromotionsResponse200DataItemRelationshipsMarketLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETpromotionsResponse200DataItemRelationshipsMarketLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETpromotionsResponse200DataItemRelationshipsMarketLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETpromotionsResponse200DataItemRelationshipsMarketData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETpromotionsResponse200DataItemRelationshipsMarketData.from_dict(_data)

        ge_tpromotions_response_200_data_item_relationships_market = cls(
            links=links,
            data=data,
        )

        ge_tpromotions_response_200_data_item_relationships_market.additional_properties = d
        return ge_tpromotions_response_200_data_item_relationships_market

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
