from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.checkout_com_payment_create_data_relationships_order import (
        CheckoutComPaymentCreateDataRelationshipsOrder,
    )


T = TypeVar("T", bound="CheckoutComPaymentCreateDataRelationships")


@attr.s(auto_attribs=True)
class CheckoutComPaymentCreateDataRelationships:
    """
    Attributes:
        order (CheckoutComPaymentCreateDataRelationshipsOrder):
    """

    order: "CheckoutComPaymentCreateDataRelationshipsOrder"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_com_payment_create_data_relationships_order import (
            CheckoutComPaymentCreateDataRelationshipsOrder,
        )

        d = src_dict.copy()
        order = CheckoutComPaymentCreateDataRelationshipsOrder.from_dict(d.pop("order"))

        checkout_com_payment_create_data_relationships = cls(
            order=order,
        )

        checkout_com_payment_create_data_relationships.additional_properties = d
        return checkout_com_payment_create_data_relationships

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
