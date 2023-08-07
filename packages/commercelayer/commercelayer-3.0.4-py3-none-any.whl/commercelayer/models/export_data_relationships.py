from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_data_relationships_events import ExportDataRelationshipsEvents


T = TypeVar("T", bound="ExportDataRelationships")


@attr.s(auto_attribs=True)
class ExportDataRelationships:
    """
    Attributes:
        events (Union[Unset, ExportDataRelationshipsEvents]):
    """

    events: Union[Unset, "ExportDataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.export_data_relationships_events import ExportDataRelationshipsEvents

        d = src_dict.copy()
        _events = d.pop("events", UNSET)
        events: Union[Unset, ExportDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = ExportDataRelationshipsEvents.from_dict(_events)

        export_data_relationships = cls(
            events=events,
        )

        export_data_relationships.additional_properties = d
        return export_data_relationships

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
