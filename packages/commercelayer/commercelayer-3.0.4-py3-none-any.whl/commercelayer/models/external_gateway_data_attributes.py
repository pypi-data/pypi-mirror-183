from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_gateway_data_attributes_metadata import ExternalGatewayDataAttributesMetadata


T = TypeVar("T", bound="ExternalGatewayDataAttributes")


@attr.s(auto_attribs=True)
class ExternalGatewayDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The payment gateway's internal name. Example: US payment gateway.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ExternalGatewayDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
        shared_secret (Union[Unset, str]): The shared secret used to sign the external request payload. Example: xxxx-
            yyyy-zzzz.
        authorize_url (Union[Unset, str]): The endpoint used by the external gateway to authorize payments. Example:
            https://external_gateway.com/authorize.
        capture_url (Union[Unset, str]): The endpoint used by the external gateway to capture payments. Example:
            https://external_gateway.com/capture.
        void_url (Union[Unset, str]): The endpoint used by the external gateway to void payments. Example:
            https://external_gateway.com/void.
        refund_url (Union[Unset, str]): The endpoint used by the external gateway to refund payments. Example:
            https://external_gateway.com/refund.
        token_url (Union[Unset, str]): The endpoint used by the external gateway to create a customer payment token.
            Example: https://external_gateway.com/token.
    """

    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ExternalGatewayDataAttributesMetadata"] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    authorize_url: Union[Unset, str] = UNSET
    capture_url: Union[Unset, str] = UNSET
    void_url: Union[Unset, str] = UNSET
    refund_url: Union[Unset, str] = UNSET
    token_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        shared_secret = self.shared_secret
        authorize_url = self.authorize_url
        capture_url = self.capture_url
        void_url = self.void_url
        refund_url = self.refund_url
        token_url = self.token_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if authorize_url is not UNSET:
            field_dict["authorize_url"] = authorize_url
        if capture_url is not UNSET:
            field_dict["capture_url"] = capture_url
        if void_url is not UNSET:
            field_dict["void_url"] = void_url
        if refund_url is not UNSET:
            field_dict["refund_url"] = refund_url
        if token_url is not UNSET:
            field_dict["token_url"] = token_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_gateway_data_attributes_metadata import ExternalGatewayDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ExternalGatewayDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExternalGatewayDataAttributesMetadata.from_dict(_metadata)

        shared_secret = d.pop("shared_secret", UNSET)

        authorize_url = d.pop("authorize_url", UNSET)

        capture_url = d.pop("capture_url", UNSET)

        void_url = d.pop("void_url", UNSET)

        refund_url = d.pop("refund_url", UNSET)

        token_url = d.pop("token_url", UNSET)

        external_gateway_data_attributes = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            shared_secret=shared_secret,
            authorize_url=authorize_url,
            capture_url=capture_url,
            void_url=void_url,
            refund_url=refund_url,
            token_url=token_url,
        )

        external_gateway_data_attributes.additional_properties = d
        return external_gateway_data_attributes

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
