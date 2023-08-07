from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_callback_data_relationships_webhook import EventCallbackDataRelationshipsWebhook


T = TypeVar("T", bound="EventCallbackDataRelationships")


@attr.s(auto_attribs=True)
class EventCallbackDataRelationships:
    """
    Attributes:
        webhook (Union[Unset, EventCallbackDataRelationshipsWebhook]):
    """

    webhook: Union[Unset, "EventCallbackDataRelationshipsWebhook"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webhook, Unset):
            webhook = self.webhook.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_callback_data_relationships_webhook import EventCallbackDataRelationshipsWebhook

        d = src_dict.copy()
        _webhook = d.pop("webhook", UNSET)
        webhook: Union[Unset, EventCallbackDataRelationshipsWebhook]
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = EventCallbackDataRelationshipsWebhook.from_dict(_webhook)

        event_callback_data_relationships = cls(
            webhook=webhook,
        )

        event_callback_data_relationships.additional_properties = d
        return event_callback_data_relationships

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
