from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_treturn_line_items_response_201_data_relationships_line_item import (
        POSTreturnLineItemsResponse201DataRelationshipsLineItem,
    )
    from ..models.pos_treturn_line_items_response_201_data_relationships_return import (
        POSTreturnLineItemsResponse201DataRelationshipsReturn,
    )


T = TypeVar("T", bound="POSTreturnLineItemsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTreturnLineItemsResponse201DataRelationships:
    """
    Attributes:
        return_ (Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsReturn]):
        line_item (Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItem]):
    """

    return_: Union[Unset, "POSTreturnLineItemsResponse201DataRelationshipsReturn"] = UNSET
    line_item: Union[Unset, "POSTreturnLineItemsResponse201DataRelationshipsLineItem"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_, Unset):
            return_ = self.return_.to_dict()

        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_ is not UNSET:
            field_dict["return"] = return_
        if line_item is not UNSET:
            field_dict["line_item"] = line_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_treturn_line_items_response_201_data_relationships_line_item import (
            POSTreturnLineItemsResponse201DataRelationshipsLineItem,
        )
        from ..models.pos_treturn_line_items_response_201_data_relationships_return import (
            POSTreturnLineItemsResponse201DataRelationshipsReturn,
        )

        d = src_dict.copy()
        _return_ = d.pop("return", UNSET)
        return_: Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsReturn]
        if isinstance(_return_, Unset):
            return_ = UNSET
        else:
            return_ = POSTreturnLineItemsResponse201DataRelationshipsReturn.from_dict(_return_)

        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = POSTreturnLineItemsResponse201DataRelationshipsLineItem.from_dict(_line_item)

        pos_treturn_line_items_response_201_data_relationships = cls(
            return_=return_,
            line_item=line_item,
        )

        pos_treturn_line_items_response_201_data_relationships.additional_properties = d
        return pos_treturn_line_items_response_201_data_relationships

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
