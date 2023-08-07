from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.return_line_item_create_data_relationships_line_item import (
        ReturnLineItemCreateDataRelationshipsLineItem,
    )
    from ..models.return_line_item_create_data_relationships_return import ReturnLineItemCreateDataRelationshipsReturn


T = TypeVar("T", bound="ReturnLineItemCreateDataRelationships")


@attr.s(auto_attribs=True)
class ReturnLineItemCreateDataRelationships:
    """
    Attributes:
        return_ (ReturnLineItemCreateDataRelationshipsReturn):
        line_item (ReturnLineItemCreateDataRelationshipsLineItem):
    """

    return_: "ReturnLineItemCreateDataRelationshipsReturn"
    line_item: "ReturnLineItemCreateDataRelationshipsLineItem"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_ = self.return_.to_dict()

        line_item = self.line_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "return": return_,
                "line_item": line_item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.return_line_item_create_data_relationships_line_item import (
            ReturnLineItemCreateDataRelationshipsLineItem,
        )
        from ..models.return_line_item_create_data_relationships_return import (
            ReturnLineItemCreateDataRelationshipsReturn,
        )

        d = src_dict.copy()
        return_ = ReturnLineItemCreateDataRelationshipsReturn.from_dict(d.pop("return"))

        line_item = ReturnLineItemCreateDataRelationshipsLineItem.from_dict(d.pop("line_item"))

        return_line_item_create_data_relationships = cls(
            return_=return_,
            line_item=line_item,
        )

        return_line_item_create_data_relationships.additional_properties = d
        return return_line_item_create_data_relationships

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
