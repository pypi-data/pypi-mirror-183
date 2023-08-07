from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.billing_info_validation_rule_create_data_type import BillingInfoValidationRuleCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_info_validation_rule_create_data_attributes import (
        BillingInfoValidationRuleCreateDataAttributes,
    )
    from ..models.billing_info_validation_rule_create_data_relationships import (
        BillingInfoValidationRuleCreateDataRelationships,
    )


T = TypeVar("T", bound="BillingInfoValidationRuleCreateData")


@attr.s(auto_attribs=True)
class BillingInfoValidationRuleCreateData:
    """
    Attributes:
        type (BillingInfoValidationRuleCreateDataType): The resource's type
        attributes (BillingInfoValidationRuleCreateDataAttributes):
        relationships (Union[Unset, BillingInfoValidationRuleCreateDataRelationships]):
    """

    type: BillingInfoValidationRuleCreateDataType
    attributes: "BillingInfoValidationRuleCreateDataAttributes"
    relationships: Union[Unset, "BillingInfoValidationRuleCreateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_info_validation_rule_create_data_attributes import (
            BillingInfoValidationRuleCreateDataAttributes,
        )
        from ..models.billing_info_validation_rule_create_data_relationships import (
            BillingInfoValidationRuleCreateDataRelationships,
        )

        d = src_dict.copy()
        type = BillingInfoValidationRuleCreateDataType(d.pop("type"))

        attributes = BillingInfoValidationRuleCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, BillingInfoValidationRuleCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = BillingInfoValidationRuleCreateDataRelationships.from_dict(_relationships)

        billing_info_validation_rule_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        billing_info_validation_rule_create_data.additional_properties = d
        return billing_info_validation_rule_create_data

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
