from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tbraintree_gateways_response_200_data_item_attributes_metadata import (
        GETbraintreeGatewaysResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETbraintreeGatewaysResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETbraintreeGatewaysResponse200DataItemAttributes:
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
        metadata (Union[Unset, GETbraintreeGatewaysResponse200DataItemAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
        descriptor_name (Union[Unset, str]): The dynamic descriptor name. Must be composed by business name (3, 7 or 12
            chars), an asterisk (*) and the product name (18, 14 or 9 chars), for a total length of 22 chars. Example:
            company*productabc1234.
        descriptor_phone (Union[Unset, str]): The dynamic descriptor phone number. Must be 10-14 characters and can only
            contain numbers, dashes, parentheses and periods. Example: 3125551212.
        descriptor_url (Union[Unset, str]): The dynamic descriptor URL. Example: company.com.
        webhook_endpoint_url (Union[Unset, str]): The gateway webhook URL, generated automatically. Example:
            https://core.commercelayer.co/webhook_callbacks/braintree_gateways/xxxxx.
    """

    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETbraintreeGatewaysResponse200DataItemAttributesMetadata"] = UNSET
    descriptor_name: Union[Unset, str] = UNSET
    descriptor_phone: Union[Unset, str] = UNSET
    descriptor_url: Union[Unset, str] = UNSET
    webhook_endpoint_url: Union[Unset, str] = UNSET
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

        descriptor_name = self.descriptor_name
        descriptor_phone = self.descriptor_phone
        descriptor_url = self.descriptor_url
        webhook_endpoint_url = self.webhook_endpoint_url

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
        if descriptor_name is not UNSET:
            field_dict["descriptor_name"] = descriptor_name
        if descriptor_phone is not UNSET:
            field_dict["descriptor_phone"] = descriptor_phone
        if descriptor_url is not UNSET:
            field_dict["descriptor_url"] = descriptor_url
        if webhook_endpoint_url is not UNSET:
            field_dict["webhook_endpoint_url"] = webhook_endpoint_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tbraintree_gateways_response_200_data_item_attributes_metadata import (
            GETbraintreeGatewaysResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETbraintreeGatewaysResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETbraintreeGatewaysResponse200DataItemAttributesMetadata.from_dict(_metadata)

        descriptor_name = d.pop("descriptor_name", UNSET)

        descriptor_phone = d.pop("descriptor_phone", UNSET)

        descriptor_url = d.pop("descriptor_url", UNSET)

        webhook_endpoint_url = d.pop("webhook_endpoint_url", UNSET)

        ge_tbraintree_gateways_response_200_data_item_attributes = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            descriptor_name=descriptor_name,
            descriptor_phone=descriptor_phone,
            descriptor_url=descriptor_url,
            webhook_endpoint_url=webhook_endpoint_url,
        )

        ge_tbraintree_gateways_response_200_data_item_attributes.additional_properties = d
        return ge_tbraintree_gateways_response_200_data_item_attributes

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
