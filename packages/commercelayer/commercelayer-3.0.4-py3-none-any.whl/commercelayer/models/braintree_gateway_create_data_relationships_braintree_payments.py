from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.braintree_gateway_create_data_relationships_braintree_payments_data import (
        BraintreeGatewayCreateDataRelationshipsBraintreePaymentsData,
    )


T = TypeVar("T", bound="BraintreeGatewayCreateDataRelationshipsBraintreePayments")


@attr.s(auto_attribs=True)
class BraintreeGatewayCreateDataRelationshipsBraintreePayments:
    """
    Attributes:
        data (BraintreeGatewayCreateDataRelationshipsBraintreePaymentsData):
    """

    data: "BraintreeGatewayCreateDataRelationshipsBraintreePaymentsData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.braintree_gateway_create_data_relationships_braintree_payments_data import (
            BraintreeGatewayCreateDataRelationshipsBraintreePaymentsData,
        )

        d = src_dict.copy()
        data = BraintreeGatewayCreateDataRelationshipsBraintreePaymentsData.from_dict(d.pop("data"))

        braintree_gateway_create_data_relationships_braintree_payments = cls(
            data=data,
        )

        braintree_gateway_create_data_relationships_braintree_payments.additional_properties = d
        return braintree_gateway_create_data_relationships_braintree_payments

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
