from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.order_copy_create_data_relationships_source_order import OrderCopyCreateDataRelationshipsSourceOrder


T = TypeVar("T", bound="OrderCopyCreateDataRelationships")


@attr.s(auto_attribs=True)
class OrderCopyCreateDataRelationships:
    """
    Attributes:
        source_order (OrderCopyCreateDataRelationshipsSourceOrder):
    """

    source_order: "OrderCopyCreateDataRelationshipsSourceOrder"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_order = self.source_order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_order": source_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_copy_create_data_relationships_source_order import (
            OrderCopyCreateDataRelationshipsSourceOrder,
        )

        d = src_dict.copy()
        source_order = OrderCopyCreateDataRelationshipsSourceOrder.from_dict(d.pop("source_order"))

        order_copy_create_data_relationships = cls(
            source_order=source_order,
        )

        order_copy_create_data_relationships.additional_properties = d
        return order_copy_create_data_relationships

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
