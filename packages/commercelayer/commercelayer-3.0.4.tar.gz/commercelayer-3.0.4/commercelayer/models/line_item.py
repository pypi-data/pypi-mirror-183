from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_data import LineItemData


T = TypeVar("T", bound="LineItem")


@attr.s(auto_attribs=True)
class LineItem:
    """
    Attributes:
        data (Union[Unset, LineItemData]):
    """

    data: Union[Unset, "LineItemData"] = UNSET
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
        from ..models.line_item_data import LineItemData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, LineItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = LineItemData.from_dict(_data)

        line_item = cls(
            data=data,
        )

        line_item.additional_properties = d
        return line_item

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
