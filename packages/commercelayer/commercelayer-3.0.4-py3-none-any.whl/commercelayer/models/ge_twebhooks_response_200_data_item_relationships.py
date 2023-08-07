from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_twebhooks_response_200_data_item_relationships_last_event_callbacks import (
        GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks,
    )


T = TypeVar("T", bound="GETwebhooksResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETwebhooksResponse200DataItemRelationships:
    """
    Attributes:
        last_event_callbacks (Union[Unset, GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks]):
    """

    last_event_callbacks: Union[Unset, "GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_event_callbacks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_event_callbacks, Unset):
            last_event_callbacks = self.last_event_callbacks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_event_callbacks is not UNSET:
            field_dict["last_event_callbacks"] = last_event_callbacks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_twebhooks_response_200_data_item_relationships_last_event_callbacks import (
            GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks,
        )

        d = src_dict.copy()
        _last_event_callbacks = d.pop("last_event_callbacks", UNSET)
        last_event_callbacks: Union[Unset, GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks]
        if isinstance(_last_event_callbacks, Unset):
            last_event_callbacks = UNSET
        else:
            last_event_callbacks = GETwebhooksResponse200DataItemRelationshipsLastEventCallbacks.from_dict(
                _last_event_callbacks
            )

        ge_twebhooks_response_200_data_item_relationships = cls(
            last_event_callbacks=last_event_callbacks,
        )

        ge_twebhooks_response_200_data_item_relationships.additional_properties = d
        return ge_twebhooks_response_200_data_item_relationships

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
