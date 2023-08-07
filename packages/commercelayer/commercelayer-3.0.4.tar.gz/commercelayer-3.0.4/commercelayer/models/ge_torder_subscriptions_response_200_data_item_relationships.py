from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer import (
        GETorderSubscriptionsResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_events import (
        GETorderSubscriptionsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_market import (
        GETorderSubscriptionsResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies import (
        GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_orders import (
        GETorderSubscriptionsResponse200DataItemRelationshipsOrders,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_source_order import (
        GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder,
    )


T = TypeVar("T", bound="GETorderSubscriptionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETorderSubscriptionsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsMarket]):
        source_order (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder]):
        customer (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomer]):
        order_copies (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies]):
        orders (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrders]):
        events (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsEvents]):
    """

    market: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsMarket"] = UNSET
    source_order: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder"] = UNSET
    customer: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsCustomer"] = UNSET
    order_copies: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies"] = UNSET
    orders: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsOrders"] = UNSET
    events: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer import (
            GETorderSubscriptionsResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_events import (
            GETorderSubscriptionsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_market import (
            GETorderSubscriptionsResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_order_copies import (
            GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_orders import (
            GETorderSubscriptionsResponse200DataItemRelationshipsOrders,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_source_order import (
            GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETorderSubscriptionsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _source_order = d.pop("source_order", UNSET)
        source_order: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder]
        if isinstance(_source_order, Unset):
            source_order = UNSET
        else:
            source_order = GETorderSubscriptionsResponse200DataItemRelationshipsSourceOrder.from_dict(_source_order)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETorderSubscriptionsResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = GETorderSubscriptionsResponse200DataItemRelationshipsOrderCopies.from_dict(_order_copies)

        _orders = d.pop("orders", UNSET)
        orders: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsOrders]
        if isinstance(_orders, Unset):
            orders = UNSET
        else:
            orders = GETorderSubscriptionsResponse200DataItemRelationshipsOrders.from_dict(_orders)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETorderSubscriptionsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_torder_subscriptions_response_200_data_item_relationships = cls(
            market=market,
            source_order=source_order,
            customer=customer,
            order_copies=order_copies,
            orders=orders,
            events=events,
        )

        ge_torder_subscriptions_response_200_data_item_relationships.additional_properties = d
        return ge_torder_subscriptions_response_200_data_item_relationships

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
