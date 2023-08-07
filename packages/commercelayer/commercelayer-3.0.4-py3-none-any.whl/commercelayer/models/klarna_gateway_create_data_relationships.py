from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.klarna_gateway_create_data_relationships_klarna_payments import (
        KlarnaGatewayCreateDataRelationshipsKlarnaPayments,
    )


T = TypeVar("T", bound="KlarnaGatewayCreateDataRelationships")


@attr.s(auto_attribs=True)
class KlarnaGatewayCreateDataRelationships:
    """
    Attributes:
        klarna_payments (Union[Unset, KlarnaGatewayCreateDataRelationshipsKlarnaPayments]):
    """

    klarna_payments: Union[Unset, "KlarnaGatewayCreateDataRelationshipsKlarnaPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        klarna_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.klarna_payments, Unset):
            klarna_payments = self.klarna_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if klarna_payments is not UNSET:
            field_dict["klarna_payments"] = klarna_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.klarna_gateway_create_data_relationships_klarna_payments import (
            KlarnaGatewayCreateDataRelationshipsKlarnaPayments,
        )

        d = src_dict.copy()
        _klarna_payments = d.pop("klarna_payments", UNSET)
        klarna_payments: Union[Unset, KlarnaGatewayCreateDataRelationshipsKlarnaPayments]
        if isinstance(_klarna_payments, Unset):
            klarna_payments = UNSET
        else:
            klarna_payments = KlarnaGatewayCreateDataRelationshipsKlarnaPayments.from_dict(_klarna_payments)

        klarna_gateway_create_data_relationships = cls(
            klarna_payments=klarna_payments,
        )

        klarna_gateway_create_data_relationships.additional_properties = d
        return klarna_gateway_create_data_relationships

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
