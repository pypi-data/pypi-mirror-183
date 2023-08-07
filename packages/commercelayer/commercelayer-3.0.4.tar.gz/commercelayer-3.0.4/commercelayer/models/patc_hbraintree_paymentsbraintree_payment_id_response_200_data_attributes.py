from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes_metadata import (
        PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata,
    )
    from ..models.patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes_options import (
        PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions,
    )


T = TypeVar("T", bound="PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributes:
    """
    Attributes:
        payment_method_nonce (Union[Unset, str]): The Braintree payment method nonce. Sent by the Braintree JS SDK.
            Example: xxxx.yyyy.zzzz.
        payment_id (Union[Unset, str]): The Braintree payment ID used by local payment and sent by the Braintree JS SDK.
            Example: xxxx.yyyy.zzzz.
        local (Union[Unset, bool]): Indicates if the payment is local, in such case Braintree will trigger a webhook
            call passing the "payment_id" and "payment_method_nonce" in order to complete the transaction. Example: True.
        options (Union[Unset, PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions]): Braintree
            payment options: 'customer_id' and 'payment_method_token' Example: {'customer_id': '1234567890'}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata]): Set of key-
            value pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    payment_method_nonce: Union[Unset, str] = UNSET
    payment_id: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    options: Union[Unset, "PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method_nonce = self.payment_method_nonce
        payment_id = self.payment_id
        local = self.local
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
        if payment_method_nonce is not UNSET:
            field_dict["payment_method_nonce"] = payment_method_nonce
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id
        if local is not UNSET:
            field_dict["local"] = local
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
        from ..models.patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes_metadata import (
            PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata,
        )
        from ..models.patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes_options import (
            PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions,
        )

        d = src_dict.copy()
        payment_method_nonce = d.pop("payment_method_nonce", UNSET)

        payment_id = d.pop("payment_id", UNSET)

        local = d.pop("local", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesOptions.from_dict(_options)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHbraintreePaymentsbraintreePaymentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes = cls(
            payment_method_nonce=payment_method_nonce,
            payment_id=payment_id,
            local=local,
            options=options,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes.additional_properties = d
        return patc_hbraintree_paymentsbraintree_payment_id_response_200_data_attributes

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
