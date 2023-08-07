from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_attachments import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_coupon_codes_promotion_rule import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_market import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_order_amount_promotion_rule import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_promotion_rules import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_skus import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus,
    )


T = TypeVar("T", bound="GETpercentageDiscountPromotionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpercentageDiscountPromotionsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket]):
        promotion_rules (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset,
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset,
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset,
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule]):
        attachments (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments]):
        sku_list (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList]):
        skus (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus]):
    """

    market: Union[Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket"] = UNSET
    promotion_rules: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules"
    ] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule"
    ] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    attachments: Union[Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments"] = UNSET
    sku_list: Union[Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus"] = UNSET
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

        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skus, Unset):
            skus = self.skus.to_dict()

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
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_attachments import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_coupon_codes_promotion_rule import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_market import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_order_amount_promotion_rule import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_promotion_rules import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_skus import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsPromotionRules.from_dict(
                _promotion_rules
            )

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[
            Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule
        ]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = (
                GETpercentageDiscountPromotionsResponse200DataItemRelationshipsOrderAmountPromotionRule.from_dict(
                    _order_amount_promotion_rule
                )
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[
            Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule
        ]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = (
                GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule.from_dict(
                    _sku_list_promotion_rule
                )
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[
            Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule
        ]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = (
                GETpercentageDiscountPromotionsResponse200DataItemRelationshipsCouponCodesPromotionRule.from_dict(
                    _coupon_codes_promotion_rule
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsAttachments.from_dict(
                _attachments
            )

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkus.from_dict(_skus)

        ge_tpercentage_discount_promotions_response_200_data_item_relationships = cls(
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
            attachments=attachments,
            sku_list=sku_list,
            skus=skus,
        )

        ge_tpercentage_discount_promotions_response_200_data_item_relationships.additional_properties = d
        return ge_tpercentage_discount_promotions_response_200_data_item_relationships

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
