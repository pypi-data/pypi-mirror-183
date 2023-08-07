from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcustomer_password_resetscustomer_password_reset_id_response_200_data_attributes_metadata import (
        PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributes:
    """
    Attributes:
        customer_password (Union[Unset, str]): The customer new password. This will be accepted only if a valid
            '_reset_password_token' is sent with the request. Example: secret.
        reset_password_token (Union[Unset, str]): Send the 'reset_password_token' that you got on create when updating
            the customer password. Example: xhFfkmfybsLxzaAP6xcs.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata]):
            Set of key-value pairs that you can attach to the resource. This can be useful for storing additional
            information about the resource in a structured format. Example: {'foo': 'bar'}.
    """

    customer_password: Union[Unset, str] = UNSET
    reset_password_token: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[
        Unset, "PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_password = self.customer_password
        reset_password_token = self.reset_password_token
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_password is not UNSET:
            field_dict["customer_password"] = customer_password
        if reset_password_token is not UNSET:
            field_dict["_reset_password_token"] = reset_password_token
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hcustomer_password_resetscustomer_password_reset_id_response_200_data_attributes_metadata import (
            PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        customer_password = d.pop("customer_password", UNSET)

        reset_password_token = d.pop("_reset_password_token", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200DataAttributesMetadata.from_dict(
                _metadata
            )

        patc_hcustomer_password_resetscustomer_password_reset_id_response_200_data_attributes = cls(
            customer_password=customer_password,
            reset_password_token=reset_password_token,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hcustomer_password_resetscustomer_password_reset_id_response_200_data_attributes.additional_properties = d
        return patc_hcustomer_password_resetscustomer_password_reset_id_response_200_data_attributes

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
