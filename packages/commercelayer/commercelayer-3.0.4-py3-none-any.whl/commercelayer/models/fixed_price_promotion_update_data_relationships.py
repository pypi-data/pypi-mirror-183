from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fixed_price_promotion_update_data_relationships_coupon_codes_promotion_rule import (
        FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule,
    )
    from ..models.fixed_price_promotion_update_data_relationships_market import (
        FixedPricePromotionUpdateDataRelationshipsMarket,
    )
    from ..models.fixed_price_promotion_update_data_relationships_order_amount_promotion_rule import (
        FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule,
    )
    from ..models.fixed_price_promotion_update_data_relationships_promotion_rules import (
        FixedPricePromotionUpdateDataRelationshipsPromotionRules,
    )
    from ..models.fixed_price_promotion_update_data_relationships_sku_list import (
        FixedPricePromotionUpdateDataRelationshipsSkuList,
    )
    from ..models.fixed_price_promotion_update_data_relationships_sku_list_promotion_rule import (
        FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule,
    )


T = TypeVar("T", bound="FixedPricePromotionUpdateDataRelationships")


@attr.s(auto_attribs=True)
class FixedPricePromotionUpdateDataRelationships:
    """
    Attributes:
        market (Union[Unset, FixedPricePromotionUpdateDataRelationshipsMarket]):
        promotion_rules (Union[Unset, FixedPricePromotionUpdateDataRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset, FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset, FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset, FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule]):
        sku_list (Union[Unset, FixedPricePromotionUpdateDataRelationshipsSkuList]):
    """

    market: Union[Unset, "FixedPricePromotionUpdateDataRelationshipsMarket"] = UNSET
    promotion_rules: Union[Unset, "FixedPricePromotionUpdateDataRelationshipsPromotionRules"] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[Unset, "FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule"] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    sku_list: Union[Unset, "FixedPricePromotionUpdateDataRelationshipsSkuList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        promotion_rules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_rules, Unset):
            promotion_rules = self.promotion_rules.to_dict()

        order_amount_promotion_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = self.order_amount_promotion_rule.to_dict()

        sku_list_promotion_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = self.sku_list_promotion_rule.to_dict()

        coupon_codes_promotion_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = self.coupon_codes_promotion_rule.to_dict()

        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if promotion_rules is not UNSET:
            field_dict["promotion_rules"] = promotion_rules
        if order_amount_promotion_rule is not UNSET:
            field_dict["order_amount_promotion_rule"] = order_amount_promotion_rule
        if sku_list_promotion_rule is not UNSET:
            field_dict["sku_list_promotion_rule"] = sku_list_promotion_rule
        if coupon_codes_promotion_rule is not UNSET:
            field_dict["coupon_codes_promotion_rule"] = coupon_codes_promotion_rule
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fixed_price_promotion_update_data_relationships_coupon_codes_promotion_rule import (
            FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule,
        )
        from ..models.fixed_price_promotion_update_data_relationships_market import (
            FixedPricePromotionUpdateDataRelationshipsMarket,
        )
        from ..models.fixed_price_promotion_update_data_relationships_order_amount_promotion_rule import (
            FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule,
        )
        from ..models.fixed_price_promotion_update_data_relationships_promotion_rules import (
            FixedPricePromotionUpdateDataRelationshipsPromotionRules,
        )
        from ..models.fixed_price_promotion_update_data_relationships_sku_list import (
            FixedPricePromotionUpdateDataRelationshipsSkuList,
        )
        from ..models.fixed_price_promotion_update_data_relationships_sku_list_promotion_rule import (
            FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, FixedPricePromotionUpdateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = FixedPricePromotionUpdateDataRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[Unset, FixedPricePromotionUpdateDataRelationshipsPromotionRules]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = FixedPricePromotionUpdateDataRelationshipsPromotionRules.from_dict(_promotion_rules)

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[Unset, FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = FixedPricePromotionUpdateDataRelationshipsOrderAmountPromotionRule.from_dict(
                _order_amount_promotion_rule
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[Unset, FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = FixedPricePromotionUpdateDataRelationshipsSkuListPromotionRule.from_dict(
                _sku_list_promotion_rule
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[Unset, FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = FixedPricePromotionUpdateDataRelationshipsCouponCodesPromotionRule.from_dict(
                _coupon_codes_promotion_rule
            )

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, FixedPricePromotionUpdateDataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = FixedPricePromotionUpdateDataRelationshipsSkuList.from_dict(_sku_list)

        fixed_price_promotion_update_data_relationships = cls(
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
            sku_list=sku_list,
        )

        fixed_price_promotion_update_data_relationships.additional_properties = d
        return fixed_price_promotion_update_data_relationships

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
