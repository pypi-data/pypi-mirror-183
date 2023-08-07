from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tadyen_gateways_response_200_data_item_relationships_adyen_payments import (
        GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments,
    )
    from ..models.ge_tadyen_gateways_response_200_data_item_relationships_payment_methods import (
        GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods,
    )


T = TypeVar("T", bound="GETadyenGatewaysResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETadyenGatewaysResponse200DataItemRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods]):
        adyen_payments (Union[Unset, GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments]):
    """

    payment_methods: Union[Unset, "GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods"] = UNSET
    adyen_payments: Union[Unset, "GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments"] = UNSET
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
        from ..models.ge_tadyen_gateways_response_200_data_item_relationships_adyen_payments import (
            GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments,
        )
        from ..models.ge_tadyen_gateways_response_200_data_item_relationships_payment_methods import (
            GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = GETadyenGatewaysResponse200DataItemRelationshipsPaymentMethods.from_dict(_payment_methods)

        _adyen_payments = d.pop("adyen_payments", UNSET)
        adyen_payments: Union[Unset, GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments]
        if isinstance(_adyen_payments, Unset):
            adyen_payments = UNSET
        else:
            adyen_payments = GETadyenGatewaysResponse200DataItemRelationshipsAdyenPayments.from_dict(_adyen_payments)

        ge_tadyen_gateways_response_200_data_item_relationships = cls(
            payment_methods=payment_methods,
            adyen_payments=adyen_payments,
        )

        ge_tadyen_gateways_response_200_data_item_relationships.additional_properties = d
        return ge_tadyen_gateways_response_200_data_item_relationships

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
