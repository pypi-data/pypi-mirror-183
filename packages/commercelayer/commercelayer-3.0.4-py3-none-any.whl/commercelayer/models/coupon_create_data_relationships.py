from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.coupon_create_data_relationships_promotion_rule import CouponCreateDataRelationshipsPromotionRule


T = TypeVar("T", bound="CouponCreateDataRelationships")


@attr.s(auto_attribs=True)
class CouponCreateDataRelationships:
    """
    Attributes:
        promotion_rule (CouponCreateDataRelationshipsPromotionRule):
    """

    promotion_rule: "CouponCreateDataRelationshipsPromotionRule"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion_rule = self.promotion_rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "promotion_rule": promotion_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coupon_create_data_relationships_promotion_rule import CouponCreateDataRelationshipsPromotionRule

        d = src_dict.copy()
        promotion_rule = CouponCreateDataRelationshipsPromotionRule.from_dict(d.pop("promotion_rule"))

        coupon_create_data_relationships = cls(
            promotion_rule=promotion_rule,
        )

        coupon_create_data_relationships.additional_properties = d
        return coupon_create_data_relationships

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
