from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location import (
        GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_events import (
        GETstockTransfersResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_line_item import (
        GETstockTransfersResponse200DataItemRelationshipsLineItem,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location import (
        GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_shipment import (
        GETstockTransfersResponse200DataItemRelationshipsShipment,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_sku import (
        GETstockTransfersResponse200DataItemRelationshipsSku,
    )


T = TypeVar("T", bound="GETstockTransfersResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETstockTransfersResponse200DataItemRelationships:
    """
    Attributes:
        sku (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsSku]):
        origin_stock_location (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation]):
        destination_stock_location (Union[Unset,
            GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation]):
        shipment (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsShipment]):
        line_item (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsLineItem]):
        events (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsEvents]):
    """

    sku: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsSku"] = UNSET
    origin_stock_location: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation"] = UNSET
    destination_stock_location: Union[
        Unset, "GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation"
    ] = UNSET
    shipment: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsShipment"] = UNSET
    line_item: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsLineItem"] = UNSET
    events: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        origin_stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_stock_location, Unset):
            origin_stock_location = self.origin_stock_location.to_dict()

        destination_stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination_stock_location, Unset):
            destination_stock_location = self.destination_stock_location.to_dict()

        shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if origin_stock_location is not UNSET:
            field_dict["origin_stock_location"] = origin_stock_location
        if destination_stock_location is not UNSET:
            field_dict["destination_stock_location"] = destination_stock_location
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if line_item is not UNSET:
            field_dict["line_item"] = line_item
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location import (
            GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_events import (
            GETstockTransfersResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_line_item import (
            GETstockTransfersResponse200DataItemRelationshipsLineItem,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location import (
            GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_shipment import (
            GETstockTransfersResponse200DataItemRelationshipsShipment,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_sku import (
            GETstockTransfersResponse200DataItemRelationshipsSku,
        )

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETstockTransfersResponse200DataItemRelationshipsSku.from_dict(_sku)

        _origin_stock_location = d.pop("origin_stock_location", UNSET)
        origin_stock_location: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation]
        if isinstance(_origin_stock_location, Unset):
            origin_stock_location = UNSET
        else:
            origin_stock_location = GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation.from_dict(
                _origin_stock_location
            )

        _destination_stock_location = d.pop("destination_stock_location", UNSET)
        destination_stock_location: Union[
            Unset, GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation
        ]
        if isinstance(_destination_stock_location, Unset):
            destination_stock_location = UNSET
        else:
            destination_stock_location = (
                GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation.from_dict(
                    _destination_stock_location
                )
            )

        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = GETstockTransfersResponse200DataItemRelationshipsShipment.from_dict(_shipment)

        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = GETstockTransfersResponse200DataItemRelationshipsLineItem.from_dict(_line_item)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETstockTransfersResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tstock_transfers_response_200_data_item_relationships = cls(
            sku=sku,
            origin_stock_location=origin_stock_location,
            destination_stock_location=destination_stock_location,
            shipment=shipment,
            line_item=line_item,
            events=events,
        )

        ge_tstock_transfers_response_200_data_item_relationships.additional_properties = d
        return ge_tstock_transfers_response_200_data_item_relationships

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
