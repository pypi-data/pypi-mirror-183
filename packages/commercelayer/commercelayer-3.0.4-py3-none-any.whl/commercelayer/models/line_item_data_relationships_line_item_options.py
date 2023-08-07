from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_data_relationships_line_item_options_data import (
        LineItemDataRelationshipsLineItemOptionsData,
    )


T = TypeVar("T", bound="LineItemDataRelationshipsLineItemOptions")


@attr.s(auto_attribs=True)
class LineItemDataRelationshipsLineItemOptions:
    """
    Attributes:
        data (Union[Unset, LineItemDataRelationshipsLineItemOptionsData]):
    """

    data: Union[Unset, "LineItemDataRelationshipsLineItemOptionsData"] = UNSET
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
        from ..models.line_item_data_relationships_line_item_options_data import (
            LineItemDataRelationshipsLineItemOptionsData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, LineItemDataRelationshipsLineItemOptionsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = LineItemDataRelationshipsLineItemOptionsData.from_dict(_data)

        line_item_data_relationships_line_item_options = cls(
            data=data,
        )

        line_item_data_relationships_line_item_options.additional_properties = d
        return line_item_data_relationships_line_item_options

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
