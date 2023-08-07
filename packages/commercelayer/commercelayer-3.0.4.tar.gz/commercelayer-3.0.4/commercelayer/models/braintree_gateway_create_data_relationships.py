from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.braintree_gateway_create_data_relationships_braintree_payments import (
        BraintreeGatewayCreateDataRelationshipsBraintreePayments,
    )


T = TypeVar("T", bound="BraintreeGatewayCreateDataRelationships")


@attr.s(auto_attribs=True)
class BraintreeGatewayCreateDataRelationships:
    """
    Attributes:
        braintree_payments (Union[Unset, BraintreeGatewayCreateDataRelationshipsBraintreePayments]):
    """

    braintree_payments: Union[Unset, "BraintreeGatewayCreateDataRelationshipsBraintreePayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        braintree_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.braintree_payments, Unset):
            braintree_payments = self.braintree_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if braintree_payments is not UNSET:
            field_dict["braintree_payments"] = braintree_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.braintree_gateway_create_data_relationships_braintree_payments import (
            BraintreeGatewayCreateDataRelationshipsBraintreePayments,
        )

        d = src_dict.copy()
        _braintree_payments = d.pop("braintree_payments", UNSET)
        braintree_payments: Union[Unset, BraintreeGatewayCreateDataRelationshipsBraintreePayments]
        if isinstance(_braintree_payments, Unset):
            braintree_payments = UNSET
        else:
            braintree_payments = BraintreeGatewayCreateDataRelationshipsBraintreePayments.from_dict(_braintree_payments)

        braintree_gateway_create_data_relationships = cls(
            braintree_payments=braintree_payments,
        )

        braintree_gateway_create_data_relationships.additional_properties = d
        return braintree_gateway_create_data_relationships

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
