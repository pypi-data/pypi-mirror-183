from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tline_item_options_response_201_data_relationships_line_item import (
        POSTlineItemOptionsResponse201DataRelationshipsLineItem,
    )
    from ..models.pos_tline_item_options_response_201_data_relationships_sku_option import (
        POSTlineItemOptionsResponse201DataRelationshipsSkuOption,
    )


T = TypeVar("T", bound="POSTlineItemOptionsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTlineItemOptionsResponse201DataRelationships:
    """
    Attributes:
        line_item (Union[Unset, POSTlineItemOptionsResponse201DataRelationshipsLineItem]):
        sku_option (Union[Unset, POSTlineItemOptionsResponse201DataRelationshipsSkuOption]):
    """

    line_item: Union[Unset, "POSTlineItemOptionsResponse201DataRelationshipsLineItem"] = UNSET
    sku_option: Union[Unset, "POSTlineItemOptionsResponse201DataRelationshipsSkuOption"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        sku_option: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_option, Unset):
            sku_option = self.sku_option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_item is not UNSET:
            field_dict["line_item"] = line_item
        if sku_option is not UNSET:
            field_dict["sku_option"] = sku_option

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tline_item_options_response_201_data_relationships_line_item import (
            POSTlineItemOptionsResponse201DataRelationshipsLineItem,
        )
        from ..models.pos_tline_item_options_response_201_data_relationships_sku_option import (
            POSTlineItemOptionsResponse201DataRelationshipsSkuOption,
        )

        d = src_dict.copy()
        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, POSTlineItemOptionsResponse201DataRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = POSTlineItemOptionsResponse201DataRelationshipsLineItem.from_dict(_line_item)

        _sku_option = d.pop("sku_option", UNSET)
        sku_option: Union[Unset, POSTlineItemOptionsResponse201DataRelationshipsSkuOption]
        if isinstance(_sku_option, Unset):
            sku_option = UNSET
        else:
            sku_option = POSTlineItemOptionsResponse201DataRelationshipsSkuOption.from_dict(_sku_option)

        pos_tline_item_options_response_201_data_relationships = cls(
            line_item=line_item,
            sku_option=sku_option,
        )

        pos_tline_item_options_response_201_data_relationships.additional_properties = d
        return pos_tline_item_options_response_201_data_relationships

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
