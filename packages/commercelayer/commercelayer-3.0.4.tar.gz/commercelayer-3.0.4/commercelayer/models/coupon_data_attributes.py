from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coupon_data_attributes_metadata import CouponDataAttributesMetadata


T = TypeVar("T", bound="CouponDataAttributes")


@attr.s(auto_attribs=True)
class CouponDataAttributes:
    """
    Attributes:
        code (Union[Unset, str]): The coupon code, that uniquely identifies the coupon within the promotion rule.
            Example: 04371af2-70b3-48d7-8f4e-316b374224c3.
        customer_single_use (Union[Unset, bool]): Indicates if the coupon can be used just once per customer.
        usage_limit (Union[Unset, int]): The total number of times this coupon can be used. Example: 50.
        usage_count (Union[Unset, int]): The number of times this coupon has been used. Example: 20.
        recipient_email (Union[Unset, str]): The email address of the associated recipient. When creating or updating a
            coupon, this is a shortcut to find or create the associated recipient by email. Example: john@example.com.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, CouponDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    code: Union[Unset, str] = UNSET
    customer_single_use: Union[Unset, bool] = UNSET
    usage_limit: Union[Unset, int] = UNSET
    usage_count: Union[Unset, int] = UNSET
    recipient_email: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CouponDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        customer_single_use = self.customer_single_use
        usage_limit = self.usage_limit
        usage_count = self.usage_count
        recipient_email = self.recipient_email
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
        if code is not UNSET:
            field_dict["code"] = code
        if customer_single_use is not UNSET:
            field_dict["customer_single_use"] = customer_single_use
        if usage_limit is not UNSET:
            field_dict["usage_limit"] = usage_limit
        if usage_count is not UNSET:
            field_dict["usage_count"] = usage_count
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
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
        from ..models.coupon_data_attributes_metadata import CouponDataAttributesMetadata

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        customer_single_use = d.pop("customer_single_use", UNSET)

        usage_limit = d.pop("usage_limit", UNSET)

        usage_count = d.pop("usage_count", UNSET)

        recipient_email = d.pop("recipient_email", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CouponDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CouponDataAttributesMetadata.from_dict(_metadata)

        coupon_data_attributes = cls(
            code=code,
            customer_single_use=customer_single_use,
            usage_limit=usage_limit,
            usage_count=usage_count,
            recipient_email=recipient_email,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        coupon_data_attributes.additional_properties = d
        return coupon_data_attributes

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
