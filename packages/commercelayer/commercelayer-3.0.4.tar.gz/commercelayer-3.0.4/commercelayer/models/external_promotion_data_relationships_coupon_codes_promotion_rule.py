from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_promotion_data_relationships_coupon_codes_promotion_rule_data import (
        ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData,
    )


T = TypeVar("T", bound="ExternalPromotionDataRelationshipsCouponCodesPromotionRule")


@attr.s(auto_attribs=True)
class ExternalPromotionDataRelationshipsCouponCodesPromotionRule:
    """
    Attributes:
        data (Union[Unset, ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData]):
    """

    data: Union[Unset, "ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData"] = UNSET
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
        from ..models.external_promotion_data_relationships_coupon_codes_promotion_rule_data import (
            ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ExternalPromotionDataRelationshipsCouponCodesPromotionRuleData.from_dict(_data)

        external_promotion_data_relationships_coupon_codes_promotion_rule = cls(
            data=data,
        )

        external_promotion_data_relationships_coupon_codes_promotion_rule.additional_properties = d
        return external_promotion_data_relationships_coupon_codes_promotion_rule

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
