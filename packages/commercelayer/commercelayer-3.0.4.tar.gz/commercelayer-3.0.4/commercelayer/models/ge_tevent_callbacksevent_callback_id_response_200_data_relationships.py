from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook import (
        GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook,
    )


T = TypeVar("T", bound="GETeventCallbackseventCallbackIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETeventCallbackseventCallbackIdResponse200DataRelationships:
    """
    Attributes:
        webhook (Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook]):
    """

    webhook: Union[Unset, "GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook"] = UNSET
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
        from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook import (
            GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook,
        )

        d = src_dict.copy()
        _webhook = d.pop("webhook", UNSET)
        webhook: Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook]
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook.from_dict(_webhook)

        ge_tevent_callbacksevent_callback_id_response_200_data_relationships = cls(
            webhook=webhook,
        )

        ge_tevent_callbacksevent_callback_id_response_200_data_relationships.additional_properties = d
        return ge_tevent_callbacksevent_callback_id_response_200_data_relationships

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
