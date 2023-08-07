from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_category_create_data_attributes_metadata import TaxCategoryCreateDataAttributesMetadata


T = TypeVar("T", bound="TaxCategoryCreateDataAttributes")


@attr.s(auto_attribs=True)
class TaxCategoryCreateDataAttributes:
    """
    Attributes:
        code (str): The tax category identifier code, specific for a particular tax calculator. Example: 31000.
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, TaxCategoryCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    code: str
    sku_code: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "TaxCategoryCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        sku_code = self.sku_code
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_category_create_data_attributes_metadata import TaxCategoryCreateDataAttributesMetadata

        d = src_dict.copy()
        code = d.pop("code")

        sku_code = d.pop("sku_code", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, TaxCategoryCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TaxCategoryCreateDataAttributesMetadata.from_dict(_metadata)

        tax_category_create_data_attributes = cls(
            code=code,
            sku_code=sku_code,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        tax_category_create_data_attributes.additional_properties = d
        return tax_category_create_data_attributes

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
