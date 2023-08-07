from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_stock_subscription_update_data_relationships_customer import (
        InStockSubscriptionUpdateDataRelationshipsCustomer,
    )
    from ..models.in_stock_subscription_update_data_relationships_market import (
        InStockSubscriptionUpdateDataRelationshipsMarket,
    )
    from ..models.in_stock_subscription_update_data_relationships_sku import (
        InStockSubscriptionUpdateDataRelationshipsSku,
    )


T = TypeVar("T", bound="InStockSubscriptionUpdateDataRelationships")


@attr.s(auto_attribs=True)
class InStockSubscriptionUpdateDataRelationships:
    """
    Attributes:
        market (Union[Unset, InStockSubscriptionUpdateDataRelationshipsMarket]):
        customer (Union[Unset, InStockSubscriptionUpdateDataRelationshipsCustomer]):
        sku (Union[Unset, InStockSubscriptionUpdateDataRelationshipsSku]):
    """

    market: Union[Unset, "InStockSubscriptionUpdateDataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "InStockSubscriptionUpdateDataRelationshipsCustomer"] = UNSET
    sku: Union[Unset, "InStockSubscriptionUpdateDataRelationshipsSku"] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if customer is not UNSET:
            field_dict["customer"] = customer
        if sku is not UNSET:
            field_dict["sku"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.in_stock_subscription_update_data_relationships_customer import (
            InStockSubscriptionUpdateDataRelationshipsCustomer,
        )
        from ..models.in_stock_subscription_update_data_relationships_market import (
            InStockSubscriptionUpdateDataRelationshipsMarket,
        )
        from ..models.in_stock_subscription_update_data_relationships_sku import (
            InStockSubscriptionUpdateDataRelationshipsSku,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, InStockSubscriptionUpdateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = InStockSubscriptionUpdateDataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, InStockSubscriptionUpdateDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = InStockSubscriptionUpdateDataRelationshipsCustomer.from_dict(_customer)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, InStockSubscriptionUpdateDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = InStockSubscriptionUpdateDataRelationshipsSku.from_dict(_sku)

        in_stock_subscription_update_data_relationships = cls(
            market=market,
            customer=customer,
            sku=sku,
        )

        in_stock_subscription_update_data_relationships.additional_properties = d
        return in_stock_subscription_update_data_relationships

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
