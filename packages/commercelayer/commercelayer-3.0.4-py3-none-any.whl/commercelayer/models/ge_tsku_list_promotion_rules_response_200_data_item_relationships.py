from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_promotion import (
        GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion,
    )
    from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_sku_list import (
        GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList,
    )
    from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_skus import (
        GETskuListPromotionRulesResponse200DataItemRelationshipsSkus,
    )


T = TypeVar("T", bound="GETskuListPromotionRulesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETskuListPromotionRulesResponse200DataItemRelationships:
    """
    Attributes:
        promotion (Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion]):
        sku_list (Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList]):
        skus (Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsSkus]):
    """

    promotion: Union[Unset, "GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion"] = UNSET
    sku_list: Union[Unset, "GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList"] = UNSET
    skus: Union[Unset, "GETskuListPromotionRulesResponse200DataItemRelationshipsSkus"] = UNSET
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
        from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_promotion import (
            GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion,
        )
        from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_sku_list import (
            GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList,
        )
        from ..models.ge_tsku_list_promotion_rules_response_200_data_item_relationships_skus import (
            GETskuListPromotionRulesResponse200DataItemRelationshipsSkus,
        )

        d = src_dict.copy()
        _promotion = d.pop("promotion", UNSET)
        promotion: Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion]
        if isinstance(_promotion, Unset):
            promotion = UNSET
        else:
            promotion = GETskuListPromotionRulesResponse200DataItemRelationshipsPromotion.from_dict(_promotion)

        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = GETskuListPromotionRulesResponse200DataItemRelationshipsSkuList.from_dict(_sku_list)

        _skus = d.pop("skus", UNSET)
        skus: Union[Unset, GETskuListPromotionRulesResponse200DataItemRelationshipsSkus]
        if isinstance(_skus, Unset):
            skus = UNSET
        else:
            skus = GETskuListPromotionRulesResponse200DataItemRelationshipsSkus.from_dict(_skus)

        ge_tsku_list_promotion_rules_response_200_data_item_relationships = cls(
            promotion=promotion,
            sku_list=sku_list,
            skus=skus,
        )

        ge_tsku_list_promotion_rules_response_200_data_item_relationships.additional_properties = d
        return ge_tsku_list_promotion_rules_response_200_data_item_relationships

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
