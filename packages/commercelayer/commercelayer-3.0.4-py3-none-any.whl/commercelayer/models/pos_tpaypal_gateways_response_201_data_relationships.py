from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tpaypal_gateways_response_201_data_relationships_payment_methods import (
        POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods,
    )
    from ..models.pos_tpaypal_gateways_response_201_data_relationships_paypal_payments import (
        POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments,
    )


T = TypeVar("T", bound="POSTpaypalGatewaysResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTpaypalGatewaysResponse201DataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods]):
        paypal_payments (Union[Unset, POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments]):
    """

    payment_methods: Union[Unset, "POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods"] = UNSET
    paypal_payments: Union[Unset, "POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments"] = UNSET
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
        from ..models.pos_tpaypal_gateways_response_201_data_relationships_payment_methods import (
            POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods,
        )
        from ..models.pos_tpaypal_gateways_response_201_data_relationships_paypal_payments import (
            POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = POSTpaypalGatewaysResponse201DataRelationshipsPaymentMethods.from_dict(_payment_methods)

        _paypal_payments = d.pop("paypal_payments", UNSET)
        paypal_payments: Union[Unset, POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments]
        if isinstance(_paypal_payments, Unset):
            paypal_payments = UNSET
        else:
            paypal_payments = POSTpaypalGatewaysResponse201DataRelationshipsPaypalPayments.from_dict(_paypal_payments)

        pos_tpaypal_gateways_response_201_data_relationships = cls(
            payment_methods=payment_methods,
            paypal_payments=paypal_payments,
        )

        pos_tpaypal_gateways_response_201_data_relationships.additional_properties = d
        return pos_tpaypal_gateways_response_201_data_relationships

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
