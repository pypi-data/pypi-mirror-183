from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_subscription_create_data_relationships_market import (
        OrderSubscriptionCreateDataRelationshipsMarket,
    )
    from ..models.order_subscription_create_data_relationships_source_order import (
        OrderSubscriptionCreateDataRelationshipsSourceOrder,
    )


T = TypeVar("T", bound="OrderSubscriptionCreateDataRelationships")


@attr.s(auto_attribs=True)
class OrderSubscriptionCreateDataRelationships:
    """
    Attributes:
        source_order (OrderSubscriptionCreateDataRelationshipsSourceOrder):
        market (Union[Unset, OrderSubscriptionCreateDataRelationshipsMarket]):
    """

    source_order: "OrderSubscriptionCreateDataRelationshipsSourceOrder"
    market: Union[Unset, "OrderSubscriptionCreateDataRelationshipsMarket"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_order = self.source_order.to_dict()

        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_order": source_order,
            }
        )
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_subscription_create_data_relationships_market import (
            OrderSubscriptionCreateDataRelationshipsMarket,
        )
        from ..models.order_subscription_create_data_relationships_source_order import (
            OrderSubscriptionCreateDataRelationshipsSourceOrder,
        )

        d = src_dict.copy()
        source_order = OrderSubscriptionCreateDataRelationshipsSourceOrder.from_dict(d.pop("source_order"))

        _market = d.pop("market", UNSET)
        market: Union[Unset, OrderSubscriptionCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = OrderSubscriptionCreateDataRelationshipsMarket.from_dict(_market)

        order_subscription_create_data_relationships = cls(
            source_order=source_order,
            market=market,
        )

        order_subscription_create_data_relationships.additional_properties = d
        return order_subscription_create_data_relationships

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
