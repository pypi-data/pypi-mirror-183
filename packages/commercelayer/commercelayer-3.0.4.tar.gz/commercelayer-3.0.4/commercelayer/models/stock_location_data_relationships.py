from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_location_data_relationships_address import StockLocationDataRelationshipsAddress
    from ..models.stock_location_data_relationships_attachments import StockLocationDataRelationshipsAttachments
    from ..models.stock_location_data_relationships_inventory_return_locations import (
        StockLocationDataRelationshipsInventoryReturnLocations,
    )
    from ..models.stock_location_data_relationships_inventory_stock_locations import (
        StockLocationDataRelationshipsInventoryStockLocations,
    )
    from ..models.stock_location_data_relationships_stock_items import StockLocationDataRelationshipsStockItems
    from ..models.stock_location_data_relationships_stock_transfers import StockLocationDataRelationshipsStockTransfers


T = TypeVar("T", bound="StockLocationDataRelationships")


@attr.s(auto_attribs=True)
class StockLocationDataRelationships:
    """
    Attributes:
        address (Union[Unset, StockLocationDataRelationshipsAddress]):
        inventory_stock_locations (Union[Unset, StockLocationDataRelationshipsInventoryStockLocations]):
        inventory_return_locations (Union[Unset, StockLocationDataRelationshipsInventoryReturnLocations]):
        stock_items (Union[Unset, StockLocationDataRelationshipsStockItems]):
        stock_transfers (Union[Unset, StockLocationDataRelationshipsStockTransfers]):
        attachments (Union[Unset, StockLocationDataRelationshipsAttachments]):
    """

    address: Union[Unset, "StockLocationDataRelationshipsAddress"] = UNSET
    inventory_stock_locations: Union[Unset, "StockLocationDataRelationshipsInventoryStockLocations"] = UNSET
    inventory_return_locations: Union[Unset, "StockLocationDataRelationshipsInventoryReturnLocations"] = UNSET
    stock_items: Union[Unset, "StockLocationDataRelationshipsStockItems"] = UNSET
    stock_transfers: Union[Unset, "StockLocationDataRelationshipsStockTransfers"] = UNSET
    attachments: Union[Unset, "StockLocationDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        inventory_stock_locations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_stock_locations, Unset):
            inventory_stock_locations = self.inventory_stock_locations.to_dict()

        inventory_return_locations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_return_locations, Unset):
            inventory_return_locations = self.inventory_return_locations.to_dict()

        stock_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_items, Unset):
            stock_items = self.stock_items.to_dict()

        stock_transfers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_transfers, Unset):
            stock_transfers = self.stock_transfers.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if inventory_stock_locations is not UNSET:
            field_dict["inventory_stock_locations"] = inventory_stock_locations
        if inventory_return_locations is not UNSET:
            field_dict["inventory_return_locations"] = inventory_return_locations
        if stock_items is not UNSET:
            field_dict["stock_items"] = stock_items
        if stock_transfers is not UNSET:
            field_dict["stock_transfers"] = stock_transfers
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_location_data_relationships_address import StockLocationDataRelationshipsAddress
        from ..models.stock_location_data_relationships_attachments import StockLocationDataRelationshipsAttachments
        from ..models.stock_location_data_relationships_inventory_return_locations import (
            StockLocationDataRelationshipsInventoryReturnLocations,
        )
        from ..models.stock_location_data_relationships_inventory_stock_locations import (
            StockLocationDataRelationshipsInventoryStockLocations,
        )
        from ..models.stock_location_data_relationships_stock_items import StockLocationDataRelationshipsStockItems
        from ..models.stock_location_data_relationships_stock_transfers import (
            StockLocationDataRelationshipsStockTransfers,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, StockLocationDataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = StockLocationDataRelationshipsAddress.from_dict(_address)

        _inventory_stock_locations = d.pop("inventory_stock_locations", UNSET)
        inventory_stock_locations: Union[Unset, StockLocationDataRelationshipsInventoryStockLocations]
        if isinstance(_inventory_stock_locations, Unset):
            inventory_stock_locations = UNSET
        else:
            inventory_stock_locations = StockLocationDataRelationshipsInventoryStockLocations.from_dict(
                _inventory_stock_locations
            )

        _inventory_return_locations = d.pop("inventory_return_locations", UNSET)
        inventory_return_locations: Union[Unset, StockLocationDataRelationshipsInventoryReturnLocations]
        if isinstance(_inventory_return_locations, Unset):
            inventory_return_locations = UNSET
        else:
            inventory_return_locations = StockLocationDataRelationshipsInventoryReturnLocations.from_dict(
                _inventory_return_locations
            )

        _stock_items = d.pop("stock_items", UNSET)
        stock_items: Union[Unset, StockLocationDataRelationshipsStockItems]
        if isinstance(_stock_items, Unset):
            stock_items = UNSET
        else:
            stock_items = StockLocationDataRelationshipsStockItems.from_dict(_stock_items)

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, StockLocationDataRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = StockLocationDataRelationshipsStockTransfers.from_dict(_stock_transfers)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, StockLocationDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = StockLocationDataRelationshipsAttachments.from_dict(_attachments)

        stock_location_data_relationships = cls(
            address=address,
            inventory_stock_locations=inventory_stock_locations,
            inventory_return_locations=inventory_return_locations,
            stock_items=stock_items,
            stock_transfers=stock_transfers,
            attachments=attachments,
        )

        stock_location_data_relationships.additional_properties = d
        return stock_location_data_relationships

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
