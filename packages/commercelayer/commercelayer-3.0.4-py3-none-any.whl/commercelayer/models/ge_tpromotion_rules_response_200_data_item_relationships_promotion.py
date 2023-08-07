from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpromotion_rules_response_200_data_item_relationships_promotion_data import (
        GETpromotionRulesResponse200DataItemRelationshipsPromotionData,
    )
    from ..models.ge_tpromotion_rules_response_200_data_item_relationships_promotion_links import (
        GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks,
    )


T = TypeVar("T", bound="GETpromotionRulesResponse200DataItemRelationshipsPromotion")


@attr.s(auto_attribs=True)
class GETpromotionRulesResponse200DataItemRelationshipsPromotion:
    """
    Attributes:
        links (Union[Unset, GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks]):
        data (Union[Unset, GETpromotionRulesResponse200DataItemRelationshipsPromotionData]):
    """

    links: Union[Unset, "GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks"] = UNSET
    data: Union[Unset, "GETpromotionRulesResponse200DataItemRelationshipsPromotionData"] = UNSET
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
        from ..models.ge_tpromotion_rules_response_200_data_item_relationships_promotion_data import (
            GETpromotionRulesResponse200DataItemRelationshipsPromotionData,
        )
        from ..models.ge_tpromotion_rules_response_200_data_item_relationships_promotion_links import (
            GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETpromotionRulesResponse200DataItemRelationshipsPromotionLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETpromotionRulesResponse200DataItemRelationshipsPromotionData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETpromotionRulesResponse200DataItemRelationshipsPromotionData.from_dict(_data)

        ge_tpromotion_rules_response_200_data_item_relationships_promotion = cls(
            links=links,
            data=data,
        )

        ge_tpromotion_rules_response_200_data_item_relationships_promotion.additional_properties = d
        return ge_tpromotion_rules_response_200_data_item_relationships_promotion

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
