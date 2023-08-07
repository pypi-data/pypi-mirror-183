from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships_braintree_payments import (
        PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments,
    )
    from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships_payment_methods import (
        PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods,
    )


T = TypeVar("T", bound="PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset,
            PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods]):
        braintree_payments (Union[Unset,
            PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments]):
    """

    payment_methods: Union[
        Unset, "PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods"
    ] = UNSET
    braintree_payments: Union[
        Unset, "PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        braintree_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.braintree_payments, Unset):
            braintree_payments = self.braintree_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if braintree_payments is not UNSET:
            field_dict["braintree_payments"] = braintree_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships_braintree_payments import (
            PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments,
        )
        from ..models.patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships_payment_methods import (
            PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[
            Unset, PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods
        ]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = (
                PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsPaymentMethods.from_dict(
                    _payment_methods
                )
            )

        _braintree_payments = d.pop("braintree_payments", UNSET)
        braintree_payments: Union[
            Unset, PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments
        ]
        if isinstance(_braintree_payments, Unset):
            braintree_payments = UNSET
        else:
            braintree_payments = (
                PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataRelationshipsBraintreePayments.from_dict(
                    _braintree_payments
                )
            )

        patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships = cls(
            payment_methods=payment_methods,
            braintree_payments=braintree_payments,
        )

        patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships.additional_properties = d
        return patc_hbraintree_gatewaysbraintree_gateway_id_response_200_data_relationships

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
