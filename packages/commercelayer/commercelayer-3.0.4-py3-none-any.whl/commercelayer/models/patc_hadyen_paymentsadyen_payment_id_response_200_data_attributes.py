from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_metadata import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata,
    )
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_data import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData,
    )
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_details import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails,
    )
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_response import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse,
    )


T = TypeVar("T", bound="PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributes:
    """
    Attributes:
        payment_request_data (Union[Unset,
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData]): The Adyen payment request data,
            collected by client. Example: {'foo': 'bar'}.
        payment_request_details (Union[Unset,
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails]): The Adyen additional details
            request data, collected by client. Example: {'foo': 'bar'}.
        payment_response (Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse]): The
            Adyen payment response, used by client (includes 'resultCode' and 'action'). Example: {'foo': 'bar'}.
        details (Union[Unset, bool]): Send this attribute if you want to send additional details the payment request.
            Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    payment_request_data: Union[
        Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData"
    ] = UNSET
    payment_request_details: Union[
        Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails"
    ] = UNSET
    payment_response: Union[Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse"] = UNSET
    details: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_request_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_request_data, Unset):
            payment_request_data = self.payment_request_data.to_dict()

        payment_request_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_request_details, Unset):
            payment_request_details = self.payment_request_details.to_dict()

        payment_response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_response, Unset):
            payment_response = self.payment_response.to_dict()

        details = self.details
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_request_data is not UNSET:
            field_dict["payment_request_data"] = payment_request_data
        if payment_request_details is not UNSET:
            field_dict["payment_request_details"] = payment_request_details
        if payment_response is not UNSET:
            field_dict["payment_response"] = payment_response
        if details is not UNSET:
            field_dict["_details"] = details
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_metadata import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata,
        )
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_data import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData,
        )
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_details import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails,
        )
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_response import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse,
        )

        d = src_dict.copy()
        _payment_request_data = d.pop("payment_request_data", UNSET)
        payment_request_data: Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData]
        if isinstance(_payment_request_data, Unset):
            payment_request_data = UNSET
        else:
            payment_request_data = (
                PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData.from_dict(
                    _payment_request_data
                )
            )

        _payment_request_details = d.pop("payment_request_details", UNSET)
        payment_request_details: Union[
            Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails
        ]
        if isinstance(_payment_request_details, Unset):
            payment_request_details = UNSET
        else:
            payment_request_details = (
                PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails.from_dict(
                    _payment_request_details
                )
            )

        _payment_response = d.pop("payment_response", UNSET)
        payment_response: Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse.from_dict(
                _payment_response
            )

        details = d.pop("_details", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes = cls(
            payment_request_data=payment_request_data,
            payment_request_details=payment_request_details,
            payment_response=payment_response,
            details=details,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes.additional_properties = d
        return patc_hadyen_paymentsadyen_payment_id_response_200_data_attributes

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
