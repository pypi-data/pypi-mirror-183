from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_com_payment_update_data_relationships_order import (
        CheckoutComPaymentUpdateDataRelationshipsOrder,
    )


T = TypeVar("T", bound="CheckoutComPaymentUpdateDataRelationships")


@attr.s(auto_attribs=True)
class CheckoutComPaymentUpdateDataRelationships:
    """
    Attributes:
        order (Union[Unset, CheckoutComPaymentUpdateDataRelationshipsOrder]):
    """

    order: Union[Unset, "CheckoutComPaymentUpdateDataRelationshipsOrder"] = UNSET
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
        from ..models.checkout_com_payment_update_data_relationships_order import (
            CheckoutComPaymentUpdateDataRelationshipsOrder,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, CheckoutComPaymentUpdateDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = CheckoutComPaymentUpdateDataRelationshipsOrder.from_dict(_order)

        checkout_com_payment_update_data_relationships = cls(
            order=order,
        )

        checkout_com_payment_update_data_relationships.additional_properties = d
        return checkout_com_payment_update_data_relationships

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
