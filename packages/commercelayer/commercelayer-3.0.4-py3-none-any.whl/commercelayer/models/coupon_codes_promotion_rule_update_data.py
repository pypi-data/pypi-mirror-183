from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coupon_codes_promotion_rule_update_data_type import CouponCodesPromotionRuleUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coupon_codes_promotion_rule_update_data_attributes import CouponCodesPromotionRuleUpdateDataAttributes
    from ..models.coupon_codes_promotion_rule_update_data_relationships import (
        CouponCodesPromotionRuleUpdateDataRelationships,
    )


T = TypeVar("T", bound="CouponCodesPromotionRuleUpdateData")


@attr.s(auto_attribs=True)
class CouponCodesPromotionRuleUpdateData:
    """
    Attributes:
        type (CouponCodesPromotionRuleUpdateDataType): The resource's type
        id (str): The resource's id Example: XGZwpOSrWL.
        attributes (CouponCodesPromotionRuleUpdateDataAttributes):
        relationships (Union[Unset, CouponCodesPromotionRuleUpdateDataRelationships]):
    """

    type: CouponCodesPromotionRuleUpdateDataType
    id: str
    attributes: "CouponCodesPromotionRuleUpdateDataAttributes"
    relationships: Union[Unset, "CouponCodesPromotionRuleUpdateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coupon_codes_promotion_rule_update_data_attributes import (
            CouponCodesPromotionRuleUpdateDataAttributes,
        )
        from ..models.coupon_codes_promotion_rule_update_data_relationships import (
            CouponCodesPromotionRuleUpdateDataRelationships,
        )

        d = src_dict.copy()
        type = CouponCodesPromotionRuleUpdateDataType(d.pop("type"))

        id = d.pop("id")

        attributes = CouponCodesPromotionRuleUpdateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, CouponCodesPromotionRuleUpdateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = CouponCodesPromotionRuleUpdateDataRelationships.from_dict(_relationships)

        coupon_codes_promotion_rule_update_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        coupon_codes_promotion_rule_update_data.additional_properties = d
        return coupon_codes_promotion_rule_update_data

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
