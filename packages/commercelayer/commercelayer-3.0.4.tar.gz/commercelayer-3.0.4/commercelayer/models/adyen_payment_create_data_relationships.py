from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.adyen_payment_create_data_relationships_order import AdyenPaymentCreateDataRelationshipsOrder


T = TypeVar("T", bound="AdyenPaymentCreateDataRelationships")


@attr.s(auto_attribs=True)
class AdyenPaymentCreateDataRelationships:
    """
    Attributes:
        order (AdyenPaymentCreateDataRelationshipsOrder):
    """

    order: "AdyenPaymentCreateDataRelationshipsOrder"
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
        from ..models.adyen_payment_create_data_relationships_order import AdyenPaymentCreateDataRelationshipsOrder

        d = src_dict.copy()
        order = AdyenPaymentCreateDataRelationshipsOrder.from_dict(d.pop("order"))

        adyen_payment_create_data_relationships = cls(
            order=order,
        )

        adyen_payment_create_data_relationships.additional_properties = d
        return adyen_payment_create_data_relationships

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
