from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_data_relationships_order_data import TransactionDataRelationshipsOrderData


T = TypeVar("T", bound="TransactionDataRelationshipsOrder")


@attr.s(auto_attribs=True)
class TransactionDataRelationshipsOrder:
    """
    Attributes:
        data (Union[Unset, TransactionDataRelationshipsOrderData]):
    """

    data: Union[Unset, "TransactionDataRelationshipsOrderData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction_data_relationships_order_data import TransactionDataRelationshipsOrderData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TransactionDataRelationshipsOrderData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TransactionDataRelationshipsOrderData.from_dict(_data)

        transaction_data_relationships_order = cls(
            data=data,
        )

        transaction_data_relationships_order.additional_properties = d
        return transaction_data_relationships_order

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
