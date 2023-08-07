from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpayment_methodspayment_method_id_response_200_data_attributes_metadata import (
        GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETpaymentMethodspaymentMethodIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETpaymentMethodspaymentMethodIdResponse200DataAttributes:
    """
    Attributes:
        payment_source_type (Union[Unset, str]): The payment source type, can be one of: 'AdyenPayment',
            'BraintreePayment', 'CheckoutComPayment', 'CreditCard', 'ExternalPayment', 'KlarnaPayment', 'PaypalPayment',
            'StripePayment', or 'WireTransfer'. Example: CreditCard.
        name (Union[Unset, str]): Payment source type, titleized Example: Credit Card.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        moto (Union[Unset, bool]): Send this attribute if you want to mark the payment as MOTO, must be supported by
            payment gateway.
        disabled_at (Union[Unset, str]): Time at which the payment method was disabled. Example:
            2018-01-01T12:00:00.000Z.
        price_amount_cents (Union[Unset, int]): The payment method's price, in cents
        price_amount_float (Union[Unset, float]): The payment method's price, float
        formatted_price_amount (Union[Unset, str]): The payment method's price, formatted Example: €0,00.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    payment_source_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    moto: Union[Unset, bool] = UNSET
    disabled_at: Union[Unset, str] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    price_amount_float: Union[Unset, float] = UNSET
    formatted_price_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_source_type = self.payment_source_type
        name = self.name
        currency_code = self.currency_code
        moto = self.moto
        disabled_at = self.disabled_at
        price_amount_cents = self.price_amount_cents
        price_amount_float = self.price_amount_float
        formatted_price_amount = self.formatted_price_amount
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
        if payment_source_type is not UNSET:
            field_dict["payment_source_type"] = payment_source_type
        if name is not UNSET:
            field_dict["name"] = name
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if moto is not UNSET:
            field_dict["moto"] = moto
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if price_amount_float is not UNSET:
            field_dict["price_amount_float"] = price_amount_float
        if formatted_price_amount is not UNSET:
            field_dict["formatted_price_amount"] = formatted_price_amount
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
        from ..models.ge_tpayment_methodspayment_method_id_response_200_data_attributes_metadata import (
            GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        payment_source_type = d.pop("payment_source_type", UNSET)

        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        moto = d.pop("moto", UNSET)

        disabled_at = d.pop("disabled_at", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        price_amount_float = d.pop("price_amount_float", UNSET)

        formatted_price_amount = d.pop("formatted_price_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETpaymentMethodspaymentMethodIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tpayment_methodspayment_method_id_response_200_data_attributes = cls(
            payment_source_type=payment_source_type,
            name=name,
            currency_code=currency_code,
            moto=moto,
            disabled_at=disabled_at,
            price_amount_cents=price_amount_cents,
            price_amount_float=price_amount_float,
            formatted_price_amount=formatted_price_amount,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tpayment_methodspayment_method_id_response_200_data_attributes.additional_properties = d
        return ge_tpayment_methodspayment_method_id_response_200_data_attributes

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
