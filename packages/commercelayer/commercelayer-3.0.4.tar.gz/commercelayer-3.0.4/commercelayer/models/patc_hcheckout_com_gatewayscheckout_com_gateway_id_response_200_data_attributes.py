from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_attributes_metadata import (
        PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The payment gateway's internal name. Example: US payment gateway.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata]): Set of
            key-value pairs that you can attach to the resource. This can be useful for storing additional information about
            the resource in a structured format. Example: {'foo': 'bar'}.
        secret_key (Union[Unset, str]): The gateway secret key. Example: sk_test_xxxx-yyyy-zzzz.
        public_key (Union[Unset, str]): The gateway public key. Example: pk_test_xxxx-yyyy-zzzz.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata"] = UNSET
    secret_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        secret_key = self.secret_key
        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_attributes_metadata import (
            PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataAttributesMetadata.from_dict(
                _metadata
            )

        secret_key = d.pop("secret_key", UNSET)

        public_key = d.pop("public_key", UNSET)

        patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            secret_key=secret_key,
            public_key=public_key,
        )

        patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_attributes.additional_properties = d
        return patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_attributes

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
