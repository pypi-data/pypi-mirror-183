from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list_data import (
        PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData,
    )
    from ..models.patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list_links import (
        PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks,
    )


T = TypeVar("T", bound="PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuList")


@attr.s(auto_attribs=True)
class PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuList:
    """
    Attributes:
        links (Union[Unset, PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks]):
        data (Union[Unset, PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData]):
    """

    links: Union[Unset, "PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks"] = UNSET
    data: Union[Unset, "PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData"] = UNSET
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
        from ..models.patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list_data import (
            PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData,
        )
        from ..models.patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list_links import (
            PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsSkuListData.from_dict(_data)

        patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list = cls(
            links=links,
            data=data,
        )

        patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list.additional_properties = (
            d
        )
        return patc_hfree_gift_promotionsfree_gift_promotion_id_response_200_data_relationships_sku_list

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
