from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_com_gateway_create_data_relationships_checkout_com_payments import (
        CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments,
    )


T = TypeVar("T", bound="CheckoutComGatewayCreateDataRelationships")


@attr.s(auto_attribs=True)
class CheckoutComGatewayCreateDataRelationships:
    """
    Attributes:
        checkout_com_payments (Union[Unset, CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments]):
    """

    checkout_com_payments: Union[Unset, "CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkout_com_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_com_payments, Unset):
            checkout_com_payments = self.checkout_com_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkout_com_payments is not UNSET:
            field_dict["checkout_com_payments"] = checkout_com_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_com_gateway_create_data_relationships_checkout_com_payments import (
            CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments,
        )

        d = src_dict.copy()
        _checkout_com_payments = d.pop("checkout_com_payments", UNSET)
        checkout_com_payments: Union[Unset, CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments]
        if isinstance(_checkout_com_payments, Unset):
            checkout_com_payments = UNSET
        else:
            checkout_com_payments = CheckoutComGatewayCreateDataRelationshipsCheckoutComPayments.from_dict(
                _checkout_com_payments
            )

        checkout_com_gateway_create_data_relationships = cls(
            checkout_com_payments=checkout_com_payments,
        )

        checkout_com_gateway_create_data_relationships.additional_properties = d
        return checkout_com_gateway_create_data_relationships

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
