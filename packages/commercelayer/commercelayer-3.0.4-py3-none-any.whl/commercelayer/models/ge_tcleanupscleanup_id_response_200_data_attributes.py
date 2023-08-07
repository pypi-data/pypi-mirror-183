from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_errors_log import (
        GETcleanupscleanupIdResponse200DataAttributesErrorsLog,
    )
    from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_filters import (
        GETcleanupscleanupIdResponse200DataAttributesFilters,
    )
    from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_metadata import (
        GETcleanupscleanupIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETcleanupscleanupIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETcleanupscleanupIdResponse200DataAttributes:
    """
    Attributes:
        resource_type (Union[Unset, str]): The type of resource being cleaned. Example: skus.
        status (Union[Unset, str]): The cleanup job status. One of 'pending' (default), 'in_progress', 'interrupted', or
            'completed'. Example: in_progress.
        started_at (Union[Unset, str]): Time at which the cleanup was started. Example: 2018-01-01T12:00:00.000Z.
        completed_at (Union[Unset, str]): Time at which the cleanup was completed. Example: 2018-01-01T12:00:00.000Z.
        interrupted_at (Union[Unset, str]): Time at which the cleanup was interrupted. Example:
            2018-01-01T12:00:00.000Z.
        filters (Union[Unset, GETcleanupscleanupIdResponse200DataAttributesFilters]): The filters used to select the
            records to be cleaned. Example: {'code_eq': 'AAA'}.
        records_count (Union[Unset, int]): Indicates the number of records to be cleaned. Example: 300.
        errors_count (Union[Unset, int]): Indicates the number of cleanup errors, if any. Example: 30.
        processed_count (Union[Unset, int]): Indicates the number of records that have been cleaned. Example: 270.
        errors_log (Union[Unset, GETcleanupscleanupIdResponse200DataAttributesErrorsLog]): Contains the cleanup errors,
            if any. Example: {'ABC': {'name': ['has already been taken']}}.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETcleanupscleanupIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    resource_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    completed_at: Union[Unset, str] = UNSET
    interrupted_at: Union[Unset, str] = UNSET
    filters: Union[Unset, "GETcleanupscleanupIdResponse200DataAttributesFilters"] = UNSET
    records_count: Union[Unset, int] = UNSET
    errors_count: Union[Unset, int] = UNSET
    processed_count: Union[Unset, int] = UNSET
    errors_log: Union[Unset, "GETcleanupscleanupIdResponse200DataAttributesErrorsLog"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETcleanupscleanupIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        status = self.status
        started_at = self.started_at
        completed_at = self.completed_at
        interrupted_at = self.interrupted_at
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        records_count = self.records_count
        errors_count = self.errors_count
        processed_count = self.processed_count
        errors_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors_log, Unset):
            errors_log = self.errors_log.to_dict()

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
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if interrupted_at is not UNSET:
            field_dict["interrupted_at"] = interrupted_at
        if filters is not UNSET:
            field_dict["filters"] = filters
        if records_count is not UNSET:
            field_dict["records_count"] = records_count
        if errors_count is not UNSET:
            field_dict["errors_count"] = errors_count
        if processed_count is not UNSET:
            field_dict["processed_count"] = processed_count
        if errors_log is not UNSET:
            field_dict["errors_log"] = errors_log
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
        from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_errors_log import (
            GETcleanupscleanupIdResponse200DataAttributesErrorsLog,
        )
        from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_filters import (
            GETcleanupscleanupIdResponse200DataAttributesFilters,
        )
        from ..models.ge_tcleanupscleanup_id_response_200_data_attributes_metadata import (
            GETcleanupscleanupIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        resource_type = d.pop("resource_type", UNSET)

        status = d.pop("status", UNSET)

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        interrupted_at = d.pop("interrupted_at", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, GETcleanupscleanupIdResponse200DataAttributesFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = GETcleanupscleanupIdResponse200DataAttributesFilters.from_dict(_filters)

        records_count = d.pop("records_count", UNSET)

        errors_count = d.pop("errors_count", UNSET)

        processed_count = d.pop("processed_count", UNSET)

        _errors_log = d.pop("errors_log", UNSET)
        errors_log: Union[Unset, GETcleanupscleanupIdResponse200DataAttributesErrorsLog]
        if isinstance(_errors_log, Unset):
            errors_log = UNSET
        else:
            errors_log = GETcleanupscleanupIdResponse200DataAttributesErrorsLog.from_dict(_errors_log)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETcleanupscleanupIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETcleanupscleanupIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tcleanupscleanup_id_response_200_data_attributes = cls(
            resource_type=resource_type,
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            interrupted_at=interrupted_at,
            filters=filters,
            records_count=records_count,
            errors_count=errors_count,
            processed_count=processed_count,
            errors_log=errors_log,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tcleanupscleanup_id_response_200_data_attributes.additional_properties = d
        return ge_tcleanupscleanup_id_response_200_data_attributes

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
