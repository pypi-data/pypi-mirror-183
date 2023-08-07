from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_customer import (
        GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_events import (
        GETinStockSubscriptionsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_market import (
        GETinStockSubscriptionsResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_sku import (
        GETinStockSubscriptionsResponse200DataItemRelationshipsSku,
    )


T = TypeVar("T", bound="GETinStockSubscriptionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETinStockSubscriptionsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsMarket]):
        customer (Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer]):
        sku (Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsSku]):
        events (Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsEvents]):
    """

    market: Union[Unset, "GETinStockSubscriptionsResponse200DataItemRelationshipsMarket"] = UNSET
    customer: Union[Unset, "GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer"] = UNSET
    sku: Union[Unset, "GETinStockSubscriptionsResponse200DataItemRelationshipsSku"] = UNSET
    events: Union[Unset, "GETinStockSubscriptionsResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if customer is not UNSET:
            field_dict["customer"] = customer
        if sku is not UNSET:
            field_dict["sku"] = sku
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_customer import (
            GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_events import (
            GETinStockSubscriptionsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_market import (
            GETinStockSubscriptionsResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_tin_stock_subscriptions_response_200_data_item_relationships_sku import (
            GETinStockSubscriptionsResponse200DataItemRelationshipsSku,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETinStockSubscriptionsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETinStockSubscriptionsResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETinStockSubscriptionsResponse200DataItemRelationshipsSku.from_dict(_sku)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETinStockSubscriptionsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETinStockSubscriptionsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tin_stock_subscriptions_response_200_data_item_relationships = cls(
            market=market,
            customer=customer,
            sku=sku,
            events=events,
        )

        ge_tin_stock_subscriptions_response_200_data_item_relationships.additional_properties = d
        return ge_tin_stock_subscriptions_response_200_data_item_relationships

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
