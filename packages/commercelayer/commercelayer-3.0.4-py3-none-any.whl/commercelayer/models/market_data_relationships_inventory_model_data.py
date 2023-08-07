from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.market_data_relationships_inventory_model_data_type import MarketDataRelationshipsInventoryModelDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataRelationshipsInventoryModelData")


@attr.s(auto_attribs=True)
class MarketDataRelationshipsInventoryModelData:
    """
    Attributes:
        type (Union[Unset, MarketDataRelationshipsInventoryModelDataType]): The resource's type
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
    """

    type: Union[Unset, MarketDataRelationshipsInventoryModelDataType] = UNSET
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
        type: Union[Unset, MarketDataRelationshipsInventoryModelDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MarketDataRelationshipsInventoryModelDataType(_type)

        id = d.pop("id", UNSET)

        market_data_relationships_inventory_model_data = cls(
            type=type,
            id=id,
        )

        market_data_relationships_inventory_model_data.additional_properties = d
        return market_data_relationships_inventory_model_data

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
