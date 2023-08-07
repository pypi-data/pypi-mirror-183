from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pos_tsku_list_items_response_201_data_type import POSTskuListItemsResponse201DataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tsku_list_items_response_201_data_attributes import POSTskuListItemsResponse201DataAttributes
    from ..models.pos_tsku_list_items_response_201_data_links import POSTskuListItemsResponse201DataLinks
    from ..models.pos_tsku_list_items_response_201_data_relationships import (
        POSTskuListItemsResponse201DataRelationships,
    )


T = TypeVar("T", bound="POSTskuListItemsResponse201Data")


@attr.s(auto_attribs=True)
class POSTskuListItemsResponse201Data:
    """
    Attributes:
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
        type (Union[Unset, POSTskuListItemsResponse201DataType]): The resource's type
        links (Union[Unset, POSTskuListItemsResponse201DataLinks]):
        attributes (Union[Unset, POSTskuListItemsResponse201DataAttributes]):
        relationships (Union[Unset, POSTskuListItemsResponse201DataRelationships]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, POSTskuListItemsResponse201DataType] = UNSET
    links: Union[Unset, "POSTskuListItemsResponse201DataLinks"] = UNSET
    attributes: Union[Unset, "POSTskuListItemsResponse201DataAttributes"] = UNSET
    relationships: Union[Unset, "POSTskuListItemsResponse201DataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if links is not UNSET:
            field_dict["links"] = links
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tsku_list_items_response_201_data_attributes import POSTskuListItemsResponse201DataAttributes
        from ..models.pos_tsku_list_items_response_201_data_links import POSTskuListItemsResponse201DataLinks
        from ..models.pos_tsku_list_items_response_201_data_relationships import (
            POSTskuListItemsResponse201DataRelationships,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, POSTskuListItemsResponse201DataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = POSTskuListItemsResponse201DataType(_type)

        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTskuListItemsResponse201DataLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTskuListItemsResponse201DataLinks.from_dict(_links)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, POSTskuListItemsResponse201DataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = POSTskuListItemsResponse201DataAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, POSTskuListItemsResponse201DataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = POSTskuListItemsResponse201DataRelationships.from_dict(_relationships)

        pos_tsku_list_items_response_201_data = cls(
            id=id,
            type=type,
            links=links,
            attributes=attributes,
            relationships=relationships,
        )

        pos_tsku_list_items_response_201_data.additional_properties = d
        return pos_tsku_list_items_response_201_data

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
