from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market_data import (
        PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData,
    )
    from ..models.patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market_links import (
        PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks,
    )


T = TypeVar(
    "T", bound="PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarket"
)


@attr.s(auto_attribs=True)
class PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarket:
    """
    Attributes:
        links (Union[Unset,
            PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks]):
        data (Union[Unset,
            PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData]):
    """

    links: Union[
        Unset, "PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks"
    ] = UNSET
    data: Union[
        Unset, "PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData"
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
        from ..models.patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market_data import (
            PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData,
        )
        from ..models.patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market_links import (
            PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsMarketData.from_dict(
                _data
            )

        patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market = (
            cls(
                links=links,
                data=data,
            )
        )

        patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market.additional_properties = (
            d
        )
        return (
            patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200_data_relationships_market
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
