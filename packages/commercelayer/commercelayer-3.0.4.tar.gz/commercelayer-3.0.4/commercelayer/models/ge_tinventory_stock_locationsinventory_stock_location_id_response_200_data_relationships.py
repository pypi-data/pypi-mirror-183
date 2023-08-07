from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_inventory_model import (
        GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel,
    )
    from ..models.ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location import (
        GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset,
            GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation]):
        inventory_model (Union[Unset,
            GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel]):
    """

    stock_location: Union[
        Unset, "GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation"
    ] = UNSET
    inventory_model: Union[
        Unset, "GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel"
    ] = UNSET
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
        from ..models.ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_inventory_model import (
            GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel,
        )
        from ..models.ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location import (
            GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[
            Unset, GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation
        ]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = (
                GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation.from_dict(
                    _stock_location
                )
            )

        _inventory_model = d.pop("inventory_model", UNSET)
        inventory_model: Union[
            Unset, GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel
        ]
        if isinstance(_inventory_model, Unset):
            inventory_model = UNSET
        else:
            inventory_model = (
                GETinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsInventoryModel.from_dict(
                    _inventory_model
                )
            )

        ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships = cls(
            stock_location=stock_location,
            inventory_model=inventory_model,
        )

        ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships.additional_properties = (
            d
        )
        return ge_tinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships

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
