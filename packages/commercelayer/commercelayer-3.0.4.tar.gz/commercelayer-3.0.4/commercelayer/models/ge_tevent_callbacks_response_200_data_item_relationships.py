from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tevent_callbacks_response_200_data_item_relationships_webhook import (
        GETeventCallbacksResponse200DataItemRelationshipsWebhook,
    )


T = TypeVar("T", bound="GETeventCallbacksResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETeventCallbacksResponse200DataItemRelationships:
    """
    Attributes:
        webhook (Union[Unset, GETeventCallbacksResponse200DataItemRelationshipsWebhook]):
    """

    webhook: Union[Unset, "GETeventCallbacksResponse200DataItemRelationshipsWebhook"] = UNSET
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
        from ..models.ge_tevent_callbacks_response_200_data_item_relationships_webhook import (
            GETeventCallbacksResponse200DataItemRelationshipsWebhook,
        )

        d = src_dict.copy()
        _webhook = d.pop("webhook", UNSET)
        webhook: Union[Unset, GETeventCallbacksResponse200DataItemRelationshipsWebhook]
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = GETeventCallbacksResponse200DataItemRelationshipsWebhook.from_dict(_webhook)

        ge_tevent_callbacks_response_200_data_item_relationships = cls(
            webhook=webhook,
        )

        ge_tevent_callbacks_response_200_data_item_relationships.additional_properties = d
        return ge_tevent_callbacks_response_200_data_item_relationships

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
