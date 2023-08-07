from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.percentage_discount_promotion_update_data_relationships_coupon_codes_promotion_rule import (
        PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule,
    )
    from ..models.percentage_discount_promotion_update_data_relationships_market import (
        PercentageDiscountPromotionUpdateDataRelationshipsMarket,
    )
    from ..models.percentage_discount_promotion_update_data_relationships_order_amount_promotion_rule import (
        PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule,
    )
    from ..models.percentage_discount_promotion_update_data_relationships_promotion_rules import (
        PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules,
    )
    from ..models.percentage_discount_promotion_update_data_relationships_sku_list import (
        PercentageDiscountPromotionUpdateDataRelationshipsSkuList,
    )
    from ..models.percentage_discount_promotion_update_data_relationships_sku_list_promotion_rule import (
        PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule,
    )


T = TypeVar("T", bound="PercentageDiscountPromotionUpdateDataRelationships")


@attr.s(auto_attribs=True)
class PercentageDiscountPromotionUpdateDataRelationships:
    """
    Attributes:
        market (Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsMarket]):
        promotion_rules (Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset,
            PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset,
            PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule]):
        sku_list (Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsSkuList]):
    """

    market: Union[Unset, "PercentageDiscountPromotionUpdateDataRelationshipsMarket"] = UNSET
    promotion_rules: Union[Unset, "PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules"] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[
        Unset, "PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule"
    ] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    sku_list: Union[Unset, "PercentageDiscountPromotionUpdateDataRelationshipsSkuList"] = UNSET
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
        from ..models.percentage_discount_promotion_update_data_relationships_coupon_codes_promotion_rule import (
            PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule,
        )
        from ..models.percentage_discount_promotion_update_data_relationships_market import (
            PercentageDiscountPromotionUpdateDataRelationshipsMarket,
        )
        from ..models.percentage_discount_promotion_update_data_relationships_order_amount_promotion_rule import (
            PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule,
        )
        from ..models.percentage_discount_promotion_update_data_relationships_promotion_rules import (
            PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules,
        )
        from ..models.percentage_discount_promotion_update_data_relationships_sku_list import (
            PercentageDiscountPromotionUpdateDataRelationshipsSkuList,
        )
        from ..models.percentage_discount_promotion_update_data_relationships_sku_list_promotion_rule import (
            PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PercentageDiscountPromotionUpdateDataRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = PercentageDiscountPromotionUpdateDataRelationshipsPromotionRules.from_dict(
                _promotion_rules
            )

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[
            Unset, PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule
        ]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = (
                PercentageDiscountPromotionUpdateDataRelationshipsOrderAmountPromotionRule.from_dict(
                    _order_amount_promotion_rule
                )
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = PercentageDiscountPromotionUpdateDataRelationshipsSkuListPromotionRule.from_dict(
                _sku_list_promotion_rule
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[
            Unset, PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule
        ]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = (
                PercentageDiscountPromotionUpdateDataRelationshipsCouponCodesPromotionRule.from_dict(
                    _coupon_codes_promotion_rule
                )
            )

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, PercentageDiscountPromotionUpdateDataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = PercentageDiscountPromotionUpdateDataRelationshipsSkuList.from_dict(_sku_list)

        percentage_discount_promotion_update_data_relationships = cls(
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
            sku_list=sku_list,
        )

        percentage_discount_promotion_update_data_relationships.additional_properties = d
        return percentage_discount_promotion_update_data_relationships

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
