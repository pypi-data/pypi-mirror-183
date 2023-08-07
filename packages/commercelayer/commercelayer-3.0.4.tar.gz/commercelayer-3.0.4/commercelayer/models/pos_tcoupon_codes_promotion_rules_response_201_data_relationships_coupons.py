from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons_data import (
        POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData,
    )
    from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons_links import (
        POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks,
    )


T = TypeVar("T", bound="POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons")


@attr.s(auto_attribs=True)
class POSTcouponCodesPromotionRulesResponse201DataRelationshipsCoupons:
    """
    Attributes:
        links (Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks]):
        data (Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData]):
    """

    links: Union[Unset, "POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks"] = UNSET
    data: Union[Unset, "POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData"] = UNSET
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
        from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons_data import (
            POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData,
        )
        from ..models.pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons_links import (
            POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsData.from_dict(_data)

        pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons = cls(
            links=links,
            data=data,
        )

        pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons.additional_properties = d
        return pos_tcoupon_codes_promotion_rules_response_201_data_relationships_coupons

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
