from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion_data import (
        PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData,
    )
    from ..models.patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion_links import (
        PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks,
    )


T = TypeVar("T", bound="PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion")


@attr.s(auto_attribs=True)
class PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotion:
    """
    Attributes:
        links (Union[Unset,
            PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks]):
        data (Union[Unset,
            PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData]):
    """

    links: Union[
        Unset, "PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks"
    ] = UNSET
    data: Union[
        Unset, "PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData"
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
        from ..models.patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion_data import (
            PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData,
        )
        from ..models.patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion_links import (
            PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionData.from_dict(
                _data
            )

        patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion = (
            cls(
                links=links,
                data=data,
            )
        )

        patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion.additional_properties = (
            d
        )
        return (
            patc_horder_amount_promotion_rulesorder_amount_promotion_rule_id_response_200_data_relationships_promotion
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
