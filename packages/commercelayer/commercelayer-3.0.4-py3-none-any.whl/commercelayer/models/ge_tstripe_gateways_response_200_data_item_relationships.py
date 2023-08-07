from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstripe_gateways_response_200_data_item_relationships_payment_methods import (
        GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods,
    )
    from ..models.ge_tstripe_gateways_response_200_data_item_relationships_stripe_payments import (
        GETstripeGatewaysResponse200DataItemRelationshipsStripePayments,
    )


T = TypeVar("T", bound="GETstripeGatewaysResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETstripeGatewaysResponse200DataItemRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods]):
        stripe_payments (Union[Unset, GETstripeGatewaysResponse200DataItemRelationshipsStripePayments]):
    """

    payment_methods: Union[Unset, "GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods"] = UNSET
    stripe_payments: Union[Unset, "GETstripeGatewaysResponse200DataItemRelationshipsStripePayments"] = UNSET
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
        from ..models.ge_tstripe_gateways_response_200_data_item_relationships_payment_methods import (
            GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods,
        )
        from ..models.ge_tstripe_gateways_response_200_data_item_relationships_stripe_payments import (
            GETstripeGatewaysResponse200DataItemRelationshipsStripePayments,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = GETstripeGatewaysResponse200DataItemRelationshipsPaymentMethods.from_dict(
                _payment_methods
            )

        _stripe_payments = d.pop("stripe_payments", UNSET)
        stripe_payments: Union[Unset, GETstripeGatewaysResponse200DataItemRelationshipsStripePayments]
        if isinstance(_stripe_payments, Unset):
            stripe_payments = UNSET
        else:
            stripe_payments = GETstripeGatewaysResponse200DataItemRelationshipsStripePayments.from_dict(
                _stripe_payments
            )

        ge_tstripe_gateways_response_200_data_item_relationships = cls(
            payment_methods=payment_methods,
            stripe_payments=stripe_payments,
        )

        ge_tstripe_gateways_response_200_data_item_relationships.additional_properties = d
        return ge_tstripe_gateways_response_200_data_item_relationships

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
