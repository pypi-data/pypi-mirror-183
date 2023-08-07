from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_payment_create_data_attributes_metadata import StripePaymentCreateDataAttributesMetadata
    from ..models.stripe_payment_create_data_attributes_options import StripePaymentCreateDataAttributesOptions


T = TypeVar("T", bound="StripePaymentCreateDataAttributes")


@attr.s(auto_attribs=True)
class StripePaymentCreateDataAttributes:
    """
    Attributes:
        options (Union[Unset, StripePaymentCreateDataAttributesOptions]): Stripe payment options: 'setup_future_usage',
            'customer', and 'payment_method' Example: {'customer': 'cus_xxx', 'payment_method': 'pm_xxx'}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, StripePaymentCreateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    options: Union[Unset, "StripePaymentCreateDataAttributesOptions"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "StripePaymentCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_payment_create_data_attributes_metadata import StripePaymentCreateDataAttributesMetadata
        from ..models.stripe_payment_create_data_attributes_options import StripePaymentCreateDataAttributesOptions

        d = src_dict.copy()
        _options = d.pop("options", UNSET)
        options: Union[Unset, StripePaymentCreateDataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = StripePaymentCreateDataAttributesOptions.from_dict(_options)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StripePaymentCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StripePaymentCreateDataAttributesMetadata.from_dict(_metadata)

        stripe_payment_create_data_attributes = cls(
            options=options,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        stripe_payment_create_data_attributes.additional_properties = d
        return stripe_payment_create_data_attributes

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
