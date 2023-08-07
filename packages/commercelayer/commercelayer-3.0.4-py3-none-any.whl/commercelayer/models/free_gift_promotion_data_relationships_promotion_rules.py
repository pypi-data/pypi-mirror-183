from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_gift_promotion_data_relationships_promotion_rules_data import (
        FreeGiftPromotionDataRelationshipsPromotionRulesData,
    )


T = TypeVar("T", bound="FreeGiftPromotionDataRelationshipsPromotionRules")


@attr.s(auto_attribs=True)
class FreeGiftPromotionDataRelationshipsPromotionRules:
    """
    Attributes:
        data (Union[Unset, FreeGiftPromotionDataRelationshipsPromotionRulesData]):
    """

    data: Union[Unset, "FreeGiftPromotionDataRelationshipsPromotionRulesData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.free_gift_promotion_data_relationships_promotion_rules_data import (
            FreeGiftPromotionDataRelationshipsPromotionRulesData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, FreeGiftPromotionDataRelationshipsPromotionRulesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = FreeGiftPromotionDataRelationshipsPromotionRulesData.from_dict(_data)

        free_gift_promotion_data_relationships_promotion_rules = cls(
            data=data,
        )

        free_gift_promotion_data_relationships_promotion_rules.additional_properties = d
        return free_gift_promotion_data_relationships_promotion_rules

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
