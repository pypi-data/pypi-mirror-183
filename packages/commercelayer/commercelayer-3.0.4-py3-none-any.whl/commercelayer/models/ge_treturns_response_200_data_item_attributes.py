from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_treturns_response_200_data_item_attributes_metadata import (
        GETreturnsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETreturnsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETreturnsResponse200DataItemAttributes:
    """
    Attributes:
        number (Union[Unset, str]): Unique identifier for the return Example: #1234/R/001.
        status (Union[Unset, str]): The return status, one of 'draft', 'requested', 'approved', 'cancelled', 'shipped',
            'rejected' or 'received' Example: draft.
        customer_email (Union[Unset, str]): The email address of the associated customer. Example: john@example.com.
        skus_count (Union[Unset, int]): The total number of SKUs in the return's line items. This can be useful to
            display a preview of the return content. Example: 2.
        approved_at (Union[Unset, str]): Time at which the return was approved. Example: 2018-01-01T12:00:00.000Z.
        cancelled_at (Union[Unset, str]): Time at which the return was cancelled. Example: 2018-01-01T12:00:00.000Z.
        shipped_at (Union[Unset, str]): Time at which the return was shipped. Example: 2018-01-01T12:00:00.000Z.
        rejected_at (Union[Unset, str]): Time at which the return was rejected. Example: 2018-01-01T12:00:00.000Z.
        received_at (Union[Unset, str]): Time at which the return was received. Example: 2018-01-01T12:00:00.000Z.
        archived_at (Union[Unset, str]): Time at which the resource has been archived. Example:
            2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETreturnsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    number: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    customer_email: Union[Unset, str] = UNSET
    skus_count: Union[Unset, int] = UNSET
    approved_at: Union[Unset, str] = UNSET
    cancelled_at: Union[Unset, str] = UNSET
    shipped_at: Union[Unset, str] = UNSET
    rejected_at: Union[Unset, str] = UNSET
    received_at: Union[Unset, str] = UNSET
    archived_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETreturnsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        status = self.status
        customer_email = self.customer_email
        skus_count = self.skus_count
        approved_at = self.approved_at
        cancelled_at = self.cancelled_at
        shipped_at = self.shipped_at
        rejected_at = self.rejected_at
        received_at = self.received_at
        archived_at = self.archived_at
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
        if number is not UNSET:
            field_dict["number"] = number
        if status is not UNSET:
            field_dict["status"] = status
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if skus_count is not UNSET:
            field_dict["skus_count"] = skus_count
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if shipped_at is not UNSET:
            field_dict["shipped_at"] = shipped_at
        if rejected_at is not UNSET:
            field_dict["rejected_at"] = rejected_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
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
        from ..models.ge_treturns_response_200_data_item_attributes_metadata import (
            GETreturnsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        status = d.pop("status", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        skus_count = d.pop("skus_count", UNSET)

        approved_at = d.pop("approved_at", UNSET)

        cancelled_at = d.pop("cancelled_at", UNSET)

        shipped_at = d.pop("shipped_at", UNSET)

        rejected_at = d.pop("rejected_at", UNSET)

        received_at = d.pop("received_at", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETreturnsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETreturnsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_treturns_response_200_data_item_attributes = cls(
            number=number,
            status=status,
            customer_email=customer_email,
            skus_count=skus_count,
            approved_at=approved_at,
            cancelled_at=cancelled_at,
            shipped_at=shipped_at,
            rejected_at=rejected_at,
            received_at=received_at,
            archived_at=archived_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_treturns_response_200_data_item_attributes.additional_properties = d
        return ge_treturns_response_200_data_item_attributes

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
