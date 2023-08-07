from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_customer import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer,
    )
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_events import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_market import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket,
    )
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_order_copies import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies,
    )
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_orders import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders,
    )
    from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_source_order import (
        PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder,
    )


T = TypeVar("T", bound="PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket]):
        source_order (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder]):
        customer (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer]):
        order_copies (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies]):
        orders (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders]):
        events (Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents]):
    """

    market: Union[Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket"] = UNSET
    source_order: Union[
        Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder"
    ] = UNSET
    customer: Union[Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer"] = UNSET
    order_copies: Union[
        Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies"
    ] = UNSET
    orders: Union[Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders"] = UNSET
    events: Union[Unset, "PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        source_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_order, Unset):
            source_order = self.source_order.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        order_copies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_copies, Unset):
            order_copies = self.order_copies.to_dict()

        orders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = self.orders.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if source_order is not UNSET:
            field_dict["source_order"] = source_order
        if customer is not UNSET:
            field_dict["customer"] = customer
        if order_copies is not UNSET:
            field_dict["order_copies"] = order_copies
        if orders is not UNSET:
            field_dict["orders"] = orders
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_customer import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer,
        )
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_events import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_market import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket,
        )
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_order_copies import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies,
        )
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_orders import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders,
        )
        from ..models.patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships_source_order import (
            PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsMarket.from_dict(_market)

        _source_order = d.pop("source_order", UNSET)
        source_order: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder]
        if isinstance(_source_order, Unset):
            source_order = UNSET
        else:
            source_order = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsSourceOrder.from_dict(
                _source_order
            )

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomer.from_dict(
                _customer
            )

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrderCopies.from_dict(
                _order_copies
            )

        _orders = d.pop("orders", UNSET)
        orders: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders]
        if isinstance(_orders, Unset):
            orders = UNSET
        else:
            orders = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsOrders.from_dict(_orders)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships = cls(
            market=market,
            source_order=source_order,
            customer=customer,
            order_copies=order_copies,
            orders=orders,
            events=events,
        )

        patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships.additional_properties = d
        return patc_horder_subscriptionsorder_subscription_id_response_200_data_relationships

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
