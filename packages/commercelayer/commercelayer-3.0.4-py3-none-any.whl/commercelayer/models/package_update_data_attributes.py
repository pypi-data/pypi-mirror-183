from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_update_data_attributes_metadata import PackageUpdateDataAttributesMetadata


T = TypeVar("T", bound="PackageUpdateDataAttributes")


@attr.s(auto_attribs=True)
class PackageUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Unique name for the package Example: Large (60x40x30).
        code (Union[Unset, str]): The package identifying code Example: YYYY 2000.
        length (Union[Unset, float]): The package length, used to automatically calculate the tax rates from the
            available carrier accounts. Example: 40.0.
        width (Union[Unset, float]): The package width, used to automatically calculate the tax rates from the available
            carrier accounts. Example: 40.0.
        height (Union[Unset, float]): The package height, used to automatically calculate the tax rates from the
            available carrier accounts. Example: 25.0.
        unit_of_length (Union[Unset, str]): The unit of length. Can be one of 'cm', or 'in'. Example: gr.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PackageUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    unit_of_length: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PackageUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        code = self.code
        length = self.length
        width = self.width
        height = self.height
        unit_of_length = self.unit_of_length
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if unit_of_length is not UNSET:
            field_dict["unit_of_length"] = unit_of_length
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_update_data_attributes_metadata import PackageUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        unit_of_length = d.pop("unit_of_length", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PackageUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PackageUpdateDataAttributesMetadata.from_dict(_metadata)

        package_update_data_attributes = cls(
            name=name,
            code=code,
            length=length,
            width=width,
            height=height,
            unit_of_length=unit_of_length,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        package_update_data_attributes.additional_properties = d
        return package_update_data_attributes

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
