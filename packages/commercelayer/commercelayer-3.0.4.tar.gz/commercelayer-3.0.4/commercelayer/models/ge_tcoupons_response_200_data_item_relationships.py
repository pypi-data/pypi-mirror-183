from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcoupons_response_200_data_item_relationships_promotion_rule import (
        GETcouponsResponse200DataItemRelationshipsPromotionRule,
    )


T = TypeVar("T", bound="GETcouponsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcouponsResponse200DataItemRelationships:
    """
    Attributes:
        promotion_rule (Union[Unset, GETcouponsResponse200DataItemRelationshipsPromotionRule]):
    """

    promotion_rule: Union[Unset, "GETcouponsResponse200DataItemRelationshipsPromotionRule"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_rule, Unset):
            promotion_rule = self.promotion_rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion_rule is not UNSET:
            field_dict["promotion_rule"] = promotion_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcoupons_response_200_data_item_relationships_promotion_rule import (
            GETcouponsResponse200DataItemRelationshipsPromotionRule,
        )

        d = src_dict.copy()
        _promotion_rule = d.pop("promotion_rule", UNSET)
        promotion_rule: Union[Unset, GETcouponsResponse200DataItemRelationshipsPromotionRule]
        if isinstance(_promotion_rule, Unset):
            promotion_rule = UNSET
        else:
            promotion_rule = GETcouponsResponse200DataItemRelationshipsPromotionRule.from_dict(_promotion_rule)

        ge_tcoupons_response_200_data_item_relationships = cls(
            promotion_rule=promotion_rule,
        )

        ge_tcoupons_response_200_data_item_relationships.additional_properties = d
        return ge_tcoupons_response_200_data_item_relationships

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
