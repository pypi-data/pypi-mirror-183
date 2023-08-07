from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule_data import (
        FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRuleData,
    )


T = TypeVar("T", bound="FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule")


@attr.s(auto_attribs=True)
class FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRule:
    """
    Attributes:
        data (FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRuleData):
    """

    data: "FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRuleData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule_data import (
            FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRuleData,
        )

        d = src_dict.copy()
        data = FreeGiftPromotionCreateDataRelationshipsCouponCodesPromotionRuleData.from_dict(d.pop("data"))

        free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule = cls(
            data=data,
        )

        free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule.additional_properties = d
        return free_gift_promotion_create_data_relationships_coupon_codes_promotion_rule

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
