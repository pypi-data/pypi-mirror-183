from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.external_promotion import ExternalPromotion
    from ..models.fixed_amount_promotion import FixedAmountPromotion
    from ..models.fixed_price_promotion import FixedPricePromotion
    from ..models.free_gift_promotion import FreeGiftPromotion
    from ..models.free_shipping_promotion import FreeShippingPromotion
    from ..models.percentage_discount_promotion import PercentageDiscountPromotion


T = TypeVar("T", bound="OrderAmountPromotionRuleCreateDataRelationships")


@attr.s(auto_attribs=True)
class OrderAmountPromotionRuleCreateDataRelationships:
    """
    Attributes:
        promotion (Union['ExternalPromotion', 'FixedAmountPromotion', 'FixedPricePromotion', 'FreeGiftPromotion',
            'FreeShippingPromotion', 'PercentageDiscountPromotion']):
    """

    promotion: Union[
        "ExternalPromotion",
        "FixedAmountPromotion",
        "FixedPricePromotion",
        "FreeGiftPromotion",
        "FreeShippingPromotion",
        "PercentageDiscountPromotion",
    ]
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "promotion": promotion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_promotion import ExternalPromotion
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.fixed_price_promotion import FixedPricePromotion
        from ..models.free_gift_promotion import FreeGiftPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion

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

        order_amount_promotion_rule_create_data_relationships = cls(
            promotion=promotion,
        )

        order_amount_promotion_rule_create_data_relationships.additional_properties = d
        return order_amount_promotion_rule_create_data_relationships

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
