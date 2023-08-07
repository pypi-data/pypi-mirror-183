from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpayment_methodspayment_method_id_response_200_data_attributes_metadata import (
        PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHpaymentMethodspaymentMethodIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHpaymentMethodspaymentMethodIdResponse200DataAttributes:
    """
    Attributes:
        payment_source_type (Union[Unset, str]): The payment source type, can be one of: 'AdyenPayment',
            'BraintreePayment', 'CheckoutComPayment', 'CreditCard', 'ExternalPayment', 'KlarnaPayment', 'PaypalPayment',
            'StripePayment', or 'WireTransfer'. Example: CreditCard.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        moto (Union[Unset, bool]): Send this attribute if you want to mark the payment as MOTO, must be supported by
            payment gateway.
        disable (Union[Unset, bool]): Send this attribute if you want to mark the payment method as disabled. Example:
            True.
        enable (Union[Unset, bool]): Send this attribute if you want to mark the payment method as enabled. Example:
            True.
        price_amount_cents (Union[Unset, int]): The payment method's price, in cents
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    payment_source_type: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    moto: Union[Unset, bool] = UNSET
    disable: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_source_type = self.payment_source_type
        currency_code = self.currency_code
        moto = self.moto
        disable = self.disable
        enable = self.enable
        price_amount_cents = self.price_amount_cents
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_source_type is not UNSET:
            field_dict["payment_source_type"] = payment_source_type
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if moto is not UNSET:
            field_dict["moto"] = moto
        if disable is not UNSET:
            field_dict["_disable"] = disable
        if enable is not UNSET:
            field_dict["_enable"] = enable
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hpayment_methodspayment_method_id_response_200_data_attributes_metadata import (
            PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        payment_source_type = d.pop("payment_source_type", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        moto = d.pop("moto", UNSET)

        disable = d.pop("_disable", UNSET)

        enable = d.pop("_enable", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hpayment_methodspayment_method_id_response_200_data_attributes = cls(
            payment_source_type=payment_source_type,
            currency_code=currency_code,
            moto=moto,
            disable=disable,
            enable=enable,
            price_amount_cents=price_amount_cents,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hpayment_methodspayment_method_id_response_200_data_attributes.additional_properties = d
        return patc_hpayment_methodspayment_method_id_response_200_data_attributes

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
