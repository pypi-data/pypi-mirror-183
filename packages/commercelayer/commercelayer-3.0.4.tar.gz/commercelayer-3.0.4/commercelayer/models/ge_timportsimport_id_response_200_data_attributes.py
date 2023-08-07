from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_timportsimport_id_response_200_data_attributes_errors_log import (
        GETimportsimportIdResponse200DataAttributesErrorsLog,
    )
    from ..models.ge_timportsimport_id_response_200_data_attributes_inputs_item import (
        GETimportsimportIdResponse200DataAttributesInputsItem,
    )
    from ..models.ge_timportsimport_id_response_200_data_attributes_metadata import (
        GETimportsimportIdResponse200DataAttributesMetadata,
    )
    from ..models.ge_timportsimport_id_response_200_data_attributes_warnings_log import (
        GETimportsimportIdResponse200DataAttributesWarningsLog,
    )


T = TypeVar("T", bound="GETimportsimportIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETimportsimportIdResponse200DataAttributes:
    """
    Attributes:
        resource_type (Union[Unset, str]): The type of resource being imported. Example: skus.
        parent_resource_id (Union[Unset, str]): The ID of the parent resource to be associated with imported data.
            Example: 1234.
        status (Union[Unset, str]): The import job status. One of 'pending' (default), 'in_progress', 'interrupted', or
            'completed'. Example: in_progress.
        started_at (Union[Unset, str]): Time at which the import was started. Example: 2018-01-01T12:00:00.000Z.
        completed_at (Union[Unset, str]): Time at which the import was completed. Example: 2018-01-01T12:00:00.000Z.
        interrupted_at (Union[Unset, str]): Time at which the import was interrupted. Example: 2018-01-01T12:00:00.000Z.
        inputs (Union[Unset, List['GETimportsimportIdResponse200DataAttributesInputsItem']]): Array of objects
            representing the resources that are being imported. Example: [{'code': 'ABC', 'name': 'Foo'}, {'code': 'DEF',
            'name': 'Bar'}].
        inputs_size (Union[Unset, int]): Indicates the size of the objects to be imported. Example: 300.
        errors_count (Union[Unset, int]): Indicates the number of import errors, if any. Example: 30.
        warnings_count (Union[Unset, int]): Indicates the number of import warnings, if any. Example: 1.
        destroyed_count (Union[Unset, int]): Indicates the number of records that have been destroyed, if any. Example:
            99.
        processed_count (Union[Unset, int]): Indicates the number of records that have been processed (created or
            updated). Example: 270.
        errors_log (Union[Unset, GETimportsimportIdResponse200DataAttributesErrorsLog]): Contains the import errors, if
            any. Example: {'ABC': {'name': ['has already been taken']}}.
        warnings_log (Union[Unset, GETimportsimportIdResponse200DataAttributesWarningsLog]): Contains the import
            warnings, if any. Example: {'ABC': ['could not be deleted']}.
        cleanup_records (Union[Unset, bool]): Indicates if the import should cleanup records that are not included in
            the inputs array. Example: True.
        attachment_url (Union[Unset, str]): The URL the the raw inputs file, which will be generated at import start.
            Example: http://cl_imports.s3.amazonaws.com/.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETimportsimportIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    resource_type: Union[Unset, str] = UNSET
    parent_resource_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    completed_at: Union[Unset, str] = UNSET
    interrupted_at: Union[Unset, str] = UNSET
    inputs: Union[Unset, List["GETimportsimportIdResponse200DataAttributesInputsItem"]] = UNSET
    inputs_size: Union[Unset, int] = UNSET
    errors_count: Union[Unset, int] = UNSET
    warnings_count: Union[Unset, int] = UNSET
    destroyed_count: Union[Unset, int] = UNSET
    processed_count: Union[Unset, int] = UNSET
    errors_log: Union[Unset, "GETimportsimportIdResponse200DataAttributesErrorsLog"] = UNSET
    warnings_log: Union[Unset, "GETimportsimportIdResponse200DataAttributesWarningsLog"] = UNSET
    cleanup_records: Union[Unset, bool] = UNSET
    attachment_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETimportsimportIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        parent_resource_id = self.parent_resource_id
        status = self.status
        started_at = self.started_at
        completed_at = self.completed_at
        interrupted_at = self.interrupted_at
        inputs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()

                inputs.append(inputs_item)

        inputs_size = self.inputs_size
        errors_count = self.errors_count
        warnings_count = self.warnings_count
        destroyed_count = self.destroyed_count
        processed_count = self.processed_count
        errors_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors_log, Unset):
            errors_log = self.errors_log.to_dict()

        warnings_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.warnings_log, Unset):
            warnings_log = self.warnings_log.to_dict()

        cleanup_records = self.cleanup_records
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
        if parent_resource_id is not UNSET:
            field_dict["parent_resource_id"] = parent_resource_id
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if interrupted_at is not UNSET:
            field_dict["interrupted_at"] = interrupted_at
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if inputs_size is not UNSET:
            field_dict["inputs_size"] = inputs_size
        if errors_count is not UNSET:
            field_dict["errors_count"] = errors_count
        if warnings_count is not UNSET:
            field_dict["warnings_count"] = warnings_count
        if destroyed_count is not UNSET:
            field_dict["destroyed_count"] = destroyed_count
        if processed_count is not UNSET:
            field_dict["processed_count"] = processed_count
        if errors_log is not UNSET:
            field_dict["errors_log"] = errors_log
        if warnings_log is not UNSET:
            field_dict["warnings_log"] = warnings_log
        if cleanup_records is not UNSET:
            field_dict["cleanup_records"] = cleanup_records
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
        from ..models.ge_timportsimport_id_response_200_data_attributes_errors_log import (
            GETimportsimportIdResponse200DataAttributesErrorsLog,
        )
        from ..models.ge_timportsimport_id_response_200_data_attributes_inputs_item import (
            GETimportsimportIdResponse200DataAttributesInputsItem,
        )
        from ..models.ge_timportsimport_id_response_200_data_attributes_metadata import (
            GETimportsimportIdResponse200DataAttributesMetadata,
        )
        from ..models.ge_timportsimport_id_response_200_data_attributes_warnings_log import (
            GETimportsimportIdResponse200DataAttributesWarningsLog,
        )

        d = src_dict.copy()
        resource_type = d.pop("resource_type", UNSET)

        parent_resource_id = d.pop("parent_resource_id", UNSET)

        status = d.pop("status", UNSET)

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        interrupted_at = d.pop("interrupted_at", UNSET)

        inputs = []
        _inputs = d.pop("inputs", UNSET)
        for inputs_item_data in _inputs or []:
            inputs_item = GETimportsimportIdResponse200DataAttributesInputsItem.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        inputs_size = d.pop("inputs_size", UNSET)

        errors_count = d.pop("errors_count", UNSET)

        warnings_count = d.pop("warnings_count", UNSET)

        destroyed_count = d.pop("destroyed_count", UNSET)

        processed_count = d.pop("processed_count", UNSET)

        _errors_log = d.pop("errors_log", UNSET)
        errors_log: Union[Unset, GETimportsimportIdResponse200DataAttributesErrorsLog]
        if isinstance(_errors_log, Unset):
            errors_log = UNSET
        else:
            errors_log = GETimportsimportIdResponse200DataAttributesErrorsLog.from_dict(_errors_log)

        _warnings_log = d.pop("warnings_log", UNSET)
        warnings_log: Union[Unset, GETimportsimportIdResponse200DataAttributesWarningsLog]
        if isinstance(_warnings_log, Unset):
            warnings_log = UNSET
        else:
            warnings_log = GETimportsimportIdResponse200DataAttributesWarningsLog.from_dict(_warnings_log)

        cleanup_records = d.pop("cleanup_records", UNSET)

        attachment_url = d.pop("attachment_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETimportsimportIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETimportsimportIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_timportsimport_id_response_200_data_attributes = cls(
            resource_type=resource_type,
            parent_resource_id=parent_resource_id,
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            interrupted_at=interrupted_at,
            inputs=inputs,
            inputs_size=inputs_size,
            errors_count=errors_count,
            warnings_count=warnings_count,
            destroyed_count=destroyed_count,
            processed_count=processed_count,
            errors_log=errors_log,
            warnings_log=warnings_log,
            cleanup_records=cleanup_records,
            attachment_url=attachment_url,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_timportsimport_id_response_200_data_attributes.additional_properties = d
        return ge_timportsimport_id_response_200_data_attributes

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
