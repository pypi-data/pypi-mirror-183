from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons import (
        POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons,
    )
    from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_promotion import (
        POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion,
    )


T = TypeVar("T", bound="POSTcouponCodesPromotionRulesResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTcouponCodesPromotionRulesResponse201DataRelationships:
    """
    Attributes:
        promotion (Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion]):
        coupons (Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons]):
    """

    promotion: Union[Unset, "POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion"] = UNSET
    coupons: Union[Unset, "POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion, Unset):
            promotion = self.promotion.to_dict()

        coupons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coupons, Unset):
            coupons = self.coupons.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion is not UNSET:
            field_dict["promotion"] = promotion
        if coupons is not UNSET:
            field_dict["coupons"] = coupons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons import (
            POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons,
        )
        from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_promotion import (
            POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = POSTcouponCodesPromotionRulesResponse201DataRelationshipsPromotion.from_dict(_promotion)

        _coupons = d.pop("coupons", UNSET)
        coupons: Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons]
        if isinstance(_coupons, Unset):
            coupons = UNSET
        else:
            coupons = POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons.from_dict(_coupons)

        pos_tcoupon_codes_promotion_rules_response_201_data_relationships = cls(
            promotion=promotion,
            coupons=coupons,
        )

        pos_tcoupon_codes_promotion_rules_response_201_data_relationships.additional_properties = d
        return pos_tcoupon_codes_promotion_rules_response_201_data_relationships

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
