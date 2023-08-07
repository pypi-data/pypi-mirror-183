from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.line_item_option_create_data_relationships_line_item import (
        LineItemOptionCreateDataRelationshipsLineItem,
    )
    from ..models.line_item_option_create_data_relationships_sku_option import (
        LineItemOptionCreateDataRelationshipsSkuOption,
    )


T = TypeVar("T", bound="LineItemOptionCreateDataRelationships")


@attr.s(auto_attribs=True)
class LineItemOptionCreateDataRelationships:
    """
    Attributes:
        line_item (LineItemOptionCreateDataRelationshipsLineItem):
        sku_option (LineItemOptionCreateDataRelationshipsSkuOption):
    """

    line_item: "LineItemOptionCreateDataRelationshipsLineItem"
    sku_option: "LineItemOptionCreateDataRelationshipsSkuOption"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_item = self.line_item.to_dict()

        sku_option = self.sku_option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_item": line_item,
                "sku_option": sku_option,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_option_create_data_relationships_line_item import (
            LineItemOptionCreateDataRelationshipsLineItem,
        )
        from ..models.line_item_option_create_data_relationships_sku_option import (
            LineItemOptionCreateDataRelationshipsSkuOption,
        )

        d = src_dict.copy()
        line_item = LineItemOptionCreateDataRelationshipsLineItem.from_dict(d.pop("line_item"))

        sku_option = LineItemOptionCreateDataRelationshipsSkuOption.from_dict(d.pop("sku_option"))

        line_item_option_create_data_relationships = cls(
            line_item=line_item,
            sku_option=sku_option,
        )

        line_item_option_create_data_relationships.additional_properties = d
        return line_item_option_create_data_relationships

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
