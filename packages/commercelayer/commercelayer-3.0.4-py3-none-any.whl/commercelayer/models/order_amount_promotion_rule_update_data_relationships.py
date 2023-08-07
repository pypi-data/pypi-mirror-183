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


T = TypeVar("T", bound="OrderAmountPromotionRuleUpdateDataRelationships")


@attr.s(auto_attribs=True)
class OrderAmountPromotionRuleUpdateDataRelationships:
    """
    Attributes:
        promotion (Union['ExternalPromotion', 'FixedAmountPromotion', 'FixedPricePromotion', 'FreeGiftPromotion',
            'FreeShippingPromotion', 'PercentageDiscountPromotion', Unset]):
    """

    promotion: Union[
        "ExternalPromotion",
        "FixedAmountPromotion",
        "FixedPricePromotion",
        "FreeGiftPromotion",
        "FreeShippingPromotion",
        "PercentageDiscountPromotion",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.fixed_amount_promotion import FixedAmountPromotion
        from ..models.fixed_price_promotion import FixedPricePromotion
        from ..models.free_gift_promotion import FreeGiftPromotion
        from ..models.free_shipping_promotion import FreeShippingPromotion
        from ..models.percentage_discount_promotion import PercentageDiscountPromotion

        promotion: Union[Dict[str, Any], Unset]
        if isinstance(self.promotion, Unset):
            promotion = UNSET

        elif isinstance(self.promotion, PercentageDiscountPromotion):
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FreeShippingPromotion):
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FixedAmountPromotion):
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FreeGiftPromotion):
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        elif isinstance(self.promotion, FixedPricePromotion):
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        else:
            promotion = UNSET
            if not isinstance(self.promotion, Unset):
                promotion = self.promotion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion is not UNSET:
            field_dict["promotion"] = promotion

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
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _promotion_type_0 = data
                promotion_type_0: Union[Unset, PercentageDiscountPromotion]
                if isinstance(_promotion_type_0, Unset):
                    promotion_type_0 = UNSET
                else:
                    promotion_type_0 = PercentageDiscountPromotion.from_dict(_promotion_type_0)

                return promotion_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _promotion_type_1 = data
                promotion_type_1: Union[Unset, FreeShippingPromotion]
                if isinstance(_promotion_type_1, Unset):
                    promotion_type_1 = UNSET
                else:
                    promotion_type_1 = FreeShippingPromotion.from_dict(_promotion_type_1)

                return promotion_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _promotion_type_2 = data
                promotion_type_2: Union[Unset, FixedAmountPromotion]
                if isinstance(_promotion_type_2, Unset):
                    promotion_type_2 = UNSET
                else:
                    promotion_type_2 = FixedAmountPromotion.from_dict(_promotion_type_2)

                return promotion_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _promotion_type_3 = data
                promotion_type_3: Union[Unset, FreeGiftPromotion]
                if isinstance(_promotion_type_3, Unset):
                    promotion_type_3 = UNSET
                else:
                    promotion_type_3 = FreeGiftPromotion.from_dict(_promotion_type_3)

                return promotion_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _promotion_type_4 = data
                promotion_type_4: Union[Unset, FixedPricePromotion]
                if isinstance(_promotion_type_4, Unset):
                    promotion_type_4 = UNSET
                else:
                    promotion_type_4 = FixedPricePromotion.from_dict(_promotion_type_4)

                return promotion_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _promotion_type_5 = data
            promotion_type_5: Union[Unset, ExternalPromotion]
            if isinstance(_promotion_type_5, Unset):
                promotion_type_5 = UNSET
            else:
                promotion_type_5 = ExternalPromotion.from_dict(_promotion_type_5)

            return promotion_type_5

        promotion = _parse_promotion(d.pop("promotion", UNSET))

        order_amount_promotion_rule_update_data_relationships = cls(
            promotion=promotion,
        )

        order_amount_promotion_rule_update_data_relationships.additional_properties = d
        return order_amount_promotion_rule_update_data_relationships

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
