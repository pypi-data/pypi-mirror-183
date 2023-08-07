from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_transfer_create_data_relationships_destination_stock_location import (
        StockTransferCreateDataRelationshipsDestinationStockLocation,
    )
    from ..models.stock_transfer_create_data_relationships_line_item import StockTransferCreateDataRelationshipsLineItem
    from ..models.stock_transfer_create_data_relationships_origin_stock_location import (
        StockTransferCreateDataRelationshipsOriginStockLocation,
    )
    from ..models.stock_transfer_create_data_relationships_shipment import StockTransferCreateDataRelationshipsShipment
    from ..models.stock_transfer_create_data_relationships_sku import StockTransferCreateDataRelationshipsSku


T = TypeVar("T", bound="StockTransferCreateDataRelationships")


@attr.s(auto_attribs=True)
class StockTransferCreateDataRelationships:
    """
    Attributes:
        sku (StockTransferCreateDataRelationshipsSku):
        origin_stock_location (StockTransferCreateDataRelationshipsOriginStockLocation):
        destination_stock_location (StockTransferCreateDataRelationshipsDestinationStockLocation):
        shipment (Union[Unset, StockTransferCreateDataRelationshipsShipment]):
        line_item (Union[Unset, StockTransferCreateDataRelationshipsLineItem]):
    """

    sku: "StockTransferCreateDataRelationshipsSku"
    origin_stock_location: "StockTransferCreateDataRelationshipsOriginStockLocation"
    destination_stock_location: "StockTransferCreateDataRelationshipsDestinationStockLocation"
    shipment: Union[Unset, "StockTransferCreateDataRelationshipsShipment"] = UNSET
    line_item: Union[Unset, "StockTransferCreateDataRelationshipsLineItem"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku = self.sku.to_dict()

        origin_stock_location = self.origin_stock_location.to_dict()

        destination_stock_location = self.destination_stock_location.to_dict()

        shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku": sku,
                "origin_stock_location": origin_stock_location,
                "destination_stock_location": destination_stock_location,
            }
        )
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if line_item is not UNSET:
            field_dict["line_item"] = line_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_transfer_create_data_relationships_destination_stock_location import (
            StockTransferCreateDataRelationshipsDestinationStockLocation,
        )
        from ..models.stock_transfer_create_data_relationships_line_item import (
            StockTransferCreateDataRelationshipsLineItem,
        )
        from ..models.stock_transfer_create_data_relationships_origin_stock_location import (
            StockTransferCreateDataRelationshipsOriginStockLocation,
        )
        from ..models.stock_transfer_create_data_relationships_shipment import (
            StockTransferCreateDataRelationshipsShipment,
        )
        from ..models.stock_transfer_create_data_relationships_sku import StockTransferCreateDataRelationshipsSku

        d = src_dict.copy()
        sku = StockTransferCreateDataRelationshipsSku.from_dict(d.pop("sku"))

        origin_stock_location = StockTransferCreateDataRelationshipsOriginStockLocation.from_dict(
            d.pop("origin_stock_location")
        )

        destination_stock_location = StockTransferCreateDataRelationshipsDestinationStockLocation.from_dict(
            d.pop("destination_stock_location")
        )

        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, StockTransferCreateDataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = StockTransferCreateDataRelationshipsShipment.from_dict(_shipment)

        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, StockTransferCreateDataRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = StockTransferCreateDataRelationshipsLineItem.from_dict(_line_item)

        stock_transfer_create_data_relationships = cls(
            sku=sku,
            origin_stock_location=origin_stock_location,
            destination_stock_location=destination_stock_location,
            shipment=shipment,
            line_item=line_item,
        )

        stock_transfer_create_data_relationships.additional_properties = d
        return stock_transfer_create_data_relationships

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
