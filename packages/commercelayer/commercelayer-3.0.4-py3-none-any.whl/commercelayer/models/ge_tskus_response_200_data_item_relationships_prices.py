from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tskus_response_200_data_item_relationships_prices_data import (
        GETskusResponse200DataItemRelationshipsPricesData,
    )
    from ..models.ge_tskus_response_200_data_item_relationships_prices_links import (
        GETskusResponse200DataItemRelationshipsPricesLinks,
    )


T = TypeVar("T", bound="GETskusResponse200DataItemRelationshipsPrices")


@attr.s(auto_attribs=True)
class GETskusResponse200DataItemRelationshipsPrices:
    """
    Attributes:
        links (Union[Unset, GETskusResponse200DataItemRelationshipsPricesLinks]):
        data (Union[Unset, GETskusResponse200DataItemRelationshipsPricesData]):
    """

    links: Union[Unset, "GETskusResponse200DataItemRelationshipsPricesLinks"] = UNSET
    data: Union[Unset, "GETskusResponse200DataItemRelationshipsPricesData"] = UNSET
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
        from ..models.ge_tskus_response_200_data_item_relationships_prices_data import (
            GETskusResponse200DataItemRelationshipsPricesData,
        )
        from ..models.ge_tskus_response_200_data_item_relationships_prices_links import (
            GETskusResponse200DataItemRelationshipsPricesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETskusResponse200DataItemRelationshipsPricesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETskusResponse200DataItemRelationshipsPricesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETskusResponse200DataItemRelationshipsPricesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETskusResponse200DataItemRelationshipsPricesData.from_dict(_data)

        ge_tskus_response_200_data_item_relationships_prices = cls(
            links=links,
            data=data,
        )

        ge_tskus_response_200_data_item_relationships_prices.additional_properties = d
        return ge_tskus_response_200_data_item_relationships_prices

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
