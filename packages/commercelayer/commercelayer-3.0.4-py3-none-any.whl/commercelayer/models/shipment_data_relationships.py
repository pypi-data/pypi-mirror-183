from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_data_relationships_attachments import ShipmentDataRelationshipsAttachments
    from ..models.shipment_data_relationships_available_shipping_methods import (
        ShipmentDataRelationshipsAvailableShippingMethods,
    )
    from ..models.shipment_data_relationships_carrier_accounts import ShipmentDataRelationshipsCarrierAccounts
    from ..models.shipment_data_relationships_delivery_lead_time import ShipmentDataRelationshipsDeliveryLeadTime
    from ..models.shipment_data_relationships_events import ShipmentDataRelationshipsEvents
    from ..models.shipment_data_relationships_order import ShipmentDataRelationshipsOrder
    from ..models.shipment_data_relationships_origin_address import ShipmentDataRelationshipsOriginAddress
    from ..models.shipment_data_relationships_parcels import ShipmentDataRelationshipsParcels
    from ..models.shipment_data_relationships_shipment_line_items import ShipmentDataRelationshipsShipmentLineItems
    from ..models.shipment_data_relationships_shipping_address import ShipmentDataRelationshipsShippingAddress
    from ..models.shipment_data_relationships_shipping_category import ShipmentDataRelationshipsShippingCategory
    from ..models.shipment_data_relationships_shipping_method import ShipmentDataRelationshipsShippingMethod
    from ..models.shipment_data_relationships_stock_line_items import ShipmentDataRelationshipsStockLineItems
    from ..models.shipment_data_relationships_stock_location import ShipmentDataRelationshipsStockLocation
    from ..models.shipment_data_relationships_stock_transfers import ShipmentDataRelationshipsStockTransfers


T = TypeVar("T", bound="ShipmentDataRelationships")


@attr.s(auto_attribs=True)
class ShipmentDataRelationships:
    """
    Attributes:
        order (Union[Unset, ShipmentDataRelationshipsOrder]):
        shipping_category (Union[Unset, ShipmentDataRelationshipsShippingCategory]):
        stock_location (Union[Unset, ShipmentDataRelationshipsStockLocation]):
        origin_address (Union[Unset, ShipmentDataRelationshipsOriginAddress]):
        shipping_address (Union[Unset, ShipmentDataRelationshipsShippingAddress]):
        shipping_method (Union[Unset, ShipmentDataRelationshipsShippingMethod]):
        delivery_lead_time (Union[Unset, ShipmentDataRelationshipsDeliveryLeadTime]):
        shipment_line_items (Union[Unset, ShipmentDataRelationshipsShipmentLineItems]):
        stock_line_items (Union[Unset, ShipmentDataRelationshipsStockLineItems]):
        stock_transfers (Union[Unset, ShipmentDataRelationshipsStockTransfers]):
        available_shipping_methods (Union[Unset, ShipmentDataRelationshipsAvailableShippingMethods]):
        carrier_accounts (Union[Unset, ShipmentDataRelationshipsCarrierAccounts]):
        parcels (Union[Unset, ShipmentDataRelationshipsParcels]):
        attachments (Union[Unset, ShipmentDataRelationshipsAttachments]):
        events (Union[Unset, ShipmentDataRelationshipsEvents]):
    """

    order: Union[Unset, "ShipmentDataRelationshipsOrder"] = UNSET
    shipping_category: Union[Unset, "ShipmentDataRelationshipsShippingCategory"] = UNSET
    stock_location: Union[Unset, "ShipmentDataRelationshipsStockLocation"] = UNSET
    origin_address: Union[Unset, "ShipmentDataRelationshipsOriginAddress"] = UNSET
    shipping_address: Union[Unset, "ShipmentDataRelationshipsShippingAddress"] = UNSET
    shipping_method: Union[Unset, "ShipmentDataRelationshipsShippingMethod"] = UNSET
    delivery_lead_time: Union[Unset, "ShipmentDataRelationshipsDeliveryLeadTime"] = UNSET
    shipment_line_items: Union[Unset, "ShipmentDataRelationshipsShipmentLineItems"] = UNSET
    stock_line_items: Union[Unset, "ShipmentDataRelationshipsStockLineItems"] = UNSET
    stock_transfers: Union[Unset, "ShipmentDataRelationshipsStockTransfers"] = UNSET
    available_shipping_methods: Union[Unset, "ShipmentDataRelationshipsAvailableShippingMethods"] = UNSET
    carrier_accounts: Union[Unset, "ShipmentDataRelationshipsCarrierAccounts"] = UNSET
    parcels: Union[Unset, "ShipmentDataRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "ShipmentDataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "ShipmentDataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        shipping_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_category, Unset):
            shipping_category = self.shipping_category.to_dict()

        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        origin_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_address, Unset):
            origin_address = self.origin_address.to_dict()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        shipping_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method, Unset):
            shipping_method = self.shipping_method.to_dict()

        delivery_lead_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_lead_time, Unset):
            delivery_lead_time = self.delivery_lead_time.to_dict()

        shipment_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_line_items, Unset):
            shipment_line_items = self.shipment_line_items.to_dict()

        stock_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_line_items, Unset):
            stock_line_items = self.stock_line_items.to_dict()

        stock_transfers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_transfers, Unset):
            stock_transfers = self.stock_transfers.to_dict()

        available_shipping_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_shipping_methods, Unset):
            available_shipping_methods = self.available_shipping_methods.to_dict()

        carrier_accounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.carrier_accounts, Unset):
            carrier_accounts = self.carrier_accounts.to_dict()

        parcels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parcels, Unset):
            parcels = self.parcels.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if shipping_category is not UNSET:
            field_dict["shipping_category"] = shipping_category
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if origin_address is not UNSET:
            field_dict["origin_address"] = origin_address
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method
        if delivery_lead_time is not UNSET:
            field_dict["delivery_lead_time"] = delivery_lead_time
        if shipment_line_items is not UNSET:
            field_dict["shipment_line_items"] = shipment_line_items
        if stock_line_items is not UNSET:
            field_dict["stock_line_items"] = stock_line_items
        if stock_transfers is not UNSET:
            field_dict["stock_transfers"] = stock_transfers
        if available_shipping_methods is not UNSET:
            field_dict["available_shipping_methods"] = available_shipping_methods
        if carrier_accounts is not UNSET:
            field_dict["carrier_accounts"] = carrier_accounts
        if parcels is not UNSET:
            field_dict["parcels"] = parcels
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_data_relationships_attachments import ShipmentDataRelationshipsAttachments
        from ..models.shipment_data_relationships_available_shipping_methods import (
            ShipmentDataRelationshipsAvailableShippingMethods,
        )
        from ..models.shipment_data_relationships_carrier_accounts import ShipmentDataRelationshipsCarrierAccounts
        from ..models.shipment_data_relationships_delivery_lead_time import ShipmentDataRelationshipsDeliveryLeadTime
        from ..models.shipment_data_relationships_events import ShipmentDataRelationshipsEvents
        from ..models.shipment_data_relationships_order import ShipmentDataRelationshipsOrder
        from ..models.shipment_data_relationships_origin_address import ShipmentDataRelationshipsOriginAddress
        from ..models.shipment_data_relationships_parcels import ShipmentDataRelationshipsParcels
        from ..models.shipment_data_relationships_shipment_line_items import ShipmentDataRelationshipsShipmentLineItems
        from ..models.shipment_data_relationships_shipping_address import ShipmentDataRelationshipsShippingAddress
        from ..models.shipment_data_relationships_shipping_category import ShipmentDataRelationshipsShippingCategory
        from ..models.shipment_data_relationships_shipping_method import ShipmentDataRelationshipsShippingMethod
        from ..models.shipment_data_relationships_stock_line_items import ShipmentDataRelationshipsStockLineItems
        from ..models.shipment_data_relationships_stock_location import ShipmentDataRelationshipsStockLocation
        from ..models.shipment_data_relationships_stock_transfers import ShipmentDataRelationshipsStockTransfers

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, ShipmentDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = ShipmentDataRelationshipsOrder.from_dict(_order)

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, ShipmentDataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = ShipmentDataRelationshipsShippingCategory.from_dict(_shipping_category)

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, ShipmentDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = ShipmentDataRelationshipsStockLocation.from_dict(_stock_location)

        _origin_address = d.pop("origin_address", UNSET)
        origin_address: Union[Unset, ShipmentDataRelationshipsOriginAddress]
        if isinstance(_origin_address, Unset):
            origin_address = UNSET
        else:
            origin_address = ShipmentDataRelationshipsOriginAddress.from_dict(_origin_address)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, ShipmentDataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ShipmentDataRelationshipsShippingAddress.from_dict(_shipping_address)

        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, ShipmentDataRelationshipsShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = ShipmentDataRelationshipsShippingMethod.from_dict(_shipping_method)

        _delivery_lead_time = d.pop("delivery_lead_time", UNSET)
        delivery_lead_time: Union[Unset, ShipmentDataRelationshipsDeliveryLeadTime]
        if isinstance(_delivery_lead_time, Unset):
            delivery_lead_time = UNSET
        else:
            delivery_lead_time = ShipmentDataRelationshipsDeliveryLeadTime.from_dict(_delivery_lead_time)

        _shipment_line_items = d.pop("shipment_line_items", UNSET)
        shipment_line_items: Union[Unset, ShipmentDataRelationshipsShipmentLineItems]
        if isinstance(_shipment_line_items, Unset):
            shipment_line_items = UNSET
        else:
            shipment_line_items = ShipmentDataRelationshipsShipmentLineItems.from_dict(_shipment_line_items)

        _stock_line_items = d.pop("stock_line_items", UNSET)
        stock_line_items: Union[Unset, ShipmentDataRelationshipsStockLineItems]
        if isinstance(_stock_line_items, Unset):
            stock_line_items = UNSET
        else:
            stock_line_items = ShipmentDataRelationshipsStockLineItems.from_dict(_stock_line_items)

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, ShipmentDataRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = ShipmentDataRelationshipsStockTransfers.from_dict(_stock_transfers)

        _available_shipping_methods = d.pop("available_shipping_methods", UNSET)
        available_shipping_methods: Union[Unset, ShipmentDataRelationshipsAvailableShippingMethods]
        if isinstance(_available_shipping_methods, Unset):
            available_shipping_methods = UNSET
        else:
            available_shipping_methods = ShipmentDataRelationshipsAvailableShippingMethods.from_dict(
                _available_shipping_methods
            )

        _carrier_accounts = d.pop("carrier_accounts", UNSET)
        carrier_accounts: Union[Unset, ShipmentDataRelationshipsCarrierAccounts]
        if isinstance(_carrier_accounts, Unset):
            carrier_accounts = UNSET
        else:
            carrier_accounts = ShipmentDataRelationshipsCarrierAccounts.from_dict(_carrier_accounts)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, ShipmentDataRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = ShipmentDataRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, ShipmentDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ShipmentDataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, ShipmentDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = ShipmentDataRelationshipsEvents.from_dict(_events)

        shipment_data_relationships = cls(
            order=order,
            shipping_category=shipping_category,
            stock_location=stock_location,
            origin_address=origin_address,
            shipping_address=shipping_address,
            shipping_method=shipping_method,
            delivery_lead_time=delivery_lead_time,
            shipment_line_items=shipment_line_items,
            stock_line_items=stock_line_items,
            stock_transfers=stock_transfers,
            available_shipping_methods=available_shipping_methods,
            carrier_accounts=carrier_accounts,
            parcels=parcels,
            attachments=attachments,
            events=events,
        )

        shipment_data_relationships.additional_properties = d
        return shipment_data_relationships

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
