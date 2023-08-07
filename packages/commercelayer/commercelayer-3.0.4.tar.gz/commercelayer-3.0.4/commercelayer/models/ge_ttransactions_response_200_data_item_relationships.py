from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttransactions_response_200_data_item_relationships_order import (
        GETtransactionsResponse200DataItemRelationshipsOrder,
    )


T = TypeVar("T", bound="GETtransactionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETtransactionsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETtransactionsResponse200DataItemRelationshipsOrder]):
    """

    order: Union[Unset, "GETtransactionsResponse200DataItemRelationshipsOrder"] = UNSET
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
        from ..models.ge_ttransactions_response_200_data_item_relationships_order import (
            GETtransactionsResponse200DataItemRelationshipsOrder,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETtransactionsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETtransactionsResponse200DataItemRelationshipsOrder.from_dict(_order)

        ge_ttransactions_response_200_data_item_relationships = cls(
            order=order,
        )

        ge_ttransactions_response_200_data_item_relationships.additional_properties = d
        return ge_ttransactions_response_200_data_item_relationships

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
