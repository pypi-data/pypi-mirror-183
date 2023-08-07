from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_tmarketsmarket_id_response_200_data_relationships_merchant_data_type import (
    GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GETmarketsmarketIdResponse200DataRelationshipsMerchantData")


@attr.s(auto_attribs=True)
class GETmarketsmarketIdResponse200DataRelationshipsMerchantData:
    """
    Attributes:
        type (Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType]): The resource's type
        id (Union[Unset, str]): The resource ID
    """

    type: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType] = UNSET
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
        type: Union[Unset, GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETmarketsmarketIdResponse200DataRelationshipsMerchantDataType(_type)

        id = d.pop("id", UNSET)

        ge_tmarketsmarket_id_response_200_data_relationships_merchant_data = cls(
            type=type,
            id=id,
        )

        ge_tmarketsmarket_id_response_200_data_relationships_merchant_data.additional_properties = d
        return ge_tmarketsmarket_id_response_200_data_relationships_merchant_data

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
