from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_update_data_attributes_metadata import WebhookUpdateDataAttributesMetadata


T = TypeVar("T", bound="WebhookUpdateDataAttributes")


@attr.s(auto_attribs=True)
class WebhookUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Unique name for the webhook. Example: myorg-orders.place.
        topic (Union[Unset, str]): The identifier of the resource/event that will trigger the webhook. Example:
            orders.place.
        callback_url (Union[Unset, str]): URI where the webhook subscription should send the POST request when the event
            occurs.
        include_resources (Union[Unset, List[str]]): List of related resources that should be included in the webhook
            body. Example: ['customer', 'shipping_address', 'billing_address'].
        reset_circuit (Union[Unset, bool]): Send this attribute if you want to reset the circuit breaker associated to
            this webhook to 'closed' state and zero failures count. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, WebhookUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    callback_url: Union[Unset, str] = UNSET
    include_resources: Union[Unset, List[str]] = UNSET
    reset_circuit: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "WebhookUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        topic = self.topic
        callback_url = self.callback_url
        include_resources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_resources, Unset):
            include_resources = self.include_resources

        reset_circuit = self.reset_circuit
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
        if reset_circuit is not UNSET:
            field_dict["_reset_circuit"] = reset_circuit
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_update_data_attributes_metadata import WebhookUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        topic = d.pop("topic", UNSET)

        callback_url = d.pop("callback_url", UNSET)

        include_resources = cast(List[str], d.pop("include_resources", UNSET))

        reset_circuit = d.pop("_reset_circuit", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, WebhookUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WebhookUpdateDataAttributesMetadata.from_dict(_metadata)

        webhook_update_data_attributes = cls(
            name=name,
            topic=topic,
            callback_url=callback_url,
            include_resources=include_resources,
            reset_circuit=reset_circuit,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        webhook_update_data_attributes.additional_properties = d
        return webhook_update_data_attributes

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
