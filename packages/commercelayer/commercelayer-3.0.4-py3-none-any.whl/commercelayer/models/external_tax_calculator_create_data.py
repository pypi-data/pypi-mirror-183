from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.external_tax_calculator_create_data_type import ExternalTaxCalculatorCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_tax_calculator_create_data_attributes import ExternalTaxCalculatorCreateDataAttributes
    from ..models.external_tax_calculator_create_data_relationships import ExternalTaxCalculatorCreateDataRelationships


T = TypeVar("T", bound="ExternalTaxCalculatorCreateData")


@attr.s(auto_attribs=True)
class ExternalTaxCalculatorCreateData:
    """
    Attributes:
        type (ExternalTaxCalculatorCreateDataType): The resource's type
        attributes (ExternalTaxCalculatorCreateDataAttributes):
        relationships (Union[Unset, ExternalTaxCalculatorCreateDataRelationships]):
    """

    type: ExternalTaxCalculatorCreateDataType
    attributes: "ExternalTaxCalculatorCreateDataAttributes"
    relationships: Union[Unset, "ExternalTaxCalculatorCreateDataRelationships"] = UNSET
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
        from ..models.external_tax_calculator_create_data_attributes import ExternalTaxCalculatorCreateDataAttributes
        from ..models.external_tax_calculator_create_data_relationships import (
            ExternalTaxCalculatorCreateDataRelationships,
        )

        d = src_dict.copy()
        type = ExternalTaxCalculatorCreateDataType(d.pop("type"))

        attributes = ExternalTaxCalculatorCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, ExternalTaxCalculatorCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ExternalTaxCalculatorCreateDataRelationships.from_dict(_relationships)

        external_tax_calculator_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        external_tax_calculator_create_data.additional_properties = d
        return external_tax_calculator_create_data

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
