from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_callback_data_attributes_metadata import EventCallbackDataAttributesMetadata
    from ..models.event_callback_data_attributes_payload import EventCallbackDataAttributesPayload


T = TypeVar("T", bound="EventCallbackDataAttributes")


@attr.s(auto_attribs=True)
class EventCallbackDataAttributes:
    """
    Attributes:
        callback_url (Union[Unset, str]): The URI of the callback, inherited by the associated webhook. Example:
            https://yourapp.com/webhooks.
        payload (Union[Unset, EventCallbackDataAttributesPayload]): The payload sent to the callback endpoint, including
            the event affected resource and the specified includes. Example: {'data': {'attributes': {'id': 'PYWehaoXJj',
            'type': 'orders'}}}.
        response_code (Union[Unset, str]): The HTTP response code of the callback endpoint. Example: 200.
        response_message (Union[Unset, str]): The HTTP response message of the callback endpoint. Example: OK.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, EventCallbackDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    callback_url: Union[Unset, str] = UNSET
    payload: Union[Unset, "EventCallbackDataAttributesPayload"] = UNSET
    response_code: Union[Unset, str] = UNSET
    response_message: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "EventCallbackDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        callback_url = self.callback_url
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        response_code = self.response_code
        response_message = self.response_message
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
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if payload is not UNSET:
            field_dict["payload"] = payload
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if response_message is not UNSET:
            field_dict["response_message"] = response_message
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
        from ..models.event_callback_data_attributes_metadata import EventCallbackDataAttributesMetadata
        from ..models.event_callback_data_attributes_payload import EventCallbackDataAttributesPayload

        d = src_dict.copy()
        callback_url = d.pop("callback_url", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, EventCallbackDataAttributesPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = EventCallbackDataAttributesPayload.from_dict(_payload)

        response_code = d.pop("response_code", UNSET)

        response_message = d.pop("response_message", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, EventCallbackDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EventCallbackDataAttributesMetadata.from_dict(_metadata)

        event_callback_data_attributes = cls(
            callback_url=callback_url,
            payload=payload,
            response_code=response_code,
            response_message=response_message,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        event_callback_data_attributes.additional_properties = d
        return event_callback_data_attributes

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
