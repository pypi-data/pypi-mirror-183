from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_attachments import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_market import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_order_amount_promotion_rule import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_promotion_rules import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_sku_list import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_sku_list_promotion_rule import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule,
    )
    from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_skus import (
        PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus,
    )


T = TypeVar("T", bound="PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket]):
        promotion_rules (Union[Unset,
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules]):
        order_amount_promotion_rule (Union[Unset,
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule]):
        sku_list_promotion_rule (Union[Unset,
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule]):
        coupon_codes_promotion_rule (Union[Unset,
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule]):
        attachments (Union[Unset,
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments]):
        sku_list (Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList]):
        skus (Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus]):
    """

    market: Union[Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket"] = UNSET
    promotion_rules: Union[
        Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules"
    ] = UNSET
    order_amount_promotion_rule: Union[
        Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule"
    ] = UNSET
    sku_list_promotion_rule: Union[
        Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule"
    ] = UNSET
    coupon_codes_promotion_rule: Union[
        Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule"
    ] = UNSET
    attachments: Union[
        Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments"
    ] = UNSET
    sku_list: Union[Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus"] = UNSET
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
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_attachments import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_market import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_order_amount_promotion_rule import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_promotion_rules import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_sku_list import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_sku_list_promotion_rule import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule,
        )
        from ..models.patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships_skus import (
            PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsMarket.from_dict(_market)

        _promotion_rules = d.pop("promotion_rules", UNSET)
        promotion_rules: Union[
            Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules
        ]
        if isinstance(_promotion_rules, Unset):
            promotion_rules = UNSET
        else:
            promotion_rules = (
                PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsPromotionRules.from_dict(
                    _promotion_rules
                )
            )

        _order_amount_promotion_rule = d.pop("order_amount_promotion_rule", UNSET)
        order_amount_promotion_rule: Union[
            Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule
        ]
        if isinstance(_order_amount_promotion_rule, Unset):
            order_amount_promotion_rule = UNSET
        else:
            order_amount_promotion_rule = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsOrderAmountPromotionRule.from_dict(
                _order_amount_promotion_rule
            )

        _sku_list_promotion_rule = d.pop("sku_list_promotion_rule", UNSET)
        sku_list_promotion_rule: Union[
            Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule
        ]
        if isinstance(_sku_list_promotion_rule, Unset):
            sku_list_promotion_rule = UNSET
        else:
            sku_list_promotion_rule = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuListPromotionRule.from_dict(
                _sku_list_promotion_rule
            )

        _coupon_codes_promotion_rule = d.pop("coupon_codes_promotion_rule", UNSET)
        coupon_codes_promotion_rule: Union[
            Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule
        ]
        if isinstance(_coupon_codes_promotion_rule, Unset):
            coupon_codes_promotion_rule = UNSET
        else:
            coupon_codes_promotion_rule = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsCouponCodesPromotionRule.from_dict(
                _coupon_codes_promotion_rule
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsAttachments.from_dict(
                    _attachments
                )
            )

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkuList.from_dict(
                _sku_list
            )

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = PATCHfixedPricePromotionsfixedPricePromotionIdResponse200DataRelationshipsSkus.from_dict(_skus)

        patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships = cls(
            market=market,
            promotion_rules=promotion_rules,
            order_amount_promotion_rule=order_amount_promotion_rule,
            sku_list_promotion_rule=sku_list_promotion_rule,
            coupon_codes_promotion_rule=coupon_codes_promotion_rule,
            attachments=attachments,
            sku_list=sku_list,
            skus=skus,
        )

        patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships.additional_properties = d
        return patc_hfixed_price_promotionsfixed_price_promotion_id_response_200_data_relationships

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
