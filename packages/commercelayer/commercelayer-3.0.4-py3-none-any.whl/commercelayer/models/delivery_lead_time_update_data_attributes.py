from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_lead_time_update_data_attributes_metadata import DeliveryLeadTimeUpdateDataAttributesMetadata


T = TypeVar("T", bound="DeliveryLeadTimeUpdateDataAttributes")


@attr.s(auto_attribs=True)
class DeliveryLeadTimeUpdateDataAttributes:
    """
    Attributes:
        min_hours (Union[Unset, int]): The delivery lead minimum time (in hours) when shipping from the associated stock
            location with the associated shipping method. Example: 48.
        max_hours (Union[Unset, int]): The delivery lead maximun time (in hours) when shipping from the associated stock
            location with the associated shipping method. Example: 72.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, DeliveryLeadTimeUpdateDataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    min_hours: Union[Unset, int] = UNSET
    max_hours: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "DeliveryLeadTimeUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_hours = self.min_hours
        max_hours = self.max_hours
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
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_lead_time_update_data_attributes_metadata import (
            DeliveryLeadTimeUpdateDataAttributesMetadata,
        )

        d = src_dict.copy()
        min_hours = d.pop("min_hours", UNSET)

        max_hours = d.pop("max_hours", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DeliveryLeadTimeUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DeliveryLeadTimeUpdateDataAttributesMetadata.from_dict(_metadata)

        delivery_lead_time_update_data_attributes = cls(
            min_hours=min_hours,
            max_hours=max_hours,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        delivery_lead_time_update_data_attributes.additional_properties = d
        return delivery_lead_time_update_data_attributes

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
