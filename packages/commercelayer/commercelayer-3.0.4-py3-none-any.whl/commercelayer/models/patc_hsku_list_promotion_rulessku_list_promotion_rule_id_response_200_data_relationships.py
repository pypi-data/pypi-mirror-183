from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_promotion import (
        PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion,
    )
    from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_sku_list import (
        PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList,
    )
    from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_skus import (
        PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus,
    )


T = TypeVar("T", bound="PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationships:
    """
    Attributes:
        promotion (Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion]):
        sku_list (Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList]):
        skus (Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus]):
    """

    promotion: Union[
        Unset, "PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion"
    ] = UNSET
    sku_list: Union[
        Unset, "PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList"
    ] = UNSET
    skus: Union[Unset, "PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promotion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion, Unset):
            promotion = self.promotion.to_dict()

        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skus, Unset):
            skus = self.skus.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promotion is not UNSET:
            field_dict["promotion"] = promotion
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_promotion import (
            PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion,
        )
        from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_sku_list import (
            PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList,
        )
        from ..models.patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships_skus import (
            PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsPromotion.from_dict(
                _promotion
            )

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkuList.from_dict(
                _sku_list
            )

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = PATCHskuListPromotionRulesskuListPromotionRuleIdResponse200DataRelationshipsSkus.from_dict(_skus)

        patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships = cls(
            promotion=promotion,
            sku_list=sku_list,
            skus=skus,
        )

        patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships.additional_properties = (
            d
        )
        return patc_hsku_list_promotion_rulessku_list_promotion_rule_id_response_200_data_relationships

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
