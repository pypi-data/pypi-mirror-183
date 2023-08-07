from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_attributes_metadata import (
        PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The payment gateway's internal name. Example: US payment gateway.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata]): Set of key-
            value pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
        merchant_account_id (Union[Unset, str]): The gateway merchant account ID. Example: xxxx-yyyy-zzzz.
        merchant_id (Union[Unset, str]): The gateway merchant ID. Example: xxxx-yyyy-zzzz.
        public_key (Union[Unset, str]): The gateway API public key. Example: xxxx-yyyy-zzzz.
        private_key (Union[Unset, str]): The gateway API private key. Example: xxxx-yyyy-zzzz.
        descriptor_name (Union[Unset, str]): The dynamic descriptor name. Must be composed by business name (3, 7 or 12
            chars), an asterisk (*) and the product name (18, 14 or 9 chars), for a total length of 22 chars. Example:
            company*productabc1234.
        descriptor_phone (Union[Unset, str]): The dynamic descriptor phone number. Must be 10-14 characters and can only
            contain numbers, dashes, parentheses and periods. Example: 3125551212.
        descriptor_url (Union[Unset, str]): The dynamic descriptor URL. Example: company.com.
    """

    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata"] = UNSET
    merchant_account_id: Union[Unset, str] = UNSET
    merchant_id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    descriptor_name: Union[Unset, str] = UNSET
    descriptor_phone: Union[Unset, str] = UNSET
    descriptor_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        merchant_account_id = self.merchant_account_id
        merchant_id = self.merchant_id
        public_key = self.public_key
        private_key = self.private_key
        descriptor_name = self.descriptor_name
        descriptor_phone = self.descriptor_phone
        descriptor_url = self.descriptor_url

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
        if merchant_account_id is not UNSET:
            field_dict["merchant_account_id"] = merchant_account_id
        if merchant_id is not UNSET:
            field_dict["merchant_id"] = merchant_id
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if descriptor_name is not UNSET:
            field_dict["descriptor_name"] = descriptor_name
        if descriptor_phone is not UNSET:
            field_dict["descriptor_phone"] = descriptor_phone
        if descriptor_url is not UNSET:
            field_dict["descriptor_url"] = descriptor_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_attributes_metadata import (
            PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataAttributesMetadata.from_dict(_metadata)

        merchant_account_id = d.pop("merchant_account_id", UNSET)

        merchant_id = d.pop("merchant_id", UNSET)

        public_key = d.pop("public_key", UNSET)

        private_key = d.pop("private_key", UNSET)

        descriptor_name = d.pop("descriptor_name", UNSET)

        descriptor_phone = d.pop("descriptor_phone", UNSET)

        descriptor_url = d.pop("descriptor_url", UNSET)

        patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_attributes = cls(
            name=name,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            merchant_account_id=merchant_account_id,
            merchant_id=merchant_id,
            public_key=public_key,
            private_key=private_key,
            descriptor_name=descriptor_name,
            descriptor_phone=descriptor_phone,
            descriptor_url=descriptor_url,
        )

        patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_attributes.additional_properties = d
        return patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_attributes

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
