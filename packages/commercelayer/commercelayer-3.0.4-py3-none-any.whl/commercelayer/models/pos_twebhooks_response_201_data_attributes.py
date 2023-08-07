from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_twebhooks_response_201_data_attributes_metadata import (
        POSTwebhooksResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTwebhooksResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTwebhooksResponse201DataAttributes:
    """
    Attributes:
        topic (str): The identifier of the resource/event that will trigger the webhook. Example: orders.place.
        callback_url (str): URI where the webhook subscription should send the POST request when the event occurs.
        name (Union[Unset, str]): Unique name for the webhook. Example: myorg-orders.place.
        include_resources (Union[Unset, List[str]]): List of related resources that should be included in the webhook
            body. Example: ['customer', 'shipping_address', 'billing_address'].
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTwebhooksResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    topic: str
    callback_url: str
    name: Union[Unset, str] = UNSET
    include_resources: Union[Unset, List[str]] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTwebhooksResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        topic = self.topic
        callback_url = self.callback_url
        name = self.name
        include_resources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_resources, Unset):
            include_resources = self.include_resources

        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
                "callback_url": callback_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if include_resources is not UNSET:
            field_dict["include_resources"] = include_resources
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_twebhooks_response_201_data_attributes_metadata import (
            POSTwebhooksResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        topic = d.pop("topic")

        callback_url = d.pop("callback_url")

        name = d.pop("name", UNSET)

        include_resources = cast(List[str], d.pop("include_resources", UNSET))

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTwebhooksResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTwebhooksResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_twebhooks_response_201_data_attributes = cls(
            topic=topic,
            callback_url=callback_url,
            name=name,
            include_resources=include_resources,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_twebhooks_response_201_data_attributes.additional_properties = d
        return pos_twebhooks_response_201_data_attributes

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
