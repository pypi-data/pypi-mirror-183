from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_texternal_gateways_response_201_data_relationships_external_payments import (
        POSTexternalGatewaysResponse201DataRelationshipsExternalPayments,
    )
    from ..models.pos_texternal_gateways_response_201_data_relationships_payment_methods import (
        POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods,
    )


T = TypeVar("T", bound="POSTexternalGatewaysResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTexternalGatewaysResponse201DataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods]):
        external_payments (Union[Unset, POSTexternalGatewaysResponse201DataRelationshipsExternalPayments]):
    """

    payment_methods: Union[Unset, "POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods"] = UNSET
    external_payments: Union[Unset, "POSTexternalGatewaysResponse201DataRelationshipsExternalPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        external_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_payments, Unset):
            external_payments = self.external_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if external_payments is not UNSET:
            field_dict["external_payments"] = external_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_texternal_gateways_response_201_data_relationships_external_payments import (
            POSTexternalGatewaysResponse201DataRelationshipsExternalPayments,
        )
        from ..models.pos_texternal_gateways_response_201_data_relationships_payment_methods import (
            POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = POSTexternalGatewaysResponse201DataRelationshipsPaymentMethods.from_dict(_payment_methods)

        _external_payments = d.pop("external_payments", UNSET)
        external_payments: Union[Unset, POSTexternalGatewaysResponse201DataRelationshipsExternalPayments]
        if isinstance(_external_payments, Unset):
            external_payments = UNSET
        else:
            external_payments = POSTexternalGatewaysResponse201DataRelationshipsExternalPayments.from_dict(
                _external_payments
            )

        pos_texternal_gateways_response_201_data_relationships = cls(
            payment_methods=payment_methods,
            external_payments=external_payments,
        )

        pos_texternal_gateways_response_201_data_relationships.additional_properties = d
        return pos_texternal_gateways_response_201_data_relationships

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
