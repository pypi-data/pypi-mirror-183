from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_treturn_line_items_response_201_data_relationships_line_item_data import (
        POSTreturnLineItemsResponse201DataRelationshipsLineItemData,
    )
    from ..models.pos_treturn_line_items_response_201_data_relationships_line_item_links import (
        POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks,
    )


T = TypeVar("T", bound="POSTreturnLineItemsResponse201DataRelationshipsLineItem")


@attr.s(auto_attribs=True)
class POSTreturnLineItemsResponse201DataRelationshipsLineItem:
    """
    Attributes:
        links (Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks]):
        data (Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItemData]):
    """

    links: Union[Unset, "POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks"] = UNSET
    data: Union[Unset, "POSTreturnLineItemsResponse201DataRelationshipsLineItemData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_treturn_line_items_response_201_data_relationships_line_item_data import (
            POSTreturnLineItemsResponse201DataRelationshipsLineItemData,
        )
        from ..models.pos_treturn_line_items_response_201_data_relationships_line_item_links import (
            POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTreturnLineItemsResponse201DataRelationshipsLineItemLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTreturnLineItemsResponse201DataRelationshipsLineItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTreturnLineItemsResponse201DataRelationshipsLineItemData.from_dict(_data)

        pos_treturn_line_items_response_201_data_relationships_line_item = cls(
            links=links,
            data=data,
        )

        pos_treturn_line_items_response_201_data_relationships_line_item.additional_properties = d
        return pos_treturn_line_items_response_201_data_relationships_line_item

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
