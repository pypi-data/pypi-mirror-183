from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_copies_response_200_data_item_relationships_events import (
        GETorderCopiesResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_torder_copies_response_200_data_item_relationships_order_subscription import (
        GETorderCopiesResponse200DataItemRelationshipsOrderSubscription,
    )
    from ..models.ge_torder_copies_response_200_data_item_relationships_source_order import (
        GETorderCopiesResponse200DataItemRelationshipsSourceOrder,
    )
    from ..models.ge_torder_copies_response_200_data_item_relationships_target_order import (
        GETorderCopiesResponse200DataItemRelationshipsTargetOrder,
    )


T = TypeVar("T", bound="GETorderCopiesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETorderCopiesResponse200DataItemRelationships:
    """
    Attributes:
        source_order (Union[Unset, GETorderCopiesResponse200DataItemRelationshipsSourceOrder]):
        target_order (Union[Unset, GETorderCopiesResponse200DataItemRelationshipsTargetOrder]):
        order_subscription (Union[Unset, GETorderCopiesResponse200DataItemRelationshipsOrderSubscription]):
        events (Union[Unset, GETorderCopiesResponse200DataItemRelationshipsEvents]):
    """

    source_order: Union[Unset, "GETorderCopiesResponse200DataItemRelationshipsSourceOrder"] = UNSET
    target_order: Union[Unset, "GETorderCopiesResponse200DataItemRelationshipsTargetOrder"] = UNSET
    order_subscription: Union[Unset, "GETorderCopiesResponse200DataItemRelationshipsOrderSubscription"] = UNSET
    events: Union[Unset, "GETorderCopiesResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_torder_copies_response_200_data_item_relationships_events import (
            GETorderCopiesResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_torder_copies_response_200_data_item_relationships_order_subscription import (
            GETorderCopiesResponse200DataItemRelationshipsOrderSubscription,
        )
        from ..models.ge_torder_copies_response_200_data_item_relationships_source_order import (
            GETorderCopiesResponse200DataItemRelationshipsSourceOrder,
        )
        from ..models.ge_torder_copies_response_200_data_item_relationships_target_order import (
            GETorderCopiesResponse200DataItemRelationshipsTargetOrder,
        )

        d = src_dict.copy()
        _source_order = d.pop("source_order", UNSET)
        source_order: Union[Unset, GETorderCopiesResponse200DataItemRelationshipsSourceOrder]
        if isinstance(_source_order, Unset):
            source_order = UNSET
        else:
            source_order = GETorderCopiesResponse200DataItemRelationshipsSourceOrder.from_dict(_source_order)

        _target_order = d.pop("target_order", UNSET)
        target_order: Union[Unset, GETorderCopiesResponse200DataItemRelationshipsTargetOrder]
        if isinstance(_target_order, Unset):
            target_order = UNSET
        else:
            target_order = GETorderCopiesResponse200DataItemRelationshipsTargetOrder.from_dict(_target_order)

        _order_subscription = d.pop("order_subscription", UNSET)
        order_subscription: Union[Unset, GETorderCopiesResponse200DataItemRelationshipsOrderSubscription]
        if isinstance(_order_subscription, Unset):
            order_subscription = UNSET
        else:
            order_subscription = GETorderCopiesResponse200DataItemRelationshipsOrderSubscription.from_dict(
                _order_subscription
            )

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETorderCopiesResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETorderCopiesResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_torder_copies_response_200_data_item_relationships = cls(
            source_order=source_order,
            target_order=target_order,
            order_subscription=order_subscription,
            events=events,
        )

        ge_torder_copies_response_200_data_item_relationships.additional_properties = d
        return ge_torder_copies_response_200_data_item_relationships

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
