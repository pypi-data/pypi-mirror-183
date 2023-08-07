from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks_data import (
        PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData,
    )
    from ..models.patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks_links import (
        PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks,
    )


T = TypeVar("T", bound="PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks")


@attr.s(auto_attribs=True)
class PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacks:
    """
    Attributes:
        links (Union[Unset, PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks]):
        data (Union[Unset, PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData]):
    """

    links: Union[Unset, "PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks"] = UNSET
    data: Union[Unset, "PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData"] = UNSET
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
        from ..models.patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks_data import (
            PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData,
        )
        from ..models.patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks_links import (
            PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHwebhookswebhookIdResponse200DataRelationshipsLastEventCallbacksData.from_dict(_data)

        patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks = cls(
            links=links,
            data=data,
        )

        patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks.additional_properties = d
        return patc_hwebhookswebhook_id_response_200_data_relationships_last_event_callbacks

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
