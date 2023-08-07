from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_copy_data_relationships_events import OrderCopyDataRelationshipsEvents
    from ..models.order_copy_data_relationships_order_subscription import OrderCopyDataRelationshipsOrderSubscription
    from ..models.order_copy_data_relationships_source_order import OrderCopyDataRelationshipsSourceOrder
    from ..models.order_copy_data_relationships_target_order import OrderCopyDataRelationshipsTargetOrder


T = TypeVar("T", bound="OrderCopyDataRelationships")


@attr.s(auto_attribs=True)
class OrderCopyDataRelationships:
    """
    Attributes:
        source_order (Union[Unset, OrderCopyDataRelationshipsSourceOrder]):
        target_order (Union[Unset, OrderCopyDataRelationshipsTargetOrder]):
        order_subscription (Union[Unset, OrderCopyDataRelationshipsOrderSubscription]):
        events (Union[Unset, OrderCopyDataRelationshipsEvents]):
    """

    source_order: Union[Unset, "OrderCopyDataRelationshipsSourceOrder"] = UNSET
    target_order: Union[Unset, "OrderCopyDataRelationshipsTargetOrder"] = UNSET
    order_subscription: Union[Unset, "OrderCopyDataRelationshipsOrderSubscription"] = UNSET
    events: Union[Unset, "OrderCopyDataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_order, Unset):
            source_order = self.source_order.to_dict()

        target_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_order, Unset):
            target_order = self.target_order.to_dict()

        order_subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_subscription, Unset):
            order_subscription = self.order_subscription.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_order is not UNSET:
            field_dict["source_order"] = source_order
        if target_order is not UNSET:
            field_dict["target_order"] = target_order
        if order_subscription is not UNSET:
            field_dict["order_subscription"] = order_subscription
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_copy_data_relationships_events import OrderCopyDataRelationshipsEvents
        from ..models.order_copy_data_relationships_order_subscription import (
            OrderCopyDataRelationshipsOrderSubscription,
        )
        from ..models.order_copy_data_relationships_source_order import OrderCopyDataRelationshipsSourceOrder
        from ..models.order_copy_data_relationships_target_order import OrderCopyDataRelationshipsTargetOrder

        d = src_dict.copy()
        _source_order = d.pop("source_order", UNSET)
        source_order: Union[Unset, OrderCopyDataRelationshipsSourceOrder]
        if isinstance(_source_order, Unset):
            source_order = UNSET
        else:
            source_order = OrderCopyDataRelationshipsSourceOrder.from_dict(_source_order)

        _target_order = d.pop("target_order", UNSET)
        target_order: Union[Unset, OrderCopyDataRelationshipsTargetOrder]
        if isinstance(_target_order, Unset):
            target_order = UNSET
        else:
            target_order = OrderCopyDataRelationshipsTargetOrder.from_dict(_target_order)

        _order_subscription = d.pop("order_subscription", UNSET)
        order_subscription: Union[Unset, OrderCopyDataRelationshipsOrderSubscription]
        if isinstance(_order_subscription, Unset):
            order_subscription = UNSET
        else:
            order_subscription = OrderCopyDataRelationshipsOrderSubscription.from_dict(_order_subscription)

        _events = d.pop("events", UNSET)
        events: Union[Unset, OrderCopyDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = OrderCopyDataRelationshipsEvents.from_dict(_events)

        order_copy_data_relationships = cls(
            source_order=source_order,
            target_order=target_order,
            order_subscription=order_subscription,
            events=events,
        )

        order_copy_data_relationships.additional_properties = d
        return order_copy_data_relationships

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
