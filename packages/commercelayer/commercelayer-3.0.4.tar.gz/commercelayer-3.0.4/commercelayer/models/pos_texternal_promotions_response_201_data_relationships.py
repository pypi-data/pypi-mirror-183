from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_texternal_promotions_response_201_data_relationships_attachments import (
        POSTexternalPromotionsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_texternal_promotions_response_201_data_relationships_coupon_codes_promotion_rule import (
        POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule,
    )
    from ..models.pos_texternal_promotions_response_201_data_relationships_market import (
        POSTexternalPromotionsResponse201DataRelationshipsMarket,
    )
    from ..models.pos_texternal_promotions_response_201_data_relationships_order_amount_promotion_rule import (
        POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule,
    )
    from ..models.pos_texternal_promotions_response_201_data_relationships_promotion_rules import (
        POSTexternalPromotionsResponse201DataRelationshipsPromotionRules,
    )
    from ..models.pos_texternal_promotions_response_201_data_relationships_sku_list_promotion_rule import (
        POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule,
    )


T = TypeVar("T", bound="POSTexternalPromotionsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTexternalPromotionsResponse201DataRelationships:
    """
    Attributes:
        market (Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsMarket]):
        promotion_rules (Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset,
            POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset,
            POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule]):
        attachments (Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsAttachments]):
    """

    market: Union[Unset, "POSTexternalPromotionsResponse201DataRelationshipsMarket"] = UNSET
    promotion_rules: Union[Unset, "POSTexternalPromotionsResponse201DataRelationshipsPromotionRules"] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[
        Unset, "POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule"
    ] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    attachments: Union[Unset, "POSTexternalPromotionsResponse201DataRelationshipsAttachments"] = UNSET
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

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

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
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_texternal_promotions_response_201_data_relationships_attachments import (
            POSTexternalPromotionsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_texternal_promotions_response_201_data_relationships_coupon_codes_promotion_rule import (
            POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule,
        )
        from ..models.pos_texternal_promotions_response_201_data_relationships_market import (
            POSTexternalPromotionsResponse201DataRelationshipsMarket,
        )
        from ..models.pos_texternal_promotions_response_201_data_relationships_order_amount_promotion_rule import (
            POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule,
        )
        from ..models.pos_texternal_promotions_response_201_data_relationships_promotion_rules import (
            POSTexternalPromotionsResponse201DataRelationshipsPromotionRules,
        )
        from ..models.pos_texternal_promotions_response_201_data_relationships_sku_list_promotion_rule import (
            POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = POSTexternalPromotionsResponse201DataRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsPromotionRules]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = POSTexternalPromotionsResponse201DataRelationshipsPromotionRules.from_dict(
                _promotion_rules
            )

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[
            Unset, POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule
        ]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = (
                POSTexternalPromotionsResponse201DataRelationshipsOrderAmountPromotionRule.from_dict(
                    _order_amount_promotion_rule
                )
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = POSTexternalPromotionsResponse201DataRelationshipsSkuListPromotionRule.from_dict(
                _sku_list_promotion_rule
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[
            Unset, POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule
        ]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = (
                POSTexternalPromotionsResponse201DataRelationshipsCouponCodesPromotionRule.from_dict(
                    _coupon_codes_promotion_rule
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTexternalPromotionsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTexternalPromotionsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_texternal_promotions_response_201_data_relationships = cls(
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
            attachments=attachments,
        )

        pos_texternal_promotions_response_201_data_relationships.additional_properties = d
        return pos_texternal_promotions_response_201_data_relationships

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
