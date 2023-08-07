from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.payment_method_update_data_relationships_payment_gateway_data import (
        PaymentMethodUpdateDataRelationshipsPaymentGatewayData,
    )


T = TypeVar("T", bound="PaymentMethodUpdateDataRelationshipsPaymentGateway")


@attr.s(auto_attribs=True)
class PaymentMethodUpdateDataRelationshipsPaymentGateway:
    """
    Attributes:
        data (PaymentMethodUpdateDataRelationshipsPaymentGatewayData):
    """

    data: "PaymentMethodUpdateDataRelationshipsPaymentGatewayData"
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
        from ..models.payment_method_update_data_relationships_payment_gateway_data import (
            PaymentMethodUpdateDataRelationshipsPaymentGatewayData,
        )

        d = src_dict.copy()
        data = PaymentMethodUpdateDataRelationshipsPaymentGatewayData.from_dict(d.pop("data"))

        payment_method_update_data_relationships_payment_gateway = cls(
            data=data,
        )

        payment_method_update_data_relationships_payment_gateway.additional_properties = d
        return payment_method_update_data_relationships_payment_gateway

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
