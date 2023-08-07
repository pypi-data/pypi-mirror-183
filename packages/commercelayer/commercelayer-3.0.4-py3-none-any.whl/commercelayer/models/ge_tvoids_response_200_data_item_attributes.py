from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tvoids_response_200_data_item_attributes_metadata import (
        GETvoidsResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETvoidsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETvoidsResponse200DataItemAttributes:
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
        metadata (Union[Unset, GETvoidsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
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
    metadata: Union[Unset, "GETvoidsResponse200DataItemAttributesMetadata"] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tvoids_response_200_data_item_attributes_metadata import (
            GETvoidsResponse200DataItemAttributesMetadata,
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
        metadata: Union[Unset, GETvoidsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETvoidsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tvoids_response_200_data_item_attributes = cls(
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
        )

        ge_tvoids_response_200_data_item_attributes.additional_properties = d
        return ge_tvoids_response_200_data_item_attributes

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
