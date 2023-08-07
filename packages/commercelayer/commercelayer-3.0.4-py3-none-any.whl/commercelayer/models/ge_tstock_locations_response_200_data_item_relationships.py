from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_locations_response_200_data_item_relationships_address import (
        GETstockLocationsResponse200DataItemRelationshipsAddress,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_attachments import (
        GETstockLocationsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_return_locations import (
        GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations import (
        GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_stock_items import (
        GETstockLocationsResponse200DataItemRelationshipsStockItems,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_stock_transfers import (
        GETstockLocationsResponse200DataItemRelationshipsStockTransfers,
    )


T = TypeVar("T", bound="GETstockLocationsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETstockLocationsResponse200DataItemRelationships:
    """
    Attributes:
        address (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsAddress]):
        inventory_stock_locations (Union[Unset,
            GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations]):
        inventory_return_locations (Union[Unset,
            GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations]):
        stock_items (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsStockItems]):
        stock_transfers (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsStockTransfers]):
        attachments (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsAttachments]):
    """

    address: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsAddress"] = UNSET
    inventory_stock_locations: Union[
        Unset, "GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations"
    ] = UNSET
    inventory_return_locations: Union[
        Unset, "GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations"
    ] = UNSET
    stock_items: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsStockItems"] = UNSET
    stock_transfers: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsStockTransfers"] = UNSET
    attachments: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tstock_locations_response_200_data_item_relationships_address import (
            GETstockLocationsResponse200DataItemRelationshipsAddress,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_attachments import (
            GETstockLocationsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_return_locations import (
            GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations import (
            GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_stock_items import (
            GETstockLocationsResponse200DataItemRelationshipsStockItems,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_stock_transfers import (
            GETstockLocationsResponse200DataItemRelationshipsStockTransfers,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GETstockLocationsResponse200DataItemRelationshipsAddress.from_dict(_address)

        _inventory_stock_locations = d.pop("inventory_stock_locations", UNSET)
        inventory_stock_locations: Union[
            Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations
        ]
        if isinstance(_inventory_stock_locations, Unset):
            inventory_stock_locations = UNSET
        else:
            inventory_stock_locations = (
                GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations.from_dict(
                    _inventory_stock_locations
                )
            )

        _inventory_return_locations = d.pop("inventory_return_locations", UNSET)
        inventory_return_locations: Union[
            Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations
        ]
        if isinstance(_inventory_return_locations, Unset):
            inventory_return_locations = UNSET
        else:
            inventory_return_locations = (
                GETstockLocationsResponse200DataItemRelationshipsInventoryReturnLocations.from_dict(
                    _inventory_return_locations
                )
            )

        _stock_items = d.pop("stock_items", UNSET)
        stock_items: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsStockItems]
        if isinstance(_stock_items, Unset):
            stock_items = UNSET
        else:
            stock_items = GETstockLocationsResponse200DataItemRelationshipsStockItems.from_dict(_stock_items)

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = GETstockLocationsResponse200DataItemRelationshipsStockTransfers.from_dict(
                _stock_transfers
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETstockLocationsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tstock_locations_response_200_data_item_relationships = cls(
            address=address,
            inventory_stock_locations=inventory_stock_locations,
            inventory_return_locations=inventory_return_locations,
            stock_items=stock_items,
            stock_transfers=stock_transfers,
            attachments=attachments,
        )

        ge_tstock_locations_response_200_data_item_relationships.additional_properties = d
        return ge_tstock_locations_response_200_data_item_relationships

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
