from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_teventsevent_id_response_200_data_relationships_webhooks_data_type import (
    GETeventseventIdResponse200DataRelationshipsWebhooksDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GETeventseventIdResponse200DataRelationshipsWebhooksData")


@attr.s(auto_attribs=True)
class GETeventseventIdResponse200DataRelationshipsWebhooksData:
    """
    Attributes:
        type (Union[Unset, GETeventseventIdResponse200DataRelationshipsWebhooksDataType]): The resource's type
        id (Union[Unset, str]): The resource ID
    """

    type: Union[Unset, GETeventseventIdResponse200DataRelationshipsWebhooksDataType] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, GETeventseventIdResponse200DataRelationshipsWebhooksDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETeventseventIdResponse200DataRelationshipsWebhooksDataType(_type)

        id = d.pop("id", UNSET)

        ge_teventsevent_id_response_200_data_relationships_webhooks_data = cls(
            type=type,
            id=id,
        )

        ge_teventsevent_id_response_200_data_relationships_webhooks_data.additional_properties = d
        return ge_teventsevent_id_response_200_data_relationships_webhooks_data

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
