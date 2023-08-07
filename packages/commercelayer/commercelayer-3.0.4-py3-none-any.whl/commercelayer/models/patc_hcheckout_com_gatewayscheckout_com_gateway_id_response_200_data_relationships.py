from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships_checkout_com_payments import (
        PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments,
    )
    from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships_payment_methods import (
        PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods,
    )


T = TypeVar("T", bound="PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset,
            PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods]):
        checkout_com_payments (Union[Unset,
            PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments]):
    """

    payment_methods: Union[
        Unset, "PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods"
    ] = UNSET
    checkout_com_payments: Union[
        Unset, "PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        checkout_com_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_com_payments, Unset):
            checkout_com_payments = self.checkout_com_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if checkout_com_payments is not UNSET:
            field_dict["checkout_com_payments"] = checkout_com_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships_checkout_com_payments import (
            PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments,
        )
        from ..models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships_payment_methods import (
            PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[
            Unset, PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods
        ]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = (
                PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsPaymentMethods.from_dict(
                    _payment_methods
                )
            )

        _checkout_com_payments = d.pop("checkout_com_payments", UNSET)
        checkout_com_payments: Union[
            Unset, PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments
        ]
        if isinstance(_checkout_com_payments, Unset):
            checkout_com_payments = UNSET
        else:
            checkout_com_payments = (
                PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataRelationshipsCheckoutComPayments.from_dict(
                    _checkout_com_payments
                )
            )

        patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships = cls(
            payment_methods=payment_methods,
            checkout_com_payments=checkout_com_payments,
        )

        patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships.additional_properties = d
        return patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200_data_relationships

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
