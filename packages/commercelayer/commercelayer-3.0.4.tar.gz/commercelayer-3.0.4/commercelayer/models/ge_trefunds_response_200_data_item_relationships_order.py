from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_trefunds_response_200_data_item_relationships_order_data import (
        GETrefundsResponse200DataItemRelationshipsOrderData,
    )
    from ..models.ge_trefunds_response_200_data_item_relationships_order_links import (
        GETrefundsResponse200DataItemRelationshipsOrderLinks,
    )


T = TypeVar("T", bound="GETrefundsResponse200DataItemRelationshipsOrder")


@attr.s(auto_attribs=True)
class GETrefundsResponse200DataItemRelationshipsOrder:
    """
    Attributes:
        links (Union[Unset, GETrefundsResponse200DataItemRelationshipsOrderLinks]):
        data (Union[Unset, GETrefundsResponse200DataItemRelationshipsOrderData]):
    """

    links: Union[Unset, "GETrefundsResponse200DataItemRelationshipsOrderLinks"] = UNSET
    data: Union[Unset, "GETrefundsResponse200DataItemRelationshipsOrderData"] = UNSET
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
        from ..models.ge_trefunds_response_200_data_item_relationships_order_data import (
            GETrefundsResponse200DataItemRelationshipsOrderData,
        )
        from ..models.ge_trefunds_response_200_data_item_relationships_order_links import (
            GETrefundsResponse200DataItemRelationshipsOrderLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETrefundsResponse200DataItemRelationshipsOrderLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETrefundsResponse200DataItemRelationshipsOrderLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETrefundsResponse200DataItemRelationshipsOrderData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETrefundsResponse200DataItemRelationshipsOrderData.from_dict(_data)

        ge_trefunds_response_200_data_item_relationships_order = cls(
            links=links,
            data=data,
        )

        ge_trefunds_response_200_data_item_relationships_order.additional_properties = d
        return ge_trefunds_response_200_data_item_relationships_order

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
