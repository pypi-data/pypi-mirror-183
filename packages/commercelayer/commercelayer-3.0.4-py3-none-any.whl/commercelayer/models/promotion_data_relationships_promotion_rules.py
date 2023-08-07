from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.promotion_data_relationships_promotion_rules_data import PromotionDataRelationshipsPromotionRulesData


T = TypeVar("T", bound="PromotionDataRelationshipsPromotionRules")


@attr.s(auto_attribs=True)
class PromotionDataRelationshipsPromotionRules:
    """
    Attributes:
        data (Union[Unset, PromotionDataRelationshipsPromotionRulesData]):
    """

    data: Union[Unset, "PromotionDataRelationshipsPromotionRulesData"] = UNSET
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
        from ..models.promotion_data_relationships_promotion_rules_data import (
            PromotionDataRelationshipsPromotionRulesData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PromotionDataRelationshipsPromotionRulesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PromotionDataRelationshipsPromotionRulesData.from_dict(_data)

        promotion_data_relationships_promotion_rules = cls(
            data=data,
        )

        promotion_data_relationships_promotion_rules.additional_properties = d
        return promotion_data_relationships_promotion_rules

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
