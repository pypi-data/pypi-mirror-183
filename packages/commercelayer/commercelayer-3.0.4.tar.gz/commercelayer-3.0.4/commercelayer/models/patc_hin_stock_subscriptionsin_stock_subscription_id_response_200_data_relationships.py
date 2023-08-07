from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_customer import (
        PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer,
    )
    from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_events import (
        PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_market import (
        PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket,
    )
    from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku import (
        PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku,
    )


T = TypeVar("T", bound="PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket]):
        customer (Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer]):
        sku (Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku]):
        events (Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents]):
    """

    market: Union[Unset, "PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer"] = UNSET
    sku: Union[Unset, "PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku"] = UNSET
    events: Union[Unset, "PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_customer import (
            PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer,
        )
        from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_events import (
            PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_market import (
            PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket,
        )
        from ..models.patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku import (
            PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsCustomer.from_dict(
                _customer
            )

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku.from_dict(_sku)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships = cls(
            market=market,
            customer=customer,
            sku=sku,
            events=events,
        )

        patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships.additional_properties = d
        return patc_hin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships

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
