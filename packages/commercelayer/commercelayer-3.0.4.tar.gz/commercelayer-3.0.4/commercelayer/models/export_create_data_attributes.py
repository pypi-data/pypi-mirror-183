from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_create_data_attributes_filters import ExportCreateDataAttributesFilters
    from ..models.export_create_data_attributes_metadata import ExportCreateDataAttributesMetadata


T = TypeVar("T", bound="ExportCreateDataAttributes")


@attr.s(auto_attribs=True)
class ExportCreateDataAttributes:
    """
    Attributes:
        resource_type (str): The type of resource being exported. Example: skus.
        format_ (Union[Unset, str]): The format of the export one of 'json' (default) or 'csv'. Example: json.
        includes (Union[Unset, List[str]]): List of related resources that should be included in the export. Example:
            ['prices.price_tiers'].
        filters (Union[Unset, ExportCreateDataAttributesFilters]): The filters used to select the records to be
            exported. Example: {'code_eq': 'AAA'}.
        dry_data (Union[Unset, bool]): Send this attribute if you want to skip exporting redundant attributes (IDs,
            timestamps, blanks, etc.), useful when combining export and import to duplicate your dataset.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ExportCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    resource_type: str
    format_: Union[Unset, str] = UNSET
    includes: Union[Unset, List[str]] = UNSET
    filters: Union[Unset, "ExportCreateDataAttributesFilters"] = UNSET
    dry_data: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ExportCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        format_ = self.format_
        includes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        dry_data = self.dry_data
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if includes is not UNSET:
            field_dict["includes"] = includes
        if filters is not UNSET:
            field_dict["filters"] = filters
        if dry_data is not UNSET:
            field_dict["dry_data"] = dry_data
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.export_create_data_attributes_filters import ExportCreateDataAttributesFilters
        from ..models.export_create_data_attributes_metadata import ExportCreateDataAttributesMetadata

        d = src_dict.copy()
        resource_type = d.pop("resource_type")

        format_ = d.pop("format", UNSET)

        includes = cast(List[str], d.pop("includes", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ExportCreateDataAttributesFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ExportCreateDataAttributesFilters.from_dict(_filters)

        dry_data = d.pop("dry_data", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ExportCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExportCreateDataAttributesMetadata.from_dict(_metadata)

        export_create_data_attributes = cls(
            resource_type=resource_type,
            format_=format_,
            includes=includes,
            filters=filters,
            dry_data=dry_data,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        export_create_data_attributes.additional_properties = d
        return export_create_data_attributes

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
