from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations_data_type import (
    GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsData")


@attr.s(auto_attribs=True)
class GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsData:
    """
    Attributes:
        type (Union[Unset, GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsDataType]): The
            resource's type
        id (Union[Unset, str]): The resource ID
    """

    type: Union[Unset, GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsDataType] = UNSET
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
        type: Union[Unset, GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocationsDataType(_type)

        id = d.pop("id", UNSET)

        ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations_data = cls(
            type=type,
            id=id,
        )

        ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations_data.additional_properties = (
            d
        )
        return ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations_data

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
