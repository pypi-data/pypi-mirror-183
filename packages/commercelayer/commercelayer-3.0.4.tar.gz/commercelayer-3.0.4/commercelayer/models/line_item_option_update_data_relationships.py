from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_option_update_data_relationships_sku_option import (
        LineItemOptionUpdateDataRelationshipsSkuOption,
    )


T = TypeVar("T", bound="LineItemOptionUpdateDataRelationships")


@attr.s(auto_attribs=True)
class LineItemOptionUpdateDataRelationships:
    """
    Attributes:
        sku_option (Union[Unset, LineItemOptionUpdateDataRelationshipsSkuOption]):
    """

    sku_option: Union[Unset, "LineItemOptionUpdateDataRelationshipsSkuOption"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_option: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_option, Unset):
            sku_option = self.sku_option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_option is not UNSET:
            field_dict["sku_option"] = sku_option

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_option_update_data_relationships_sku_option import (
            LineItemOptionUpdateDataRelationshipsSkuOption,
        )

        d = src_dict.copy()
        _sku_option = d.pop("sku_option", UNSET)
        sku_option: Union[Unset, LineItemOptionUpdateDataRelationshipsSkuOption]
        if isinstance(_sku_option, Unset):
            sku_option = UNSET
        else:
            sku_option = LineItemOptionUpdateDataRelationshipsSkuOption.from_dict(_sku_option)

        line_item_option_update_data_relationships = cls(
            sku_option=sku_option,
        )

        line_item_option_update_data_relationships.additional_properties = d
        return line_item_option_update_data_relationships

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
