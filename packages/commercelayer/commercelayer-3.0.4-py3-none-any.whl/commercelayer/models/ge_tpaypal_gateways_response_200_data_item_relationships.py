from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpaypal_gateways_response_200_data_item_relationships_payment_methods import (
        GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods,
    )
    from ..models.ge_tpaypal_gateways_response_200_data_item_relationships_paypal_payments import (
        GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments,
    )


T = TypeVar("T", bound="GETpaypalGatewaysResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpaypalGatewaysResponse200DataItemRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods]):
        paypal_payments (Union[Unset, GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments]):
    """

    payment_methods: Union[Unset, "GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods"] = UNSET
    paypal_payments: Union[Unset, "GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        paypal_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paypal_payments, Unset):
            paypal_payments = self.paypal_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if paypal_payments is not UNSET:
            field_dict["paypal_payments"] = paypal_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tpaypal_gateways_response_200_data_item_relationships_payment_methods import (
            GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods,
        )
        from ..models.ge_tpaypal_gateways_response_200_data_item_relationships_paypal_payments import (
            GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = GETpaypalGatewaysResponse200DataItemRelationshipsPaymentMethods.from_dict(
                _payment_methods
            )

        _paypal_payments = d.pop("paypal_payments", UNSET)
        paypal_payments: Union[Unset, GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments]
        if isinstance(_paypal_payments, Unset):
            paypal_payments = UNSET
        else:
            paypal_payments = GETpaypalGatewaysResponse200DataItemRelationshipsPaypalPayments.from_dict(
                _paypal_payments
            )

        ge_tpaypal_gateways_response_200_data_item_relationships = cls(
            payment_methods=payment_methods,
            paypal_payments=paypal_payments,
        )

        ge_tpaypal_gateways_response_200_data_item_relationships.additional_properties = d
        return ge_tpaypal_gateways_response_200_data_item_relationships

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
