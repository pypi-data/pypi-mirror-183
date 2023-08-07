from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_amount_promotion_rules_response_200_data_item_relationships_promotion import (
        GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion,
    )


T = TypeVar("T", bound="GETorderAmountPromotionRulesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETorderAmountPromotionRulesResponse200DataItemRelationships:
    """
    Attributes:
        promotion (Union[Unset, GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion]):
    """

    promotion: Union[Unset, "GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion, Unset):
            promotion = self.promotion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion is not UNSET:
            field_dict["promotion"] = promotion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_torder_amount_promotion_rules_response_200_data_item_relationships_promotion import (
            GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[Unset, GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotion.from_dict(_promotion)

        ge_torder_amount_promotion_rules_response_200_data_item_relationships = cls(
            promotion=promotion,
        )

        ge_torder_amount_promotion_rules_response_200_data_item_relationships.additional_properties = d
        return ge_torder_amount_promotion_rules_response_200_data_item_relationships

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
