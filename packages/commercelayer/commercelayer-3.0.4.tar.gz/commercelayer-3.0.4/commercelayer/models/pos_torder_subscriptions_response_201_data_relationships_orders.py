from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torder_subscriptions_response_201_data_relationships_orders_data import (
        POSTorderSubscriptionsResponse201DataRelationshipsOrdersData,
    )
    from ..models.pos_torder_subscriptions_response_201_data_relationships_orders_links import (
        POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks,
    )


T = TypeVar("T", bound="POSTorderSubscriptionsResponse201DataRelationshipsOrders")


@attr.s(auto_attribs=True)
class POSTorderSubscriptionsResponse201DataRelationshipsOrders:
    """
    Attributes:
        links (Union[Unset, POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks]):
        data (Union[Unset, POSTorderSubscriptionsResponse201DataRelationshipsOrdersData]):
    """

    links: Union[Unset, "POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks"] = UNSET
    data: Union[Unset, "POSTorderSubscriptionsResponse201DataRelationshipsOrdersData"] = UNSET
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
        from ..models.pos_torder_subscriptions_response_201_data_relationships_orders_data import (
            POSTorderSubscriptionsResponse201DataRelationshipsOrdersData,
        )
        from ..models.pos_torder_subscriptions_response_201_data_relationships_orders_links import (
            POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTorderSubscriptionsResponse201DataRelationshipsOrdersLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTorderSubscriptionsResponse201DataRelationshipsOrdersData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTorderSubscriptionsResponse201DataRelationshipsOrdersData.from_dict(_data)

        pos_torder_subscriptions_response_201_data_relationships_orders = cls(
            links=links,
            data=data,
        )

        pos_torder_subscriptions_response_201_data_relationships_orders.additional_properties = d
        return pos_torder_subscriptions_response_201_data_relationships_orders

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
