from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_data import (
        GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData,
    )
    from ..models.ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_links import (
        GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks,
    )


T = TypeVar("T", bound="GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRule")


@attr.s(auto_attribs=True)
class GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRule:
    """
    Attributes:
        links (Union[Unset,
            GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks]):
        data (Union[Unset,
            GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData]):
    """

    links: Union[
        Unset, "GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks"
    ] = UNSET
    data: Union[
        Unset, "GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData"
    ] = UNSET
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
        from ..models.ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_data import (
            GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData,
        )
        from ..models.ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_links import (
            GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData.from_dict(
                _data
            )

        ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule = (
            cls(
                links=links,
                data=data,
            )
        )

        ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule.additional_properties = (
            d
        )
        return (
            ge_tfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule
        )

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
