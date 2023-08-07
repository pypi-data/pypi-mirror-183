from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_stock_location_data_relationships_inventory_model import (
        InventoryStockLocationDataRelationshipsInventoryModel,
    )
    from ..models.inventory_stock_location_data_relationships_stock_location import (
        InventoryStockLocationDataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="InventoryStockLocationDataRelationships")


@attr.s(auto_attribs=True)
class InventoryStockLocationDataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, InventoryStockLocationDataRelationshipsStockLocation]):
        inventory_model (Union[Unset, InventoryStockLocationDataRelationshipsInventoryModel]):
    """

    stock_location: Union[Unset, "InventoryStockLocationDataRelationshipsStockLocation"] = UNSET
    inventory_model: Union[Unset, "InventoryStockLocationDataRelationshipsInventoryModel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        inventory_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_model, Unset):
            inventory_model = self.inventory_model.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if inventory_model is not UNSET:
            field_dict["inventory_model"] = inventory_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_stock_location_data_relationships_inventory_model import (
            InventoryStockLocationDataRelationshipsInventoryModel,
        )
        from ..models.inventory_stock_location_data_relationships_stock_location import (
            InventoryStockLocationDataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, InventoryStockLocationDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = InventoryStockLocationDataRelationshipsStockLocation.from_dict(_stock_location)

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[Unset, InventoryStockLocationDataRelationshipsInventoryModel]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = InventoryStockLocationDataRelationshipsInventoryModel.from_dict(_inventory_model)

        inventory_stock_location_data_relationships = cls(
            stock_location=stock_location,
            inventory_model=inventory_model,
        )

        inventory_stock_location_data_relationships.additional_properties = d
        return inventory_stock_location_data_relationships

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
