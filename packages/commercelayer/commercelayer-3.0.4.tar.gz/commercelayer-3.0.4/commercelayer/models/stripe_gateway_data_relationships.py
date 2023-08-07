from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_gateway_data_relationships_payment_methods import StripeGatewayDataRelationshipsPaymentMethods
    from ..models.stripe_gateway_data_relationships_stripe_payments import StripeGatewayDataRelationshipsStripePayments


T = TypeVar("T", bound="StripeGatewayDataRelationships")


@attr.s(auto_attribs=True)
class StripeGatewayDataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, StripeGatewayDataRelationshipsPaymentMethods]):
        stripe_payments (Union[Unset, StripeGatewayDataRelationshipsStripePayments]):
    """

    payment_methods: Union[Unset, "StripeGatewayDataRelationshipsPaymentMethods"] = UNSET
    stripe_payments: Union[Unset, "StripeGatewayDataRelationshipsStripePayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        stripe_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stripe_payments, Unset):
            stripe_payments = self.stripe_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods
        if stripe_payments is not UNSET:
            field_dict["stripe_payments"] = stripe_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_gateway_data_relationships_payment_methods import (
            StripeGatewayDataRelationshipsPaymentMethods,
        )
        from ..models.stripe_gateway_data_relationships_stripe_payments import (
            StripeGatewayDataRelationshipsStripePayments,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, StripeGatewayDataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = StripeGatewayDataRelationshipsPaymentMethods.from_dict(_payment_methods)

        _stripe_payments = d.pop("stripe_payments", UNSET)
        stripe_payments: Union[Unset, StripeGatewayDataRelationshipsStripePayments]
        if isinstance(_stripe_payments, Unset):
            stripe_payments = UNSET
        else:
            stripe_payments = StripeGatewayDataRelationshipsStripePayments.from_dict(_stripe_payments)

        stripe_gateway_data_relationships = cls(
            payment_methods=payment_methods,
            stripe_payments=stripe_payments,
        )

        stripe_gateway_data_relationships.additional_properties = d
        return stripe_gateway_data_relationships

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
