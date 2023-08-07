from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_tline_item_optionsline_item_option_id_response_200_data_relationships_sku_option_data_type import (
    GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionData")


@attr.s(auto_attribs=True)
class GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionData:
    """
    Attributes:
        type (Union[Unset, GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionDataType]): The
            resource's type
        id (Union[Unset, str]): The resource ID
    """

    type: Union[Unset, GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionDataType] = UNSET
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
        type: Union[Unset, GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOptionDataType(_type)

        id = d.pop("id", UNSET)

        ge_tline_item_optionsline_item_option_id_response_200_data_relationships_sku_option_data = cls(
            type=type,
            id=id,
        )

        ge_tline_item_optionsline_item_option_id_response_200_data_relationships_sku_option_data.additional_properties = (
            d
        )
        return ge_tline_item_optionsline_item_option_id_response_200_data_relationships_sku_option_data

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
