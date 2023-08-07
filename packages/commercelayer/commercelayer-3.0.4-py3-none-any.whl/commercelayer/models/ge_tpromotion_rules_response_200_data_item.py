from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_tpromotion_rules_response_200_data_item_type import GETpromotionRulesResponse200DataItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpromotion_rules_response_200_data_item_attributes import (
        GETpromotionRulesResponse200DataItemAttributes,
    )
    from ..models.ge_tpromotion_rules_response_200_data_item_links import GETpromotionRulesResponse200DataItemLinks
    from ..models.ge_tpromotion_rules_response_200_data_item_relationships import (
        GETpromotionRulesResponse200DataItemRelationships,
    )


T = TypeVar("T", bound="GETpromotionRulesResponse200DataItem")


@attr.s(auto_attribs=True)
class GETpromotionRulesResponse200DataItem:
    """
    Attributes:
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
        type (Union[Unset, GETpromotionRulesResponse200DataItemType]): The resource's type
        links (Union[Unset, GETpromotionRulesResponse200DataItemLinks]):
        attributes (Union[Unset, GETpromotionRulesResponse200DataItemAttributes]):
        relationships (Union[Unset, GETpromotionRulesResponse200DataItemRelationships]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, GETpromotionRulesResponse200DataItemType] = UNSET
    links: Union[Unset, "GETpromotionRulesResponse200DataItemLinks"] = UNSET
    attributes: Union[Unset, "GETpromotionRulesResponse200DataItemAttributes"] = UNSET
    relationships: Union[Unset, "GETpromotionRulesResponse200DataItemRelationships"] = UNSET
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
        from ..models.ge_tpromotion_rules_response_200_data_item_attributes import (
            GETpromotionRulesResponse200DataItemAttributes,
        )
        from ..models.ge_tpromotion_rules_response_200_data_item_links import GETpromotionRulesResponse200DataItemLinks
        from ..models.ge_tpromotion_rules_response_200_data_item_relationships import (
            GETpromotionRulesResponse200DataItemRelationships,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GETpromotionRulesResponse200DataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETpromotionRulesResponse200DataItemType(_type)

        _links = d.pop("links", UNSET)
        links: Union[Unset, GETpromotionRulesResponse200DataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETpromotionRulesResponse200DataItemLinks.from_dict(_links)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, GETpromotionRulesResponse200DataItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = GETpromotionRulesResponse200DataItemAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, GETpromotionRulesResponse200DataItemRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = GETpromotionRulesResponse200DataItemRelationships.from_dict(_relationships)

        ge_tpromotion_rules_response_200_data_item = cls(
            id=id,
            type=type,
            links=links,
            attributes=attributes,
            relationships=relationships,
        )

        ge_tpromotion_rules_response_200_data_item.additional_properties = d
        return ge_tpromotion_rules_response_200_data_item

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
