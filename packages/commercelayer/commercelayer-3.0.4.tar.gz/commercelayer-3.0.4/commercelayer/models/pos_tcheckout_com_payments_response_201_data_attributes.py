from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcheckout_com_payments_response_201_data_attributes_metadata import (
        POSTcheckoutComPaymentsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTcheckoutComPaymentsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTcheckoutComPaymentsResponse201DataAttributes:
    """
    Attributes:
        payment_type (str): The payment source type. Example: token.
        token (str): The Checkout.com card or digital wallet token. Example: tok_4gzeau5o2uqubbk6fufs3m7p54.
        session_id (Union[Unset, str]): A payment session ID used to obtain the details. Example:
            sid_y3oqhf46pyzuxjbcn2giaqnb44.
        success_url (Union[Unset, str]): The URL to redirect your customer upon 3DS succeeded authentication. Example:
            http://commercelayer.dev/checkout_com/success.
        failure_url (Union[Unset, str]): The URL to redirect your customer upon 3DS failed authentication. Example:
            http://commercelayer.dev/checkout_com/failure.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTcheckoutComPaymentsResponse201DataAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    payment_type: str
    token: str
    session_id: Union[Unset, str] = UNSET
    success_url: Union[Unset, str] = UNSET
    failure_url: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTcheckoutComPaymentsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_type = self.payment_type
        token = self.token
        session_id = self.session_id
        success_url = self.success_url
        failure_url = self.failure_url
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_type": payment_type,
                "token": token,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if failure_url is not UNSET:
            field_dict["failure_url"] = failure_url
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcheckout_com_payments_response_201_data_attributes_metadata import (
            POSTcheckoutComPaymentsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        payment_type = d.pop("payment_type")

        token = d.pop("token")

        session_id = d.pop("session_id", UNSET)

        success_url = d.pop("success_url", UNSET)

        failure_url = d.pop("failure_url", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTcheckoutComPaymentsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTcheckoutComPaymentsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tcheckout_com_payments_response_201_data_attributes = cls(
            payment_type=payment_type,
            token=token,
            session_id=session_id,
            success_url=success_url,
            failure_url=failure_url,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tcheckout_com_payments_response_201_data_attributes.additional_properties = d
        return pos_tcheckout_com_payments_response_201_data_attributes

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
