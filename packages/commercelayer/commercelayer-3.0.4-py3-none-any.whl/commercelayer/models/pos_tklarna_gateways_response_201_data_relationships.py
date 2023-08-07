from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments import (
        POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments,
    )
    from ..models.pos_tklarna_gateways_response_201_data_relationships_payment_methods import (
        POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods,
    )


T = TypeVar("T", bound="POSTklarnaGatewaysResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTklarnaGatewaysResponse201DataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods]):
        klarna_payments (Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments]):
    """

    payment_methods: Union[Unset, "POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods"] = UNSET
    klarna_payments: Union[Unset, "POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        klarna_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.klarna_payments, Unset):
            klarna_payments = self.klarna_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if klarna_payments is not UNSET:
            field_dict["klarna_payments"] = klarna_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments import (
            POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments,
        )
        from ..models.pos_tklarna_gateways_response_201_data_relationships_payment_methods import (
            POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = POSTklarnaGatewaysResponse201DataRelationshipsPaymentMethods.from_dict(_payment_methods)

        _klarna_payments = d.pop("klarna_payments", UNSET)
        klarna_payments: Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments]
        if isinstance(_klarna_payments, Unset):
            klarna_payments = UNSET
        else:
            klarna_payments = POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments.from_dict(_klarna_payments)

        pos_tklarna_gateways_response_201_data_relationships = cls(
            payment_methods=payment_methods,
            klarna_payments=klarna_payments,
        )

        pos_tklarna_gateways_response_201_data_relationships.additional_properties = d
        return pos_tklarna_gateways_response_201_data_relationships

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
