from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tdelivery_lead_times_response_200_data_item_attributes_metadata import (
        GETdeliveryLeadTimesResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETdeliveryLeadTimesResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETdeliveryLeadTimesResponse200DataItemAttributes:
    """
    Attributes:
        min_hours (Union[Unset, int]): The delivery lead minimum time (in hours) when shipping from the associated stock
            location with the associated shipping method. Example: 48.
        max_hours (Union[Unset, int]): The delivery lead maximun time (in hours) when shipping from the associated stock
            location with the associated shipping method. Example: 72.
        min_days (Union[Unset, int]): The delivery lead minimum time, in days (rounded) Example: 2.
        max_days (Union[Unset, int]): The delivery lead maximun time, in days (rounded) Example: 3.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETdeliveryLeadTimesResponse200DataItemAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    min_hours: Union[Unset, int] = UNSET
    max_hours: Union[Unset, int] = UNSET
    min_days: Union[Unset, int] = UNSET
    max_days: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETdeliveryLeadTimesResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_hours = self.min_hours
        max_hours = self.max_hours
        min_days = self.min_days
        max_days = self.max_days
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
        if min_hours is not UNSET:
            field_dict["min_hours"] = min_hours
        if max_hours is not UNSET:
            field_dict["max_hours"] = max_hours
        if min_days is not UNSET:
            field_dict["min_days"] = min_days
        if max_days is not UNSET:
            field_dict["max_days"] = max_days
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
        from ..models.ge_tdelivery_lead_times_response_200_data_item_attributes_metadata import (
            GETdeliveryLeadTimesResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        min_hours = d.pop("min_hours", UNSET)

        max_hours = d.pop("max_hours", UNSET)

        min_days = d.pop("min_days", UNSET)

        max_days = d.pop("max_days", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETdeliveryLeadTimesResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETdeliveryLeadTimesResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tdelivery_lead_times_response_200_data_item_attributes = cls(
            min_hours=min_hours,
            max_hours=max_hours,
            min_days=min_days,
            max_days=max_days,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tdelivery_lead_times_response_200_data_item_attributes.additional_properties = d
        return ge_tdelivery_lead_times_response_200_data_item_attributes

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
