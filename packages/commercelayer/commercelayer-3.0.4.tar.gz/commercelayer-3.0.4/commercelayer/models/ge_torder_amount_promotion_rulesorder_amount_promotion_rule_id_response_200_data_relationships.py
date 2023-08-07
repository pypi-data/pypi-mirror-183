from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion import (
        GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion,
    )


T = TypeVar("T", bound="GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationships:
    """
    Attributes:
        promotion (Union[Unset,
            GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion]):
    """

    promotion: Union[
        Unset, "GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion"
    ] = UNSET
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
        from ..models.ge_torder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion import (
            GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[
            Unset, GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion
        ]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = (
                GETorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion.from_dict(
                    _promotion
                )
            )

        ge_torder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships = cls(
            promotion=promotion,
        )

        ge_torder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships.additional_properties = (
            d
        )
        return ge_torder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships

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
