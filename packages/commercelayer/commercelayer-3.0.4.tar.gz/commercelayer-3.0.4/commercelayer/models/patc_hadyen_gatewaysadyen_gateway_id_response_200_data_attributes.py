from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hadyen_gatewaysadyen_gateway_id_response_200_data_attributes_metadata import (
        PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The payment gateway's internal name. Example: US payment gateway.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
        merchant_account (Union[Unset, str]): The gateway merchant account. Example: xxxx-yyyy-zzzz.
        api_key (Union[Unset, str]): The gateway API key. Example: xxxx-yyyy-zzzz.
        public_key (Union[Unset, str]): The public key linked to your API credential. Example: xxxx-yyyy-zzzz.
        live_url_prefix (Union[Unset, str]): The prefix of the endpoint used for live transactions. Example:
            1797a841fbb37ca7-AdyenDemo.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata"] = UNSET
    merchant_account: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    live_url_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        merchant_account = self.merchant_account
        api_key = self.api_key
        public_key = self.public_key
        live_url_prefix = self.live_url_prefix

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
        if merchant_account is not UNSET:
            field_dict["merchant_account"] = merchant_account
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if live_url_prefix is not UNSET:
            field_dict["live_url_prefix"] = live_url_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hadyen_gatewaysadyen_gateway_id_response_200_data_attributes_metadata import (
            PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHadyenGatewaysadyenGatewayIdResponse200DataAttributesMetadata.from_dict(_metadata)

        merchant_account = d.pop("merchant_account", UNSET)

        api_key = d.pop("api_key", UNSET)

        public_key = d.pop("public_key", UNSET)

        live_url_prefix = d.pop("live_url_prefix", UNSET)

        patc_hadyen_gatewaysadyen_gateway_id_response_200_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            merchant_account=merchant_account,
            api_key=api_key,
            public_key=public_key,
            live_url_prefix=live_url_prefix,
        )

        patc_hadyen_gatewaysadyen_gateway_id_response_200_data_attributes.additional_properties = d
        return patc_hadyen_gatewaysadyen_gateway_id_response_200_data_attributes

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
