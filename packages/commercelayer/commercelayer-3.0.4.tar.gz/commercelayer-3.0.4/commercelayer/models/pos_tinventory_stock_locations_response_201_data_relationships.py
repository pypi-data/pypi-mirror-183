from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tinventory_stock_locations_response_201_data_relationships_inventory_model import (
        POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel,
    )
    from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location import (
        POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="POSTinventoryStockLocationsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTinventoryStockLocationsResponse201DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation]):
        inventory_model (Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel]):
    """

    stock_location: Union[Unset, "POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation"] = UNSET
    inventory_model: Union[Unset, "POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel"] = UNSET
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
        from ..models.pos_tinventory_stock_locations_response_201_data_relationships_inventory_model import (
            POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel,
        )
        from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location import (
            POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation.from_dict(
                _stock_location
            )

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = POSTinventoryStockLocationsResponse201DataRelationshipsInventoryModel.from_dict(
                _inventory_model
            )

        pos_tinventory_stock_locations_response_201_data_relationships = cls(
            stock_location=stock_location,
            inventory_model=inventory_model,
        )

        pos_tinventory_stock_locations_response_201_data_relationships.additional_properties = d
        return pos_tinventory_stock_locations_response_201_data_relationships

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
