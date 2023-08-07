from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.klarna_payment_data_attributes_metadata import KlarnaPaymentDataAttributesMetadata
    from ..models.klarna_payment_data_attributes_payment_methods_item import (
        KlarnaPaymentDataAttributesPaymentMethodsItem,
    )


T = TypeVar("T", bound="KlarnaPaymentDataAttributes")


@attr.s(auto_attribs=True)
class KlarnaPaymentDataAttributes:
    """
    Attributes:
        session_id (Union[Unset, str]): The identifier of the payment session, useful to updated it. Example: xxxx-yyyy-
            zzzz.
        client_token (Union[Unset, str]): The public token linked to your API credential. Available upon session
            creation. Example: xxxx-yyyy-zzzz.
        payment_methods (Union[Unset, List['KlarnaPaymentDataAttributesPaymentMethodsItem']]): The merchant available
            payment methods for the assoiated order. Available upon session creation. Example: [{'foo': 'bar'}].
        auth_token (Union[Unset, str]): The token returned by a successful client authorization, mandatory to place the
            order. Example: xxxx-yyyy-zzzz.
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
        metadata (Union[Unset, KlarnaPaymentDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    session_id: Union[Unset, str] = UNSET
    client_token: Union[Unset, str] = UNSET
    payment_methods: Union[Unset, List["KlarnaPaymentDataAttributesPaymentMethodsItem"]] = UNSET
    auth_token: Union[Unset, str] = UNSET
    mismatched_amounts: Union[Unset, bool] = UNSET
    intent_amount_cents: Union[Unset, int] = UNSET
    intent_amount_float: Union[Unset, float] = UNSET
    formatted_intent_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "KlarnaPaymentDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id
        client_token = self.client_token
        payment_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item = payment_methods_item_data.to_dict()

                payment_methods.append(payment_methods_item)

        auth_token = self.auth_token
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
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if client_token is not UNSET:
            field_dict["client_token"] = client_token
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
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
        from ..models.klarna_payment_data_attributes_metadata import KlarnaPaymentDataAttributesMetadata
        from ..models.klarna_payment_data_attributes_payment_methods_item import (
            KlarnaPaymentDataAttributesPaymentMethodsItem,
        )

        d = src_dict.copy()
        session_id = d.pop("session_id", UNSET)

        client_token = d.pop("client_token", UNSET)

        payment_methods = []
        _payment_methods = d.pop("payment_methods", UNSET)
        for payment_methods_item_data in _payment_methods or []:
            payment_methods_item = KlarnaPaymentDataAttributesPaymentMethodsItem.from_dict(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        auth_token = d.pop("auth_token", UNSET)

        mismatched_amounts = d.pop("mismatched_amounts", UNSET)

        intent_amount_cents = d.pop("intent_amount_cents", UNSET)

        intent_amount_float = d.pop("intent_amount_float", UNSET)

        formatted_intent_amount = d.pop("formatted_intent_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, KlarnaPaymentDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KlarnaPaymentDataAttributesMetadata.from_dict(_metadata)

        klarna_payment_data_attributes = cls(
            session_id=session_id,
            client_token=client_token,
            payment_methods=payment_methods,
            auth_token=auth_token,
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

        klarna_payment_data_attributes.additional_properties = d
        return klarna_payment_data_attributes

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
