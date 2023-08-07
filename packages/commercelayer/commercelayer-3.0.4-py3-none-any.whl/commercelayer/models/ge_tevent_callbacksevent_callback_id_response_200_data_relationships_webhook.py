from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook_data import (
        GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData,
    )
    from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook_links import (
        GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks,
    )


T = TypeVar("T", bound="GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook")


@attr.s(auto_attribs=True)
class GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhook:
    """
    Attributes:
        links (Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks]):
        data (Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData]):
    """

    links: Union[Unset, "GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks"] = UNSET
    data: Union[Unset, "GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData"] = UNSET
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
        from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook_data import (
            GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData,
        )
        from ..models.ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook_links import (
            GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETeventCallbackseventCallbackIdResponse200DataRelationshipsWebhookData.from_dict(_data)

        ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook = cls(
            links=links,
            data=data,
        )

        ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook.additional_properties = d
        return ge_tevent_callbacksevent_callback_id_response_200_data_relationships_webhook

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
