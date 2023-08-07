from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule_data import (
        GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData,
    )
    from ..models.ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule_links import (
        GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks,
    )


T = TypeVar("T", bound="GETcouponscouponIdResponse200DataRelationshipsPromotionRule")


@attr.s(auto_attribs=True)
class GETcouponscouponIdResponse200DataRelationshipsPromotionRule:
    """
    Attributes:
        links (Union[Unset, GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks]):
        data (Union[Unset, GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData]):
    """

    links: Union[Unset, "GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks"] = UNSET
    data: Union[Unset, "GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData"] = UNSET
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
        from ..models.ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule_data import (
            GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData,
        )
        from ..models.ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule_links import (
            GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETcouponscouponIdResponse200DataRelationshipsPromotionRuleLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETcouponscouponIdResponse200DataRelationshipsPromotionRuleData.from_dict(_data)

        ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule = cls(
            links=links,
            data=data,
        )

        ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule.additional_properties = d
        return ge_tcouponscoupon_id_response_200_data_relationships_promotion_rule

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
