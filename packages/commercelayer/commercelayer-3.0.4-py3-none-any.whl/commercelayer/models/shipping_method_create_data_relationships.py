from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_method_create_data_relationships_market import ShippingMethodCreateDataRelationshipsMarket
    from ..models.shipping_method_create_data_relationships_shipping_category import (
        ShippingMethodCreateDataRelationshipsShippingCategory,
    )
    from ..models.shipping_method_create_data_relationships_shipping_method_tiers import (
        ShippingMethodCreateDataRelationshipsShippingMethodTiers,
    )
    from ..models.shipping_method_create_data_relationships_shipping_zone import (
        ShippingMethodCreateDataRelationshipsShippingZone,
    )
    from ..models.shipping_method_create_data_relationships_stock_location import (
        ShippingMethodCreateDataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="ShippingMethodCreateDataRelationships")


@attr.s(auto_attribs=True)
class ShippingMethodCreateDataRelationships:
    """
    Attributes:
        market (Union[Unset, ShippingMethodCreateDataRelationshipsMarket]):
        shipping_zone (Union[Unset, ShippingMethodCreateDataRelationshipsShippingZone]):
        shipping_category (Union[Unset, ShippingMethodCreateDataRelationshipsShippingCategory]):
        stock_location (Union[Unset, ShippingMethodCreateDataRelationshipsStockLocation]):
        shipping_method_tiers (Union[Unset, ShippingMethodCreateDataRelationshipsShippingMethodTiers]):
    """

    market: Union[Unset, "ShippingMethodCreateDataRelationshipsMarket"] = UNSET
    shipping_zone: Union[Unset, "ShippingMethodCreateDataRelationshipsShippingZone"] = UNSET
    shipping_category: Union[Unset, "ShippingMethodCreateDataRelationshipsShippingCategory"] = UNSET
    stock_location: Union[Unset, "ShippingMethodCreateDataRelationshipsStockLocation"] = UNSET
    shipping_method_tiers: Union[Unset, "ShippingMethodCreateDataRelationshipsShippingMethodTiers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        shipping_zone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_zone, Unset):
            shipping_zone = self.shipping_zone.to_dict()

        shipping_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_category, Unset):
            shipping_category = self.shipping_category.to_dict()

        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        shipping_method_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method_tiers, Unset):
            shipping_method_tiers = self.shipping_method_tiers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if shipping_zone is not UNSET:
            field_dict["shipping_zone"] = shipping_zone
        if shipping_category is not UNSET:
            field_dict["shipping_category"] = shipping_category
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if shipping_method_tiers is not UNSET:
            field_dict["shipping_method_tiers"] = shipping_method_tiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_method_create_data_relationships_market import (
            ShippingMethodCreateDataRelationshipsMarket,
        )
        from ..models.shipping_method_create_data_relationships_shipping_category import (
            ShippingMethodCreateDataRelationshipsShippingCategory,
        )
        from ..models.shipping_method_create_data_relationships_shipping_method_tiers import (
            ShippingMethodCreateDataRelationshipsShippingMethodTiers,
        )
        from ..models.shipping_method_create_data_relationships_shipping_zone import (
            ShippingMethodCreateDataRelationshipsShippingZone,
        )
        from ..models.shipping_method_create_data_relationships_stock_location import (
            ShippingMethodCreateDataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, ShippingMethodCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = ShippingMethodCreateDataRelationshipsMarket.from_dict(_market)

        _shipping_zone = d.pop("shipping_zone", UNSET)
        shipping_zone: Union[Unset, ShippingMethodCreateDataRelationshipsShippingZone]
        if isinstance(_shipping_zone, Unset):
            shipping_zone = UNSET
        else:
            shipping_zone = ShippingMethodCreateDataRelationshipsShippingZone.from_dict(_shipping_zone)

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, ShippingMethodCreateDataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = ShippingMethodCreateDataRelationshipsShippingCategory.from_dict(_shipping_category)

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, ShippingMethodCreateDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = ShippingMethodCreateDataRelationshipsStockLocation.from_dict(_stock_location)

        _shipping_method_tiers = d.pop("shipping_method_tiers", UNSET)
        shipping_method_tiers: Union[Unset, ShippingMethodCreateDataRelationshipsShippingMethodTiers]
        if isinstance(_shipping_method_tiers, Unset):
            shipping_method_tiers = UNSET
        else:
            shipping_method_tiers = ShippingMethodCreateDataRelationshipsShippingMethodTiers.from_dict(
                _shipping_method_tiers
            )

        shipping_method_create_data_relationships = cls(
            market=market,
            shipping_zone=shipping_zone,
            shipping_category=shipping_category,
            stock_location=stock_location,
            shipping_method_tiers=shipping_method_tiers,
        )

        shipping_method_create_data_relationships.additional_properties = d
        return shipping_method_create_data_relationships

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
