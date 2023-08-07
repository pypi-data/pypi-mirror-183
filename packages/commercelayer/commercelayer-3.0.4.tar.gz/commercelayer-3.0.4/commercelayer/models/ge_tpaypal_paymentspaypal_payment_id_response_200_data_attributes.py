from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpaypal_paymentspaypal_payment_id_response_200_data_attributes_metadata import (
        GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETpaypalPaymentspaypalPaymentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETpaypalPaymentspaypalPaymentIdResponse200DataAttributes:
    """
    Attributes:
        return_url (Union[Unset, str]): The URL where the payer is redirected after they approve the payment. Example:
            https://yourdomain.com/thankyou.
        cancel_url (Union[Unset, str]): The URL where the payer is redirected after they cancel the payment. Example:
            https://yourdomain.com/checkout/payment.
        note_to_payer (Union[Unset, str]): A free-form field that you can use to send a note to the payer on PayPal.
            Example: Thank you for shopping with us!.
        paypal_payer_id (Union[Unset, str]): The id of the payer that PayPal passes in the return_url. Example:
            ABCDEFGHG123456.
        name (Union[Unset, str]): The PayPal payer id (if present) Example: ABCDEFGHG123456.
        paypal_id (Union[Unset, str]): The id of the PayPal payment object. Example: 1234567890.
        status (Union[Unset, str]): The PayPal payment status. One of 'created' (default) or 'approved'. Example:
            created.
        approval_url (Union[Unset, str]): The URL the customer should be redirected to approve the payment. Example:
            https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-1234567890ABCDEFGHG.
        mismatched_amounts (Union[Unset, bool]): Indicates if the order current amount differs form the one of the
            created payment intent.
        intent_amount_cents (Union[Unset, int]): The amount of the associated payment intent, in cents. Example: 1000.
        intent_amount_float (Union[Unset, float]): The amount of the associated payment intent, float. Example: 10.0.
        formatted_intent_amount (Union[Unset, str]): The amount of the associated payment intent, formatted. Example:
            €10,00.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    return_url: Union[Unset, str] = UNSET
    cancel_url: Union[Unset, str] = UNSET
    note_to_payer: Union[Unset, str] = UNSET
    paypal_payer_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    paypal_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    approval_url: Union[Unset, str] = UNSET
    mismatched_amounts: Union[Unset, bool] = UNSET
    intent_amount_cents: Union[Unset, int] = UNSET
    intent_amount_float: Union[Unset, float] = UNSET
    formatted_intent_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_url = self.return_url
        cancel_url = self.cancel_url
        note_to_payer = self.note_to_payer
        paypal_payer_id = self.paypal_payer_id
        name = self.name
        paypal_id = self.paypal_id
        status = self.status
        approval_url = self.approval_url
        mismatched_amounts = self.mismatched_amounts
        intent_amount_cents = self.intent_amount_cents
        intent_amount_float = self.intent_amount_float
        formatted_intent_amount = self.formatted_intent_amount
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
        if return_url is not UNSET:
            field_dict["return_url"] = return_url
        if cancel_url is not UNSET:
            field_dict["cancel_url"] = cancel_url
        if note_to_payer is not UNSET:
            field_dict["note_to_payer"] = note_to_payer
        if paypal_payer_id is not UNSET:
            field_dict["paypal_payer_id"] = paypal_payer_id
        if name is not UNSET:
            field_dict["name"] = name
        if paypal_id is not UNSET:
            field_dict["paypal_id"] = paypal_id
        if status is not UNSET:
            field_dict["status"] = status
        if approval_url is not UNSET:
            field_dict["approval_url"] = approval_url
        if mismatched_amounts is not UNSET:
            field_dict["mismatched_amounts"] = mismatched_amounts
        if intent_amount_cents is not UNSET:
            field_dict["intent_amount_cents"] = intent_amount_cents
        if intent_amount_float is not UNSET:
            field_dict["intent_amount_float"] = intent_amount_float
        if formatted_intent_amount is not UNSET:
            field_dict["formatted_intent_amount"] = formatted_intent_amount
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
        from ..models.ge_tpaypal_paymentspaypal_payment_id_response_200_data_attributes_metadata import (
            GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        return_url = d.pop("return_url", UNSET)

        cancel_url = d.pop("cancel_url", UNSET)

        note_to_payer = d.pop("note_to_payer", UNSET)

        paypal_payer_id = d.pop("paypal_payer_id", UNSET)

        name = d.pop("name", UNSET)

        paypal_id = d.pop("paypal_id", UNSET)

        status = d.pop("status", UNSET)

        approval_url = d.pop("approval_url", UNSET)

        mismatched_amounts = d.pop("mismatched_amounts", UNSET)

        intent_amount_cents = d.pop("intent_amount_cents", UNSET)

        intent_amount_float = d.pop("intent_amount_float", UNSET)

        formatted_intent_amount = d.pop("formatted_intent_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETpaypalPaymentspaypalPaymentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tpaypal_paymentspaypal_payment_id_response_200_data_attributes = cls(
            return_url=return_url,
            cancel_url=cancel_url,
            note_to_payer=note_to_payer,
            paypal_payer_id=paypal_payer_id,
            name=name,
            paypal_id=paypal_id,
            status=status,
            approval_url=approval_url,
            mismatched_amounts=mismatched_amounts,
            intent_amount_cents=intent_amount_cents,
            intent_amount_float=intent_amount_float,
            formatted_intent_amount=formatted_intent_amount,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tpaypal_paymentspaypal_payment_id_response_200_data_attributes.additional_properties = d
        return ge_tpaypal_paymentspaypal_payment_id_response_200_data_attributes

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
