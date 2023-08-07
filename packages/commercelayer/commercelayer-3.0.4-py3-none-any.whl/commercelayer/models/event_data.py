from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_data_type import EventDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_data_attributes import EventDataAttributes
    from ..models.event_data_relationships import EventDataRelationships


T = TypeVar("T", bound="EventData")


@attr.s(auto_attribs=True)
class EventData:
    """
    Attributes:
        type (EventDataType): The resource's type
        attributes (EventDataAttributes):
        relationships (Union[Unset, EventDataRelationships]):
    """

    type: EventDataType
    attributes: "EventDataAttributes"
    relationships: Union[Unset, "EventDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_data_attributes import EventDataAttributes
        from ..models.event_data_relationships import EventDataRelationships

        d = src_dict.copy()
        type = EventDataType(d.pop("type"))

        attributes = EventDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, EventDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = EventDataRelationships.from_dict(_relationships)

        event_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        event_data.additional_properties = d
        return event_data

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
