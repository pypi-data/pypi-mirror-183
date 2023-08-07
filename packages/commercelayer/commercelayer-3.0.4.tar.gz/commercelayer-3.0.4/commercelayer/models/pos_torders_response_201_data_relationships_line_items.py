from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torders_response_201_data_relationships_line_items_data import (
        POSTordersResponse201DataRelationshipsLineItemsData,
    )
    from ..models.pos_torders_response_201_data_relationships_line_items_links import (
        POSTordersResponse201DataRelationshipsLineItemsLinks,
    )


T = TypeVar("T", bound="POSTordersResponse201DataRelationshipsLineItems")


@attr.s(auto_attribs=True)
class POSTordersResponse201DataRelationshipsLineItems:
    """
    Attributes:
        links (Union[Unset, POSTordersResponse201DataRelationshipsLineItemsLinks]):
        data (Union[Unset, POSTordersResponse201DataRelationshipsLineItemsData]):
    """

    links: Union[Unset, "POSTordersResponse201DataRelationshipsLineItemsLinks"] = UNSET
    data: Union[Unset, "POSTordersResponse201DataRelationshipsLineItemsData"] = UNSET
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
        from ..models.pos_torders_response_201_data_relationships_line_items_data import (
            POSTordersResponse201DataRelationshipsLineItemsData,
        )
        from ..models.pos_torders_response_201_data_relationships_line_items_links import (
            POSTordersResponse201DataRelationshipsLineItemsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTordersResponse201DataRelationshipsLineItemsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTordersResponse201DataRelationshipsLineItemsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTordersResponse201DataRelationshipsLineItemsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTordersResponse201DataRelationshipsLineItemsData.from_dict(_data)

        pos_torders_response_201_data_relationships_line_items = cls(
            links=links,
            data=data,
        )

        pos_torders_response_201_data_relationships_line_items.additional_properties = d
        return pos_torders_response_201_data_relationships_line_items

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
