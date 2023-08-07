from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcoupons_response_201_data_attributes_metadata import POSTcouponsResponse201DataAttributesMetadata


T = TypeVar("T", bound="POSTcouponsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTcouponsResponse201DataAttributes:
    """
    Attributes:
        code (str): The coupon code, that uniquely identifies the coupon within the promotion rule. Example:
            04371af2-70b3-48d7-8f4e-316b374224c3.
        usage_limit (int): The total number of times this coupon can be used. Example: 50.
        customer_single_use (Union[Unset, bool]): Indicates if the coupon can be used just once per customer.
        recipient_email (Union[Unset, str]): The email address of the associated recipient. When creating or updating a
            coupon, this is a shortcut to find or create the associated recipient by email. Example: john@example.com.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTcouponsResponse201DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    code: str
    usage_limit: int
    customer_single_use: Union[Unset, bool] = UNSET
    recipient_email: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTcouponsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        usage_limit = self.usage_limit
        customer_single_use = self.customer_single_use
        recipient_email = self.recipient_email
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "usage_limit": usage_limit,
            }
        )
        if customer_single_use is not UNSET:
            field_dict["customer_single_use"] = customer_single_use
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcoupons_response_201_data_attributes_metadata import (
            POSTcouponsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        code = d.pop("code")

        usage_limit = d.pop("usage_limit")

        customer_single_use = d.pop("customer_single_use", UNSET)

        recipient_email = d.pop("recipient_email", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTcouponsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTcouponsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tcoupons_response_201_data_attributes = cls(
            code=code,
            usage_limit=usage_limit,
            customer_single_use=customer_single_use,
            recipient_email=recipient_email,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tcoupons_response_201_data_attributes.additional_properties = d
        return pos_tcoupons_response_201_data_attributes

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
