from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule_data import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData,
    )
    from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule_links import (
        GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks,
    )


T = TypeVar("T", bound="GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule")


@attr.s(auto_attribs=True)
class GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRule:
    """
    Attributes:
        links (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks]):
        data (Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData]):
    """

    links: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks"
    ] = UNSET
    data: Union[
        Unset, "GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData"
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
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule_data import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData,
        )
        from ..models.ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule_links import (
            GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETpercentageDiscountPromotionsResponse200DataItemRelationshipsSkuListPromotionRuleData.from_dict(
                _data
            )

        ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule = cls(
            links=links,
            data=data,
        )

        ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule.additional_properties = (
            d
        )
        return ge_tpercentage_discount_promotions_response_200_data_item_relationships_sku_list_promotion_rule

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
