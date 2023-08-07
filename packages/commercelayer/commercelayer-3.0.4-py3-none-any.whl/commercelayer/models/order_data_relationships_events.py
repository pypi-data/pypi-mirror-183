from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_data_relationships_events_data import OrderDataRelationshipsEventsData


T = TypeVar("T", bound="OrderDataRelationshipsEvents")


@attr.s(auto_attribs=True)
class OrderDataRelationshipsEvents:
    """
    Attributes:
        data (Union[Unset, OrderDataRelationshipsEventsData]):
    """

    data: Union[Unset, "OrderDataRelationshipsEventsData"] = UNSET
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
        from ..models.order_data_relationships_events_data import OrderDataRelationshipsEventsData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, OrderDataRelationshipsEventsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = OrderDataRelationshipsEventsData.from_dict(_data)

        order_data_relationships_events = cls(
            data=data,
        )

        order_data_relationships_events.additional_properties = d
        return order_data_relationships_events

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
