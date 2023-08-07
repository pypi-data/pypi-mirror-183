from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_promotion import ExternalPromotion
    from ..models.fixed_amount_promotion import FixedAmountPromotion
    from ..models.fixed_price_promotion import FixedPricePromotion
    from ..models.free_gift_promotion import FreeGiftPromotion
    from ..models.free_shipping_promotion import FreeShippingPromotion
    from ..models.percentage_discount_promotion import PercentageDiscountPromotion
    from ..models.sku_list_promotion_rule_create_data_relationships_sku_list import (
        SkuListPromotionRuleCreateDataRelationshipsSkuList,
    )


T = TypeVar("T", bound="SkuListPromotionRuleCreateDataRelationships")


@attr.s(auto_attribs=True)
class SkuListPromotionRuleCreateDataRelationships:
    """
    Attributes:
        promotion (Union['ExternalPromotion', 'FixedAmountPromotion', 'FixedPricePromotion', 'FreeGiftPromotion',
            'FreeShippingPromotion', 'PercentageDiscountPromotion']):
        sku_list (Union[Unset, SkuListPromotionRuleCreateDataRelationshipsSkuList]):
    """

    promotion: Union[
        "ExternalPromotion",
        "FixedAmountPromotion",
        "FixedPricePromotion",
        "FreeGiftPromotion",
        "FreeShippingPromotion",
        "PercentageDiscountPromotion",
    ]
    sku_list: Union[Unset, "SkuListPromotionRuleCreateDataRelationshipsSkuList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.fixed_price_promotion import FixedPricePromotion
        from ..models.free_gift_promotion import FreeGiftPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion

        promotion: Dict[str, Any]

        if isinstance(self.promotion, PercentageDiscountPromotion):
            promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FreeShippingPromotion):
            promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FixedAmountPromotion):
            promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FreeGiftPromotion):
            promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FixedPricePromotion):
            promotion = self.promotion.to_dict()

        else:
            promotion = self.promotion.to_dict()

        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "promotion": promotion,
            }
        )
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_promotion import ExternalPromotion
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.fixed_price_promotion import FixedPricePromotion
        from ..models.free_gift_promotion import FreeGiftPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion
        from ..models.sku_list_promotion_rule_create_data_relationships_sku_list import (
            SkuListPromotionRuleCreateDataRelationshipsSkuList,
        )

        d = src_dict.copy()

        def _parse_promotion(
            data: object,
        ) -> Union[
            "ExternalPromotion",
            "FixedAmountPromotion",
            "FixedPricePromotion",
            "FreeGiftPromotion",
            "FreeShippingPromotion",
            "PercentageDiscountPromotion",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                promotion_type_0 = PercentageDiscountPromotion.from_dict(data)

                return promotion_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                promotion_type_1 = FreeShippingPromotion.from_dict(data)

                return promotion_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                promotion_type_2 = FixedAmountPromotion.from_dict(data)

                return promotion_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                promotion_type_3 = FreeGiftPromotion.from_dict(data)

                return promotion_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                promotion_type_4 = FixedPricePromotion.from_dict(data)

                return promotion_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            promotion_type_5 = ExternalPromotion.from_dict(data)

            return promotion_type_5

        promotion = _parse_promotion(d.pop("promotion"))

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, SkuListPromotionRuleCreateDataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = SkuListPromotionRuleCreateDataRelationshipsSkuList.from_dict(_sku_list)

        sku_list_promotion_rule_create_data_relationships = cls(
            promotion=promotion,
            sku_list=sku_list,
        )

        sku_list_promotion_rule_create_data_relationships.additional_properties = d
        return sku_list_promotion_rule_create_data_relationships

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
