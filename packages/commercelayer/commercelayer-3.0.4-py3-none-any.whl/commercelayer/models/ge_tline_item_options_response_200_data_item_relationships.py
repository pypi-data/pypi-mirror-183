from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tline_item_options_response_200_data_item_relationships_line_item import (
        GETlineItemOptionsResponse200DataItemRelationshipsLineItem,
    )
    from ..models.ge_tline_item_options_response_200_data_item_relationships_sku_option import (
        GETlineItemOptionsResponse200DataItemRelationshipsSkuOption,
    )


T = TypeVar("T", bound="GETlineItemOptionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETlineItemOptionsResponse200DataItemRelationships:
    """
    Attributes:
        line_item (Union[Unset, GETlineItemOptionsResponse200DataItemRelationshipsLineItem]):
        sku_option (Union[Unset, GETlineItemOptionsResponse200DataItemRelationshipsSkuOption]):
    """

    line_item: Union[Unset, "GETlineItemOptionsResponse200DataItemRelationshipsLineItem"] = UNSET
    sku_option: Union[Unset, "GETlineItemOptionsResponse200DataItemRelationshipsSkuOption"] = UNSET
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
        from ..models.ge_tline_item_options_response_200_data_item_relationships_line_item import (
            GETlineItemOptionsResponse200DataItemRelationshipsLineItem,
        )
        from ..models.ge_tline_item_options_response_200_data_item_relationships_sku_option import (
            GETlineItemOptionsResponse200DataItemRelationshipsSkuOption,
        )

        d = src_dict.copy()
        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, GETlineItemOptionsResponse200DataItemRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = GETlineItemOptionsResponse200DataItemRelationshipsLineItem.from_dict(_line_item)

        _sku_option = d.pop("sku_option", UNSET)
        sku_option: Union[Unset, GETlineItemOptionsResponse200DataItemRelationshipsSkuOption]
        if isinstance(_sku_option, Unset):
            sku_option = UNSET
        else:
            sku_option = GETlineItemOptionsResponse200DataItemRelationshipsSkuOption.from_dict(_sku_option)

        ge_tline_item_options_response_200_data_item_relationships = cls(
            line_item=line_item,
            sku_option=sku_option,
        )

        ge_tline_item_options_response_200_data_item_relationships.additional_properties = d
        return ge_tline_item_options_response_200_data_item_relationships

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
