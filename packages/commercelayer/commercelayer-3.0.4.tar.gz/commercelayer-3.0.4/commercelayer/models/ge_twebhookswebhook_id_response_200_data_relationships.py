from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_twebhookswebhook_id_response_200_data_relationships_last_event_callbacks import (
        GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks,
    )


T = TypeVar("T", bound="GETwebhookswebhookIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETwebhookswebhookIdResponse200DataRelationships:
    """
    Attributes:
        last_event_callbacks (Union[Unset, GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks]):
    """

    last_event_callbacks: Union[Unset, "GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks"] = UNSET
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
        from ..models.ge_twebhookswebhook_id_response_200_data_relationships_last_event_callbacks import (
            GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks,
        )

        d = src_dict.copy()
        _last_event_callbacks = d.pop("last_event_callbacks", UNSET)
        last_event_callbacks: Union[Unset, GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks]
        if isinstance(_last_event_callbacks, Unset):
            last_event_callbacks = UNSET
        else:
            last_event_callbacks = GETwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks.from_dict(
                _last_event_callbacks
            )

        ge_twebhookswebhook_id_response_200_data_relationships = cls(
            last_event_callbacks=last_event_callbacks,
        )

        ge_twebhookswebhook_id_response_200_data_relationships.additional_properties = d
        return ge_twebhookswebhook_id_response_200_data_relationships

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
