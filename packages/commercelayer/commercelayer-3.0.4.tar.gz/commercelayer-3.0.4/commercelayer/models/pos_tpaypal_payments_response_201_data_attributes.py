from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tpaypal_payments_response_201_data_attributes_metadata import (
        POSTpaypalPaymentsResponse201DataAttributesMetadata,
    )


T = TypeVar("T", bound="POSTpaypalPaymentsResponse201DataAttributes")


@attr.s(auto_attribs=True)
class POSTpaypalPaymentsResponse201DataAttributes:
    """
    Attributes:
        return_url (str): The URL where the payer is redirected after they approve the payment. Example:
            https://yourdomain.com/thankyou.
        cancel_url (str): The URL where the payer is redirected after they cancel the payment. Example:
            https://yourdomain.com/checkout/payment.
        note_to_payer (Union[Unset, str]): A free-form field that you can use to send a note to the payer on PayPal.
            Example: Thank you for shopping with us!.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, POSTpaypalPaymentsResponse201DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    return_url: str
    cancel_url: str
    note_to_payer: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "POSTpaypalPaymentsResponse201DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_url = self.return_url
        cancel_url = self.cancel_url
        note_to_payer = self.note_to_payer
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "return_url": return_url,
                "cancel_url": cancel_url,
            }
        )
        if note_to_payer is not UNSET:
            field_dict["note_to_payer"] = note_to_payer
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tpaypal_payments_response_201_data_attributes_metadata import (
            POSTpaypalPaymentsResponse201DataAttributesMetadata,
        )

        d = src_dict.copy()
        return_url = d.pop("return_url")

        cancel_url = d.pop("cancel_url")

        note_to_payer = d.pop("note_to_payer", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, POSTpaypalPaymentsResponse201DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = POSTpaypalPaymentsResponse201DataAttributesMetadata.from_dict(_metadata)

        pos_tpaypal_payments_response_201_data_attributes = cls(
            return_url=return_url,
            cancel_url=cancel_url,
            note_to_payer=note_to_payer,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        pos_tpaypal_payments_response_201_data_attributes.additional_properties = d
        return pos_tpaypal_payments_response_201_data_attributes

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
