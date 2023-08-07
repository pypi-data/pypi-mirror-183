from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_copies_response_200_data_item_attributes_errors_log import (
        GETorderCopiesResponse200DataItemAttributesErrorsLog,
    )
    from ..models.ge_torder_copies_response_200_data_item_attributes_metadata import (
        GETorderCopiesResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETorderCopiesResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETorderCopiesResponse200DataItemAttributes:
    """
    Attributes:
        status (Union[Unset, str]): The order copy status. One of 'pending' (default), 'in_progress', 'failed', or
            'completed'. Example: in_progress.
        started_at (Union[Unset, str]): Time at which the order copy was started. Example: 2018-01-01T12:00:00.000Z.
        completed_at (Union[Unset, str]): Time at which the order copy was completed. Example: 2018-01-01T12:00:00.000Z.
        failed_at (Union[Unset, str]): Time at which the order copy has failed. Example: 2018-01-01T12:00:00.000Z.
        place_target_order (Union[Unset, bool]): Indicates if the target order must be placed upon copy. Example: True.
        cancel_source_order (Union[Unset, bool]): Indicates if the source order must be cancelled upon copy. Example:
            True.
        reuse_wallet (Union[Unset, bool]): Indicates if the payment source within the source order customer's wallet
            must be copied. Example: True.
        errors_log (Union[Unset, GETorderCopiesResponse200DataItemAttributesErrorsLog]): Contains the order copy errors,
            if any. Example: {'status': ['cannot transition from draft to placed']}.
        errors_count (Union[Unset, int]): Indicates the number of copy errors, if any. Example: 2.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETorderCopiesResponse200DataItemAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    status: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    completed_at: Union[Unset, str] = UNSET
    failed_at: Union[Unset, str] = UNSET
    place_target_order: Union[Unset, bool] = UNSET
    cancel_source_order: Union[Unset, bool] = UNSET
    reuse_wallet: Union[Unset, bool] = UNSET
    errors_log: Union[Unset, "GETorderCopiesResponse200DataItemAttributesErrorsLog"] = UNSET
    errors_count: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETorderCopiesResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        started_at = self.started_at
        completed_at = self.completed_at
        failed_at = self.failed_at
        place_target_order = self.place_target_order
        cancel_source_order = self.cancel_source_order
        reuse_wallet = self.reuse_wallet
        errors_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors_log, Unset):
            errors_log = self.errors_log.to_dict()

        errors_count = self.errors_count
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
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if place_target_order is not UNSET:
            field_dict["place_target_order"] = place_target_order
        if cancel_source_order is not UNSET:
            field_dict["cancel_source_order"] = cancel_source_order
        if reuse_wallet is not UNSET:
            field_dict["reuse_wallet"] = reuse_wallet
        if errors_log is not UNSET:
            field_dict["errors_log"] = errors_log
        if errors_count is not UNSET:
            field_dict["errors_count"] = errors_count
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
        from ..models.ge_torder_copies_response_200_data_item_attributes_errors_log import (
            GETorderCopiesResponse200DataItemAttributesErrorsLog,
        )
        from ..models.ge_torder_copies_response_200_data_item_attributes_metadata import (
            GETorderCopiesResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        started_at = d.pop("started_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        failed_at = d.pop("failed_at", UNSET)

        place_target_order = d.pop("place_target_order", UNSET)

        cancel_source_order = d.pop("cancel_source_order", UNSET)

        reuse_wallet = d.pop("reuse_wallet", UNSET)

        _errors_log = d.pop("errors_log", UNSET)
        errors_log: Union[Unset, GETorderCopiesResponse200DataItemAttributesErrorsLog]
        if isinstance(_errors_log, Unset):
            errors_log = UNSET
        else:
            errors_log = GETorderCopiesResponse200DataItemAttributesErrorsLog.from_dict(_errors_log)

        errors_count = d.pop("errors_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETorderCopiesResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETorderCopiesResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_torder_copies_response_200_data_item_attributes = cls(
            status=status,
            started_at=started_at,
            completed_at=completed_at,
            failed_at=failed_at,
            place_target_order=place_target_order,
            cancel_source_order=cancel_source_order,
            reuse_wallet=reuse_wallet,
            errors_log=errors_log,
            errors_count=errors_count,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_torder_copies_response_200_data_item_attributes.additional_properties = d
        return ge_torder_copies_response_200_data_item_attributes

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
