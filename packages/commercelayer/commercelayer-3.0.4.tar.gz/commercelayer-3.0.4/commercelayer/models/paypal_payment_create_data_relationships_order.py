from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.paypal_payment_create_data_relationships_order_data import (
        PaypalPaymentCreateDataRelationshipsOrderData,
    )


T = TypeVar("T", bound="PaypalPaymentCreateDataRelationshipsOrder")


@attr.s(auto_attribs=True)
class PaypalPaymentCreateDataRelationshipsOrder:
    """
    Attributes:
        data (PaypalPaymentCreateDataRelationshipsOrderData):
    """

    data: "PaypalPaymentCreateDataRelationshipsOrderData"
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
        from ..models.paypal_payment_create_data_relationships_order_data import (
            PaypalPaymentCreateDataRelationshipsOrderData,
        )

        d = src_dict.copy()
        data = PaypalPaymentCreateDataRelationshipsOrderData.from_dict(d.pop("data"))

        paypal_payment_create_data_relationships_order = cls(
            data=data,
        )

        paypal_payment_create_data_relationships_order.additional_properties = d
        return paypal_payment_create_data_relationships_order

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
