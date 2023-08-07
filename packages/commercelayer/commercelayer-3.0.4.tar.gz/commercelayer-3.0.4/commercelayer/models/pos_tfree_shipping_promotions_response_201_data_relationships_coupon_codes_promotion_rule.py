from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule_data import (
        POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData,
    )
    from ..models.pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule_links import (
        POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks,
    )


T = TypeVar("T", bound="POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRule")


@attr.s(auto_attribs=True)
class POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRule:
    """
    Attributes:
        links (Union[Unset, POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks]):
        data (Union[Unset, POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData]):
    """

    links: Union[Unset, "POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks"] = UNSET
    data: Union[Unset, "POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData"] = UNSET
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
        from ..models.pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule_data import (
            POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData,
        )
        from ..models.pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule_links import (
            POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTfreeShippingPromotionsResponse201DataRelationshipsCouponCodesPromotionRuleData.from_dict(_data)

        pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule = cls(
            links=links,
            data=data,
        )

        pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule.additional_properties = (
            d
        )
        return pos_tfree_shipping_promotions_response_201_data_relationships_coupon_codes_promotion_rule

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
