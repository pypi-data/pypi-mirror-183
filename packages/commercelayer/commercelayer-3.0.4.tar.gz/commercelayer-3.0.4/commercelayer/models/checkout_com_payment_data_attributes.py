from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_com_payment_data_attributes_metadata import CheckoutComPaymentDataAttributesMetadata
    from ..models.checkout_com_payment_data_attributes_payment_response import (
        CheckoutComPaymentDataAttributesPaymentResponse,
    )


T = TypeVar("T", bound="CheckoutComPaymentDataAttributes")


@attr.s(auto_attribs=True)
class CheckoutComPaymentDataAttributes:
    """
    Attributes:
        public_key (Union[Unset, str]): The Checkout.com publishable API key. Example: pk_test_xxxx-yyyy-zzzz.
        payment_type (Union[Unset, str]): The payment source type. Example: token.
        token (Union[Unset, str]): The Checkout.com card or digital wallet token. Example:
            tok_4gzeau5o2uqubbk6fufs3m7p54.
        session_id (Union[Unset, str]): A payment session ID used to obtain the details. Example:
            sid_y3oqhf46pyzuxjbcn2giaqnb44.
        success_url (Union[Unset, str]): The URL to redirect your customer upon 3DS succeeded authentication. Example:
            http://commercelayer.dev/checkout_com/success.
        failure_url (Union[Unset, str]): The URL to redirect your customer upon 3DS failed authentication. Example:
            http://commercelayer.dev/checkout_com/failure.
        source_id (Union[Unset, str]): The payment source identifier that can be used for subsequent payments. Example:
            src_nwd3m4in3hkuddfpjsaevunhdy.
        customer_token (Union[Unset, str]): The customer's unique identifier. This can be passed as a source when making
            a payment. Example: cus_udst2tfldj6upmye2reztkmm4i.
        redirect_uri (Union[Unset, str]): The URI that the customer should be redirected to in order to complete the
            payment. Example: https://api.checkout.com/3ds/pay_mbabizu24mvu3mela5njyhpit4.
        payment_response (Union[Unset, CheckoutComPaymentDataAttributesPaymentResponse]): The Checkout.com payment
            response, used to fetch internal data. Example: {'foo': 'bar'}.
        mismatched_amounts (Union[Unset, bool]): Indicates if the order current amount differs form the one of the
            associated authorization.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, CheckoutComPaymentDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    public_key: Union[Unset, str] = UNSET
    payment_type: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    success_url: Union[Unset, str] = UNSET
    failure_url: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    customer_token: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    payment_response: Union[Unset, "CheckoutComPaymentDataAttributesPaymentResponse"] = UNSET
    mismatched_amounts: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CheckoutComPaymentDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_key = self.public_key
        payment_type = self.payment_type
        token = self.token
        session_id = self.session_id
        success_url = self.success_url
        failure_url = self.failure_url
        source_id = self.source_id
        customer_token = self.customer_token
        redirect_uri = self.redirect_uri
        payment_response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_response, Unset):
            payment_response = self.payment_response.to_dict()

        mismatched_amounts = self.mismatched_amounts
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
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if token is not UNSET:
            field_dict["token"] = token
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if failure_url is not UNSET:
            field_dict["failure_url"] = failure_url
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if customer_token is not UNSET:
            field_dict["customer_token"] = customer_token
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if payment_response is not UNSET:
            field_dict["payment_response"] = payment_response
        if mismatched_amounts is not UNSET:
            field_dict["mismatched_amounts"] = mismatched_amounts
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
        from ..models.checkout_com_payment_data_attributes_metadata import CheckoutComPaymentDataAttributesMetadata
        from ..models.checkout_com_payment_data_attributes_payment_response import (
            CheckoutComPaymentDataAttributesPaymentResponse,
        )

        d = src_dict.copy()
        public_key = d.pop("public_key", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        token = d.pop("token", UNSET)

        session_id = d.pop("session_id", UNSET)

        success_url = d.pop("success_url", UNSET)

        failure_url = d.pop("failure_url", UNSET)

        source_id = d.pop("source_id", UNSET)

        customer_token = d.pop("customer_token", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        _payment_response = d.pop("payment_response", UNSET)
        payment_response: Union[Unset, CheckoutComPaymentDataAttributesPaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = CheckoutComPaymentDataAttributesPaymentResponse.from_dict(_payment_response)

        mismatched_amounts = d.pop("mismatched_amounts", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CheckoutComPaymentDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CheckoutComPaymentDataAttributesMetadata.from_dict(_metadata)

        checkout_com_payment_data_attributes = cls(
            public_key=public_key,
            payment_type=payment_type,
            token=token,
            session_id=session_id,
            success_url=success_url,
            failure_url=failure_url,
            source_id=source_id,
            customer_token=customer_token,
            redirect_uri=redirect_uri,
            payment_response=payment_response,
            mismatched_amounts=mismatched_amounts,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        checkout_com_payment_data_attributes.additional_properties = d
        return checkout_com_payment_data_attributes

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
