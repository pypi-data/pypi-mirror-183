from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons import (
        GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons,
    )
    from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_promotion import (
        GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion,
    )


T = TypeVar("T", bound="GETcouponCodesPromotionRulesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcouponCodesPromotionRulesResponse200DataItemRelationships:
    """
    Attributes:
        promotion (Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion]):
        coupons (Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons]):
    """

    promotion: Union[Unset, "GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion"] = UNSET
    coupons: Union[Unset, "GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons"] = UNSET
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
        from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons import (
            GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons,
        )
        from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_promotion import (
            GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = GETcouponCodesPromotionRulesResponse200DataItemRelationshipsPromotion.from_dict(_promotion)

        _coupons = d.pop("coupons", UNSET)
        coupons: Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons]
        if isinstance(_coupons, Unset):
            coupons = UNSET
        else:
            coupons = GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons.from_dict(_coupons)

        ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships = cls(
            promotion=promotion,
            coupons=coupons,
        )

        ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships.additional_properties = d
        return ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships

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
