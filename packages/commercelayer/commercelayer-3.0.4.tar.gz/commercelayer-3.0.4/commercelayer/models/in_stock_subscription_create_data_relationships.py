from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.in_stock_subscription_create_data_relationships_customer import (
        InStockSubscriptionCreateDataRelationshipsCustomer,
    )
    from ..models.in_stock_subscription_create_data_relationships_market import (
        InStockSubscriptionCreateDataRelationshipsMarket,
    )
    from ..models.in_stock_subscription_create_data_relationships_sku import (
        InStockSubscriptionCreateDataRelationshipsSku,
    )


T = TypeVar("T", bound="InStockSubscriptionCreateDataRelationships")


@attr.s(auto_attribs=True)
class InStockSubscriptionCreateDataRelationships:
    """
    Attributes:
        market (InStockSubscriptionCreateDataRelationshipsMarket):
        customer (InStockSubscriptionCreateDataRelationshipsCustomer):
        sku (InStockSubscriptionCreateDataRelationshipsSku):
    """

    market: "InStockSubscriptionCreateDataRelationshipsMarket"
    customer: "InStockSubscriptionCreateDataRelationshipsCustomer"
    sku: "InStockSubscriptionCreateDataRelationshipsSku"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market = self.market.to_dict()

        customer = self.customer.to_dict()

        sku = self.sku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market": market,
                "customer": customer,
                "sku": sku,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.in_stock_subscription_create_data_relationships_customer import (
            InStockSubscriptionCreateDataRelationshipsCustomer,
        )
        from ..models.in_stock_subscription_create_data_relationships_market import (
            InStockSubscriptionCreateDataRelationshipsMarket,
        )
        from ..models.in_stock_subscription_create_data_relationships_sku import (
            InStockSubscriptionCreateDataRelationshipsSku,
        )

        d = src_dict.copy()
        market = InStockSubscriptionCreateDataRelationshipsMarket.from_dict(d.pop("market"))

        customer = InStockSubscriptionCreateDataRelationshipsCustomer.from_dict(d.pop("customer"))

        sku = InStockSubscriptionCreateDataRelationshipsSku.from_dict(d.pop("sku"))

        in_stock_subscription_create_data_relationships = cls(
            market=market,
            customer=customer,
            sku=sku,
        )

        in_stock_subscription_create_data_relationships.additional_properties = d
        return in_stock_subscription_create_data_relationships

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
