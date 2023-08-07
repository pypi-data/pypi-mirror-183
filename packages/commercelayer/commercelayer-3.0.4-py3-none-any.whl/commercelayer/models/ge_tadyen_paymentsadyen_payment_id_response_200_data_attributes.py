from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_metadata import (
        GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata,
    )
    from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_methods import (
        GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods,
    )
    from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_data import (
        GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData,
    )
    from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_details import (
        GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails,
    )
    from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_response import (
        GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse,
    )


T = TypeVar("T", bound="GETadyenPaymentsadyenPaymentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETadyenPaymentsadyenPaymentIdResponse200DataAttributes:
    """
    Attributes:
        public_key (Union[Unset, str]): The public key linked to your API credential. Example: xxxx-yyyy-zzzz.
        payment_methods (Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods]): The
            merchant available payment methods for the assoiated order (i.e. country and amount). Required by the Adyen JS
            SDK. Example: {'foo': 'bar'}.
        payment_request_data (Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData]):
            The Adyen payment request data, collected by client. Example: {'foo': 'bar'}.
        payment_request_details (Union[Unset,
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails]): The Adyen additional details
            request data, collected by client. Example: {'foo': 'bar'}.
        payment_response (Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse]): The
            Adyen payment response, used by client (includes 'resultCode' and 'action'). Example: {'foo': 'bar'}.
        mismatched_amounts (Union[Unset, bool]): Indicates if the order current amount differs form the one of the
            associated authorization.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata]): Set of key-value pairs
            that you can attach to the resource. This can be useful for storing additional information about the resource in
            a structured format. Example: {'foo': 'bar'}.
    """

    public_key: Union[Unset, str] = UNSET
    payment_methods: Union[Unset, "GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods"] = UNSET
    payment_request_data: Union[
        Unset, "GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData"
    ] = UNSET
    payment_request_details: Union[
        Unset, "GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails"
    ] = UNSET
    payment_response: Union[Unset, "GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse"] = UNSET
    mismatched_amounts: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_key = self.public_key
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        payment_request_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_request_data, Unset):
            payment_request_data = self.payment_request_data.to_dict()

        payment_request_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_request_details, Unset):
            payment_request_details = self.payment_request_details.to_dict()

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
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if payment_request_data is not UNSET:
            field_dict["payment_request_data"] = payment_request_data
        if payment_request_details is not UNSET:
            field_dict["payment_request_details"] = payment_request_details
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
        from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_metadata import (
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata,
        )
        from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_methods import (
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods,
        )
        from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_data import (
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData,
        )
        from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_request_details import (
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails,
        )
        from ..models.ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes_payment_response import (
            GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse,
        )

        d = src_dict.copy()
        public_key = d.pop("public_key", UNSET)

        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentMethods.from_dict(
                _payment_methods
            )

        _payment_request_data = d.pop("payment_request_data", UNSET)
        payment_request_data: Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData]
        if isinstance(_payment_request_data, Unset):
            payment_request_data = UNSET
        else:
            payment_request_data = GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestData.from_dict(
                _payment_request_data
            )

        _payment_request_details = d.pop("payment_request_details", UNSET)
        payment_request_details: Union[
            Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails
        ]
        if isinstance(_payment_request_details, Unset):
            payment_request_details = UNSET
        else:
            payment_request_details = (
                GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentRequestDetails.from_dict(
                    _payment_request_details
                )
            )

        _payment_response = d.pop("payment_response", UNSET)
        payment_response: Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = GETadyenPaymentsadyenPaymentIdResponse200DataAttributesPaymentResponse.from_dict(
                _payment_response
            )

        mismatched_amounts = d.pop("mismatched_amounts", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETadyenPaymentsadyenPaymentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes = cls(
            public_key=public_key,
            payment_methods=payment_methods,
            payment_request_data=payment_request_data,
            payment_request_details=payment_request_details,
            payment_response=payment_response,
            mismatched_amounts=mismatched_amounts,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes.additional_properties = d
        return ge_tadyen_paymentsadyen_payment_id_response_200_data_attributes

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
