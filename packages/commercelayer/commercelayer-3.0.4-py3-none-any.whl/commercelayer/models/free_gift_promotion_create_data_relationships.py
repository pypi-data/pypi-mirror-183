from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule import (
        FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule,
    )
    from ..models.free_gift_promotion_create_data_relationships_market import (
        FreeGiftPromotionCreateDataRelationshipsMarket,
    )
    from ..models.free_gift_promotion_create_data_relationships_order_amount_promotion_rule import (
        FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule,
    )
    from ..models.free_gift_promotion_create_data_relationships_promotion_rules import (
        FreeGiftPromotionCreateDataRelationshipsPromotionRules,
    )
    from ..models.free_gift_promotion_create_data_relationships_sku_list import (
        FreeGiftPromotionCreateDataRelationshipsSkuList,
    )
    from ..models.free_gift_promotion_create_data_relationships_sku_list_promotion_rule import (
        FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule,
    )


T = TypeVar("T", bound="FreeGiftPromotionCreateDataRelationships")


@attr.s(auto_attribs=True)
class FreeGiftPromotionCreateDataRelationships:
    """
    Attributes:
        sku_list (FreeGiftPromotionCreateDataRelationshipsSkuList):
        market (Union[Unset, FreeGiftPromotionCreateDataRelationshipsMarket]):
        promotion_rules (Union[Unset, FreeGiftPromotionCreateDataRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset, FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset, FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset, FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule]):
    """

    sku_list: "FreeGiftPromotionCreateDataRelationshipsSkuList"
    market: Union[Unset, "FreeGiftPromotionCreateDataRelationshipsMarket"] = UNSET
    promotion_rules: Union[Unset, "FreeGiftPromotionCreateDataRelationshipsPromotionRules"] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[Unset, "FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule"] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_list = self.sku_list.to_dict()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku_list": sku_list,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule import (
            FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule,
        )
        from ..models.free_gift_promotion_create_data_relationships_market import (
            FreeGiftPromotionCreateDataRelationshipsMarket,
        )
        from ..models.free_gift_promotion_create_data_relationships_order_amount_promotion_rule import (
            FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule,
        )
        from ..models.free_gift_promotion_create_data_relationships_promotion_rules import (
            FreeGiftPromotionCreateDataRelationshipsPromotionRules,
        )
        from ..models.free_gift_promotion_create_data_relationships_sku_list import (
            FreeGiftPromotionCreateDataRelationshipsSkuList,
        )
        from ..models.free_gift_promotion_create_data_relationships_sku_list_promotion_rule import (
            FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule,
        )

        d = src_dict.copy()
        sku_list = FreeGiftPromotionCreateDataRelationshipsSkuList.from_dict(d.pop("sku_list"))

        _market = d.pop("market", UNSET)
        market: Union[Unset, FreeGiftPromotionCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = FreeGiftPromotionCreateDataRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[Unset, FreeGiftPromotionCreateDataRelationshipsPromotionRules]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = FreeGiftPromotionCreateDataRelationshipsPromotionRules.from_dict(_promotion_rules)

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[Unset, FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = FreeGiftPromotionCreateDataRelationshipsOrderAmountPromotionRule.from_dict(
                _order_amount_promotion_rule
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[Unset, FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = FreeGiftPromotionCreateDataRelationshipsSkuListPromotionRule.from_dict(
                _sku_list_promotion_rule
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[Unset, FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule.from_dict(
                _coupon_codes_promotion_rule
            )

        free_gift_promotion_create_data_relationships = cls(
            sku_list=sku_list,
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
        )

        free_gift_promotion_create_data_relationships.additional_properties = d
        return free_gift_promotion_create_data_relationships

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
