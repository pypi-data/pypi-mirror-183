from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paypal_payment_update_data_relationships_order import PaypalPaymentUpdateDataRelationshipsOrder


T = TypeVar("T", bound="PaypalPaymentUpdateDataRelationships")


@attr.s(auto_attribs=True)
class PaypalPaymentUpdateDataRelationships:
    """
    Attributes:
        order (Union[Unset, PaypalPaymentUpdateDataRelationshipsOrder]):
    """

    order: Union[Unset, "PaypalPaymentUpdateDataRelationshipsOrder"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.paypal_payment_update_data_relationships_order import PaypalPaymentUpdateDataRelationshipsOrder

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PaypalPaymentUpdateDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PaypalPaymentUpdateDataRelationshipsOrder.from_dict(_order)

        paypal_payment_update_data_relationships = cls(
            order=order,
        )

        paypal_payment_update_data_relationships.additional_properties = d
        return paypal_payment_update_data_relationships

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
