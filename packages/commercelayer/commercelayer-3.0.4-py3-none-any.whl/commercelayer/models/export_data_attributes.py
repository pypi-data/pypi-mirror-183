from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_data_attributes_filters import ExportDataAttributesFilters
    from ..models.export_data_attributes_metadata import ExportDataAttributesMetadata


T = TypeVar("T", bound="ExportDataAttributes")


@attr.s(auto_attribs=True)
class ExportDataAttributes:
    """
    Attributes:
        resource_type (Union[Unset, str]): The type of resource being exported. Example: skus.
        format_ (Union[Unset, str]): The format of the export one of 'json' (default) or 'csv'. Example: json.
        status (Union[Unset, str]): The export job status. One of 'pending' (default), 'in_progress', or 'completed'.
            Example: in_progress.
        includes (Union[Unset, List[str]]): List of related resources that should be included in the export. Example:
            ['prices.price_tiers'].
        filters (Union[Unset, ExportDataAttributesFilters]): The filters used to select the records to be exported.
            Example: {'code_eq': 'AAA'}.
        dry_data (Union[Unset, bool]): Send this attribute if you want to skip exporting redundant attributes (IDs,
            timestamps, blanks, etc.), useful when combining export and import to duplicate your dataset.
        started_at (Union[Unset, str]): Time at which the export was started. Example: 2018-01-01T12:00:00.000Z.
        completed_at (Union[Unset, str]): Time at which the export was completed. Example: 2018-01-01T12:00:00.000Z.
        interrupted_at (Union[Unset, str]): Time at which the export was interrupted. Example: 2018-01-01T12:00:00.000Z.
        records_count (Union[Unset, int]): Indicates the number of records to be exported. Example: 300.
        attachment_url (Union[Unset, str]): The URL to the output file, which will be generated upon export completion.
            Example: http://cl_exports.s3.amazonaws.com/.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ExportDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    resource_type: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    includes: Union[Unset, List[str]] = UNSET
    filters: Union[Unset, "ExportDataAttributesFilters"] = UNSET
    dry_data: Union[Unset, bool] = UNSET
    started_at: Union[Unset, str] = UNSET
    completed_at: Union[Unset, str] = UNSET
    interrupted_at: Union[Unset, str] = UNSET
    records_count: Union[Unset, int] = UNSET
    attachment_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ExportDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        format_ = self.format_
        status = self.status
        includes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.includes, Unset):
            includes = self.includes

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        dry_data = self.dry_data
        started_at = self.started_at
        completed_at = self.completed_at
        interrupted_at = self.interrupted_at
        records_count = self.records_count
        attachment_url = self.attachment_url
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if status is not UNSET:
            field_dict["status"] = status
        if includes is not UNSET:
            field_dict["includes"] = includes
        if filters is not UNSET:
            field_dict["filters"] = filters
        if dry_data is not UNSET:
            field_dict["dry_data"] = dry_data
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if interrupted_at is not UNSET:
            field_dict["interrupted_at"] = interrupted_at
        if records_count is not UNSET:
            field_dict["records_count"] = records_count
        if attachment_url is not UNSET:
            field_dict["attachment_url"] = attachment_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.export_data_attributes_filters import ExportDataAttributesFilters
        from ..models.export_data_attributes_metadata import ExportDataAttributesMetadata

        d = src_dict.copy()
        resource_type = d.pop("resource_type", UNSET)

        format_ = d.pop("format", UNSET)

        status = d.pop("status", UNSET)

        includes = cast(List[str], d.pop("includes", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ExportDataAttributesFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ExportDataAttributesFilters.from_dict(_filters)

        dry_data = d.pop("dry_data", UNSET)

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        interrupted_at = d.pop("interrupted_at", UNSET)

        records_count = d.pop("records_count", UNSET)

        attachment_url = d.pop("attachment_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ExportDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExportDataAttributesMetadata.from_dict(_metadata)

        export_data_attributes = cls(
            resource_type=resource_type,
            format_=format_,
            status=status,
            includes=includes,
            filters=filters,
            dry_data=dry_data,
            started_at=started_at,
            completed_at=completed_at,
            interrupted_at=interrupted_at,
            records_count=records_count,
            attachment_url=attachment_url,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        export_data_attributes.additional_properties = d
        return export_data_attributes

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
