from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstripe_payments_response_200_data_item_attributes_metadata import (
        GETstripePaymentsResponse200DataItemAttributesMetadata,
    )
    from ..models.ge_tstripe_payments_response_200_data_item_attributes_options import (
        GETstripePaymentsResponse200DataItemAttributesOptions,
    )
    from ..models.ge_tstripe_payments_response_200_data_item_attributes_payment_method import (
        GETstripePaymentsResponse200DataItemAttributesPaymentMethod,
    )


T = TypeVar("T", bound="GETstripePaymentsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETstripePaymentsResponse200DataItemAttributes:
    """
    Attributes:
        client_secret (Union[Unset, str]): The Stripe payment intent client secret. Required to create a charge through
            Stripe.js. Example: pi_1234XXX_secret_5678YYY.
        publishable_key (Union[Unset, str]): The Stripe publishable API key. Example: pk_live_xxxx-yyyy-zzzz.
        options (Union[Unset, GETstripePaymentsResponse200DataItemAttributesOptions]): Stripe payment options:
            'setup_future_usage', 'customer', and 'payment_method' Example: {'customer': 'cus_xxx', 'payment_method':
            'pm_xxx'}.
        payment_method (Union[Unset, GETstripePaymentsResponse200DataItemAttributesPaymentMethod]): Stripe
            'payment_method', set by webhook. Example: {'id': 'pm_xxx'}.
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
        metadata (Union[Unset, GETstripePaymentsResponse200DataItemAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    client_secret: Union[Unset, str] = UNSET
    publishable_key: Union[Unset, str] = UNSET
    options: Union[Unset, "GETstripePaymentsResponse200DataItemAttributesOptions"] = UNSET
    payment_method: Union[Unset, "GETstripePaymentsResponse200DataItemAttributesPaymentMethod"] = UNSET
    mismatched_amounts: Union[Unset, bool] = UNSET
    intent_amount_cents: Union[Unset, int] = UNSET
    intent_amount_float: Union[Unset, float] = UNSET
    formatted_intent_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETstripePaymentsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_secret = self.client_secret
        publishable_key = self.publishable_key
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        payment_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.to_dict()

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
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if publishable_key is not UNSET:
            field_dict["publishable_key"] = publishable_key
        if options is not UNSET:
            field_dict["options"] = options
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
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
        from ..models.ge_tstripe_payments_response_200_data_item_attributes_metadata import (
            GETstripePaymentsResponse200DataItemAttributesMetadata,
        )
        from ..models.ge_tstripe_payments_response_200_data_item_attributes_options import (
            GETstripePaymentsResponse200DataItemAttributesOptions,
        )
        from ..models.ge_tstripe_payments_response_200_data_item_attributes_payment_method import (
            GETstripePaymentsResponse200DataItemAttributesPaymentMethod,
        )

        d = src_dict.copy()
        client_secret = d.pop("client_secret", UNSET)

        publishable_key = d.pop("publishable_key", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, GETstripePaymentsResponse200DataItemAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = GETstripePaymentsResponse200DataItemAttributesOptions.from_dict(_options)

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, GETstripePaymentsResponse200DataItemAttributesPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = GETstripePaymentsResponse200DataItemAttributesPaymentMethod.from_dict(_payment_method)

        mismatched_amounts = d.pop("mismatched_amounts", UNSET)

        intent_amount_cents = d.pop("intent_amount_cents", UNSET)

        intent_amount_float = d.pop("intent_amount_float", UNSET)

        formatted_intent_amount = d.pop("formatted_intent_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETstripePaymentsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETstripePaymentsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tstripe_payments_response_200_data_item_attributes = cls(
            client_secret=client_secret,
            publishable_key=publishable_key,
            options=options,
            payment_method=payment_method,
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

        ge_tstripe_payments_response_200_data_item_attributes.additional_properties = d
        return ge_tstripe_payments_response_200_data_item_attributes

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
