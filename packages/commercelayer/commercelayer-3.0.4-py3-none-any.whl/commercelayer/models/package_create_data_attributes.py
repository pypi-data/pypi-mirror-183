from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_create_data_attributes_metadata import PackageCreateDataAttributesMetadata


T = TypeVar("T", bound="PackageCreateDataAttributes")


@attr.s(auto_attribs=True)
class PackageCreateDataAttributes:
    """
    Attributes:
        name (str): Unique name for the package Example: Large (60x40x30).
        length (float): The package length, used to automatically calculate the tax rates from the available carrier
            accounts. Example: 40.0.
        width (float): The package width, used to automatically calculate the tax rates from the available carrier
            accounts. Example: 40.0.
        height (float): The package height, used to automatically calculate the tax rates from the available carrier
            accounts. Example: 25.0.
        unit_of_length (str): The unit of length. Can be one of 'cm', or 'in'. Example: gr.
        code (Union[Unset, str]): The package identifying code Example: YYYY 2000.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PackageCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: str
    length: float
    width: float
    height: float
    unit_of_length: str
    code: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PackageCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        length = self.length
        width = self.width
        height = self.height
        unit_of_length = self.unit_of_length
        code = self.code
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "length": length,
                "width": width,
                "height": height,
                "unit_of_length": unit_of_length,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_create_data_attributes_metadata import PackageCreateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name")

        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit_of_length = d.pop("unit_of_length")

        code = d.pop("code", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PackageCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PackageCreateDataAttributesMetadata.from_dict(_metadata)

        package_create_data_attributes = cls(
            name=name,
            length=length,
            width=width,
            height=height,
            unit_of_length=unit_of_length,
            code=code,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        package_create_data_attributes.additional_properties = d
        return package_create_data_attributes

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
