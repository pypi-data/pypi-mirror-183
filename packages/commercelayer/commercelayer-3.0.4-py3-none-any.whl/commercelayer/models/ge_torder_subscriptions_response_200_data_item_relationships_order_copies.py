from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies_data import (
        GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies_links import (
        GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks,
    )


T = TypeVar("T", bound="GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies")


@attr.s(auto_attribs=True)
class GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies:
    """
    Attributes:
        links (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks]):
        data (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData]):
    """

    links: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks"] = UNSET
    data: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData"] = UNSET
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
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies_data import (
            GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies_links import (
            GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopiesData.from_dict(_data)

        ge_torder_subscriptions_response_200_data_item_relationships_order_copies = cls(
            links=links,
            data=data,
        )

        ge_torder_subscriptions_response_200_data_item_relationships_order_copies.additional_properties = d
        return ge_torder_subscriptions_response_200_data_item_relationships_order_copies

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
