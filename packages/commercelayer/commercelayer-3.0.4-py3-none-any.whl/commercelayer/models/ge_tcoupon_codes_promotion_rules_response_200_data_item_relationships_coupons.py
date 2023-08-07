from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons_data import (
        GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData,
    )
    from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons_links import (
        GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks,
    )


T = TypeVar("T", bound="GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons")


@attr.s(auto_attribs=True)
class GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCoupons:
    """
    Attributes:
        links (Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks]):
        data (Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData]):
    """

    links: Union[Unset, "GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks"] = UNSET
    data: Union[Unset, "GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons_data import (
            GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData,
        )
        from ..models.ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons_links import (
            GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsData.from_dict(_data)

        ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons = cls(
            links=links,
            data=data,
        )

        ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons.additional_properties = d
        return ge_tcoupon_codes_promotion_rules_response_200_data_item_relationships_coupons

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
