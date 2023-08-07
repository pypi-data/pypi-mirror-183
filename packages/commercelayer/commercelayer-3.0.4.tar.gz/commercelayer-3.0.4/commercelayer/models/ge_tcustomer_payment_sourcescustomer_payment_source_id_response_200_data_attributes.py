from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_attributes_metadata import (
        GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Returns the associated payment source's name Example: XXXX-XXXX-XXXX-1111.
        customer_token (Union[Unset, str]): Returns the customer gateway token stored in the gateway Example:
            cus_xxxyyyzzz.
        payment_source_token (Union[Unset, str]): Returns the payment source token stored in the gateway Example:
            pm_xxxyyyzzz.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata]): Set
            of key-value pairs that you can attach to the resource. This can be useful for storing additional information
            about the resource in a structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    customer_token: Union[Unset, str] = UNSET
    payment_source_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        customer_token = self.customer_token
        payment_source_token = self.payment_source_token
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
        if customer_token is not UNSET:
            field_dict["customer_token"] = customer_token
        if payment_source_token is not UNSET:
            field_dict["payment_source_token"] = payment_source_token
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
        from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_attributes_metadata import (
            GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        customer_token = d.pop("customer_token", UNSET)

        payment_source_token = d.pop("payment_source_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataAttributesMetadata.from_dict(
                _metadata
            )

        ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_attributes = cls(
            name=name,
            customer_token=customer_token,
            payment_source_token=payment_source_token,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_attributes.additional_properties = d
        return ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_attributes

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
