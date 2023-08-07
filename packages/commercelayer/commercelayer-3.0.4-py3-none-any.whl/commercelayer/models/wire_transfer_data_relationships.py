from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wire_transfer_data_relationships_order import WireTransferDataRelationshipsOrder


T = TypeVar("T", bound="WireTransferDataRelationships")


@attr.s(auto_attribs=True)
class WireTransferDataRelationships:
    """
    Attributes:
        order (Union[Unset, WireTransferDataRelationshipsOrder]):
    """

    order: Union[Unset, "WireTransferDataRelationshipsOrder"] = UNSET
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
        from ..models.wire_transfer_data_relationships_order import WireTransferDataRelationshipsOrder

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, WireTransferDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = WireTransferDataRelationshipsOrder.from_dict(_order)

        wire_transfer_data_relationships = cls(
            order=order,
        )

        wire_transfer_data_relationships.additional_properties = d
        return wire_transfer_data_relationships

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
