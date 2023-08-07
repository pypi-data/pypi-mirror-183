from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_data import (
        PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData,
    )
    from ..models.patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_links import (
        PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks,
    )


T = TypeVar("T", bound="PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRule")


@attr.s(auto_attribs=True)
class PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRule:
    """
    Attributes:
        links (Union[Unset,
            PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks]):
        data (Union[Unset,
            PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData]):
    """

    links: Union[
        Unset, "PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks"
    ] = UNSET
    data: Union[
        Unset, "PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData"
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
        from ..models.patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_data import (
            PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData,
        )
        from ..models.patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule_links import (
            PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHexternalPromotionsexternalPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleData.from_dict(
                _data
            )

        patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule = (
            cls(
                links=links,
                data=data,
            )
        )

        patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule.additional_properties = (
            d
        )
        return (
            patc_hexternal_promotionsexternal_promotion_id_response_200_data_relationships_coupon_codes_promotion_rule
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
