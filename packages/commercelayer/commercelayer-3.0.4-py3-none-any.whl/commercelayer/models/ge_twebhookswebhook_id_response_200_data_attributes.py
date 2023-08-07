from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_twebhookswebhook_id_response_200_data_attributes_metadata import (
        GETwebhookswebhookIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETwebhookswebhookIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETwebhookswebhookIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Unique name for the webhook. Example: myorg-orders.place.
        topic (Union[Unset, str]): The identifier of the resource/event that will trigger the webhook. Example:
            orders.place.
        callback_url (Union[Unset, str]): URI where the webhook subscription should send the POST request when the event
            occurs.
        include_resources (Union[Unset, List[str]]): List of related resources that should be included in the webhook
            body. Example: ['customer', 'shipping_address', 'billing_address'].
        circuit_state (Union[Unset, str]): The circuit breaker state, by default it is 'closed'. It can become 'open'
            once the number of consecutive failures overlaps the specified threshold, in such case no further calls to the
            failing callback are made. Example: closed.
        circuit_failure_count (Union[Unset, int]): The number of consecutive failures recorded by the circuit breaker
            associated to this webhook, will be reset on first successful call to callback. Example: 5.
        shared_secret (Union[Unset, str]): The shared secret used to sign the external request payload. Example:
            https://yourapp.com/webhooks.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETwebhookswebhookIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    callback_url: Union[Unset, str] = UNSET
    include_resources: Union[Unset, List[str]] = UNSET
    circuit_state: Union[Unset, str] = UNSET
    circuit_failure_count: Union[Unset, int] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETwebhookswebhookIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        topic = self.topic
        callback_url = self.callback_url
        include_resources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_resources, Unset):
            include_resources = self.include_resources

        circuit_state = self.circuit_state
        circuit_failure_count = self.circuit_failure_count
        shared_secret = self.shared_secret
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
        if name is not UNSET:
            field_dict["name"] = name
        if topic is not UNSET:
            field_dict["topic"] = topic
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if include_resources is not UNSET:
            field_dict["include_resources"] = include_resources
        if circuit_state is not UNSET:
            field_dict["circuit_state"] = circuit_state
        if circuit_failure_count is not UNSET:
            field_dict["circuit_failure_count"] = circuit_failure_count
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
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
        from ..models.ge_twebhookswebhook_id_response_200_data_attributes_metadata import (
            GETwebhookswebhookIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        topic = d.pop("topic", UNSET)

        callback_url = d.pop("callback_url", UNSET)

        include_resources = cast(List[str], d.pop("include_resources", UNSET))

        circuit_state = d.pop("circuit_state", UNSET)

        circuit_failure_count = d.pop("circuit_failure_count", UNSET)

        shared_secret = d.pop("shared_secret", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETwebhookswebhookIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETwebhookswebhookIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_twebhookswebhook_id_response_200_data_attributes = cls(
            name=name,
            topic=topic,
            callback_url=callback_url,
            include_resources=include_resources,
            circuit_state=circuit_state,
            circuit_failure_count=circuit_failure_count,
            shared_secret=shared_secret,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_twebhookswebhook_id_response_200_data_attributes.additional_properties = d
        return ge_twebhookswebhook_id_response_200_data_attributes

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
