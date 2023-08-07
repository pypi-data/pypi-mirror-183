from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tauthorizations_response_200_data_item_attributes_metadata import (
        GETauthorizationsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETauthorizationsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETauthorizationsResponse200DataItemAttributes:
    """
    Attributes:
        number (Union[Unset, str]): The transaction number, auto generated Example: 42/T/001.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            inherited from the associated order. Example: EUR.
        amount_cents (Union[Unset, int]): The transaction amount, in cents. Example: 1500.
        amount_float (Union[Unset, float]): The transaction amount, float. Example: 15.0.
        formatted_amount (Union[Unset, str]): The transaction amount, formatted. Example: €15,00.
        succeeded (Union[Unset, bool]): Indicates if the transaction is successful
        message (Union[Unset, str]): The message returned by the payment gateway Example: Accepted.
        error_code (Union[Unset, str]): The error code, if any, returned by the payment gateway Example: 00001.
        error_detail (Union[Unset, str]): The error detail, if any, returned by the payment gateway Example: Already
            settled.
        token (Union[Unset, str]): The token identifying the transaction, returned by the payment gateway Example: xxxx-
            yyyy-zzzz.
        gateway_transaction_id (Union[Unset, str]): The ID identifying the transaction, returned by the payment gateway
            Example: xxxx-yyyy-zzzz.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETauthorizationsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
        cvv_code (Union[Unset, str]): The CVV code returned by the payment gateway Example: 000.
        cvv_message (Union[Unset, str]): The CVV message returned by the payment gateway Example: validated.
        avs_code (Union[Unset, str]): The AVS code returned by the payment gateway Example: 000.
        avs_message (Union[Unset, str]): The AVS message returned by the payment gateway Example: validated.
        fraud_review (Union[Unset, str]): The fraud review message, if any, returned by the payment gateway Example:
            passed.
        capture_amount_cents (Union[Unset, int]): The amount to be captured, in cents. Example: 500.
        capture_amount_float (Union[Unset, float]): The amount to be captured, float. Example: 5.0.
        formatted_capture_amount (Union[Unset, str]): The amount to be captured, formatted. Example: €5,00.
        capture_balance_cents (Union[Unset, int]): The balance to be captured, in cents. Example: 1000.
        capture_balance_float (Union[Unset, float]): The balance to be captured, float. Example: 10.0.
        formatted_capture_balance (Union[Unset, str]): The balance to be captured, formatted. Example: €10,00.
        void_balance_cents (Union[Unset, int]): The balance to be voided, in cents. Example: 1500.
        void_balance_float (Union[Unset, float]): The balance to be voided, float. Example: 15.0.
        formatted_void_balance (Union[Unset, str]): The balance to be voided, formatted. Example: €15,00.
    """

    number: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    amount_cents: Union[Unset, int] = UNSET
    amount_float: Union[Unset, float] = UNSET
    formatted_amount: Union[Unset, str] = UNSET
    succeeded: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    error_code: Union[Unset, str] = UNSET
    error_detail: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    gateway_transaction_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETauthorizationsResponse200DataItemAttributesMetadata"] = UNSET
    cvv_code: Union[Unset, str] = UNSET
    cvv_message: Union[Unset, str] = UNSET
    avs_code: Union[Unset, str] = UNSET
    avs_message: Union[Unset, str] = UNSET
    fraud_review: Union[Unset, str] = UNSET
    capture_amount_cents: Union[Unset, int] = UNSET
    capture_amount_float: Union[Unset, float] = UNSET
    formatted_capture_amount: Union[Unset, str] = UNSET
    capture_balance_cents: Union[Unset, int] = UNSET
    capture_balance_float: Union[Unset, float] = UNSET
    formatted_capture_balance: Union[Unset, str] = UNSET
    void_balance_cents: Union[Unset, int] = UNSET
    void_balance_float: Union[Unset, float] = UNSET
    formatted_void_balance: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        currency_code = self.currency_code
        amount_cents = self.amount_cents
        amount_float = self.amount_float
        formatted_amount = self.formatted_amount
        succeeded = self.succeeded
        message = self.message
        error_code = self.error_code
        error_detail = self.error_detail
        token = self.token
        gateway_transaction_id = self.gateway_transaction_id
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        cvv_code = self.cvv_code
        cvv_message = self.cvv_message
        avs_code = self.avs_code
        avs_message = self.avs_message
        fraud_review = self.fraud_review
        capture_amount_cents = self.capture_amount_cents
        capture_amount_float = self.capture_amount_float
        formatted_capture_amount = self.formatted_capture_amount
        capture_balance_cents = self.capture_balance_cents
        capture_balance_float = self.capture_balance_float
        formatted_capture_balance = self.formatted_capture_balance
        void_balance_cents = self.void_balance_cents
        void_balance_float = self.void_balance_float
        formatted_void_balance = self.formatted_void_balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if amount_float is not UNSET:
            field_dict["amount_float"] = amount_float
        if formatted_amount is not UNSET:
            field_dict["formatted_amount"] = formatted_amount
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if message is not UNSET:
            field_dict["message"] = message
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_detail is not UNSET:
            field_dict["error_detail"] = error_detail
        if token is not UNSET:
            field_dict["token"] = token
        if gateway_transaction_id is not UNSET:
            field_dict["gateway_transaction_id"] = gateway_transaction_id
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
        if cvv_code is not UNSET:
            field_dict["cvv_code"] = cvv_code
        if cvv_message is not UNSET:
            field_dict["cvv_message"] = cvv_message
        if avs_code is not UNSET:
            field_dict["avs_code"] = avs_code
        if avs_message is not UNSET:
            field_dict["avs_message"] = avs_message
        if fraud_review is not UNSET:
            field_dict["fraud_review"] = fraud_review
        if capture_amount_cents is not UNSET:
            field_dict["capture_amount_cents"] = capture_amount_cents
        if capture_amount_float is not UNSET:
            field_dict["capture_amount_float"] = capture_amount_float
        if formatted_capture_amount is not UNSET:
            field_dict["formatted_capture_amount"] = formatted_capture_amount
        if capture_balance_cents is not UNSET:
            field_dict["capture_balance_cents"] = capture_balance_cents
        if capture_balance_float is not UNSET:
            field_dict["capture_balance_float"] = capture_balance_float
        if formatted_capture_balance is not UNSET:
            field_dict["formatted_capture_balance"] = formatted_capture_balance
        if void_balance_cents is not UNSET:
            field_dict["void_balance_cents"] = void_balance_cents
        if void_balance_float is not UNSET:
            field_dict["void_balance_float"] = void_balance_float
        if formatted_void_balance is not UNSET:
            field_dict["formatted_void_balance"] = formatted_void_balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tauthorizations_response_200_data_item_attributes_metadata import (
            GETauthorizationsResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        amount_cents = d.pop("amount_cents", UNSET)

        amount_float = d.pop("amount_float", UNSET)

        formatted_amount = d.pop("formatted_amount", UNSET)

        succeeded = d.pop("succeeded", UNSET)

        message = d.pop("message", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_detail = d.pop("error_detail", UNSET)

        token = d.pop("token", UNSET)

        gateway_transaction_id = d.pop("gateway_transaction_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETauthorizationsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETauthorizationsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        cvv_code = d.pop("cvv_code", UNSET)

        cvv_message = d.pop("cvv_message", UNSET)

        avs_code = d.pop("avs_code", UNSET)

        avs_message = d.pop("avs_message", UNSET)

        fraud_review = d.pop("fraud_review", UNSET)

        capture_amount_cents = d.pop("capture_amount_cents", UNSET)

        capture_amount_float = d.pop("capture_amount_float", UNSET)

        formatted_capture_amount = d.pop("formatted_capture_amount", UNSET)

        capture_balance_cents = d.pop("capture_balance_cents", UNSET)

        capture_balance_float = d.pop("capture_balance_float", UNSET)

        formatted_capture_balance = d.pop("formatted_capture_balance", UNSET)

        void_balance_cents = d.pop("void_balance_cents", UNSET)

        void_balance_float = d.pop("void_balance_float", UNSET)

        formatted_void_balance = d.pop("formatted_void_balance", UNSET)

        ge_tauthorizations_response_200_data_item_attributes = cls(
            number=number,
            currency_code=currency_code,
            amount_cents=amount_cents,
            amount_float=amount_float,
            formatted_amount=formatted_amount,
            succeeded=succeeded,
            message=message,
            error_code=error_code,
            error_detail=error_detail,
            token=token,
            gateway_transaction_id=gateway_transaction_id,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            cvv_code=cvv_code,
            cvv_message=cvv_message,
            avs_code=avs_code,
            avs_message=avs_message,
            fraud_review=fraud_review,
            capture_amount_cents=capture_amount_cents,
            capture_amount_float=capture_amount_float,
            formatted_capture_amount=formatted_capture_amount,
            capture_balance_cents=capture_balance_cents,
            capture_balance_float=capture_balance_float,
            formatted_capture_balance=formatted_capture_balance,
            void_balance_cents=void_balance_cents,
            void_balance_float=void_balance_float,
            formatted_void_balance=formatted_void_balance,
        )

        ge_tauthorizations_response_200_data_item_attributes.additional_properties = d
        return ge_tauthorizations_response_200_data_item_attributes

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
