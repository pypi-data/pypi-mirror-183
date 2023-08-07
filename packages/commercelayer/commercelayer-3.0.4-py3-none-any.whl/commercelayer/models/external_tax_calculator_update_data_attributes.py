from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_tax_calculator_update_data_attributes_metadata import (
        ExternalTaxCalculatorUpdateDataAttributesMetadata,
    )


T = TypeVar("T", bound="ExternalTaxCalculatorUpdateDataAttributes")


@attr.s(auto_attribs=True)
class ExternalTaxCalculatorUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The tax calculator's internal name. Example: Personal tax calculator.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ExternalTaxCalculatorUpdateDataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
        tax_calculator_url (Union[Unset, str]): The URL to the service that will compute the taxes. Example:
            https://external_calculator.yourbrand.com.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ExternalTaxCalculatorUpdateDataAttributesMetadata"] = UNSET
    tax_calculator_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        tax_calculator_url = self.tax_calculator_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tax_calculator_url is not UNSET:
            field_dict["tax_calculator_url"] = tax_calculator_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_tax_calculator_update_data_attributes_metadata import (
            ExternalTaxCalculatorUpdateDataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ExternalTaxCalculatorUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExternalTaxCalculatorUpdateDataAttributesMetadata.from_dict(_metadata)

        tax_calculator_url = d.pop("tax_calculator_url", UNSET)

        external_tax_calculator_update_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            tax_calculator_url=tax_calculator_url,
        )

        external_tax_calculator_update_data_attributes.additional_properties = d
        return external_tax_calculator_update_data_attributes

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
