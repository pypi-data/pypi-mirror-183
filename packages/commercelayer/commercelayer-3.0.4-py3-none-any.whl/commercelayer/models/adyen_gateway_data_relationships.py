from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_gateway_data_relationships_adyen_payments import AdyenGatewayDataRelationshipsAdyenPayments
    from ..models.adyen_gateway_data_relationships_payment_methods import AdyenGatewayDataRelationshipsPaymentMethods


T = TypeVar("T", bound="AdyenGatewayDataRelationships")


@attr.s(auto_attribs=True)
class AdyenGatewayDataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, AdyenGatewayDataRelationshipsPaymentMethods]):
        adyen_payments (Union[Unset, AdyenGatewayDataRelationshipsAdyenPayments]):
    """

    payment_methods: Union[Unset, "AdyenGatewayDataRelationshipsPaymentMethods"] = UNSET
    adyen_payments: Union[Unset, "AdyenGatewayDataRelationshipsAdyenPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        adyen_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.adyen_payments, Unset):
            adyen_payments = self.adyen_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if adyen_payments is not UNSET:
            field_dict["adyen_payments"] = adyen_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_gateway_data_relationships_adyen_payments import AdyenGatewayDataRelationshipsAdyenPayments
        from ..models.adyen_gateway_data_relationships_payment_methods import (
            AdyenGatewayDataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, AdyenGatewayDataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = AdyenGatewayDataRelationshipsPaymentMethods.from_dict(_payment_methods)

        _adyen_payments = d.pop("adyen_payments", UNSET)
        adyen_payments: Union[Unset, AdyenGatewayDataRelationshipsAdyenPayments]
        if isinstance(_adyen_payments, Unset):
            adyen_payments = UNSET
        else:
            adyen_payments = AdyenGatewayDataRelationshipsAdyenPayments.from_dict(_adyen_payments)

        adyen_gateway_data_relationships = cls(
            payment_methods=payment_methods,
            adyen_payments=adyen_payments,
        )

        adyen_gateway_data_relationships.additional_properties = d
        return adyen_gateway_data_relationships

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
