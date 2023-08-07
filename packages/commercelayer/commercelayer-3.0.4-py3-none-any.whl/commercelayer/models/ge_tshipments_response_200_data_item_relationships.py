from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipments_response_200_data_item_relationships_attachments import (
        GETshipmentsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_available_shipping_methods import (
        GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_carrier_accounts import (
        GETshipmentsResponse200DataItemRelationshipsCarrierAccounts,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_delivery_lead_time import (
        GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_events import (
        GETshipmentsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_order import (
        GETshipmentsResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_origin_address import (
        GETshipmentsResponse200DataItemRelationshipsOriginAddress,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_parcels import (
        GETshipmentsResponse200DataItemRelationshipsParcels,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_shipment_line_items import (
        GETshipmentsResponse200DataItemRelationshipsShipmentLineItems,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_shipping_address import (
        GETshipmentsResponse200DataItemRelationshipsShippingAddress,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_shipping_category import (
        GETshipmentsResponse200DataItemRelationshipsShippingCategory,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_shipping_method import (
        GETshipmentsResponse200DataItemRelationshipsShippingMethod,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_stock_line_items import (
        GETshipmentsResponse200DataItemRelationshipsStockLineItems,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_stock_location import (
        GETshipmentsResponse200DataItemRelationshipsStockLocation,
    )
    from ..models.ge_tshipments_response_200_data_item_relationships_stock_transfers import (
        GETshipmentsResponse200DataItemRelationshipsStockTransfers,
    )


T = TypeVar("T", bound="GETshipmentsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETshipmentsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETshipmentsResponse200DataItemRelationshipsOrder]):
        shipping_category (Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingCategory]):
        stock_location (Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockLocation]):
        origin_address (Union[Unset, GETshipmentsResponse200DataItemRelationshipsOriginAddress]):
        shipping_address (Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingAddress]):
        shipping_method (Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingMethod]):
        delivery_lead_time (Union[Unset, GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime]):
        shipment_line_items (Union[Unset, GETshipmentsResponse200DataItemRelationshipsShipmentLineItems]):
        stock_line_items (Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockLineItems]):
        stock_transfers (Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockTransfers]):
        available_shipping_methods (Union[Unset, GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods]):
        carrier_accounts (Union[Unset, GETshipmentsResponse200DataItemRelationshipsCarrierAccounts]):
        parcels (Union[Unset, GETshipmentsResponse200DataItemRelationshipsParcels]):
        attachments (Union[Unset, GETshipmentsResponse200DataItemRelationshipsAttachments]):
        events (Union[Unset, GETshipmentsResponse200DataItemRelationshipsEvents]):
    """

    order: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsOrder"] = UNSET
    shipping_category: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsShippingCategory"] = UNSET
    stock_location: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsStockLocation"] = UNSET
    origin_address: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsOriginAddress"] = UNSET
    shipping_address: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsShippingAddress"] = UNSET
    shipping_method: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsShippingMethod"] = UNSET
    delivery_lead_time: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime"] = UNSET
    shipment_line_items: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsShipmentLineItems"] = UNSET
    stock_line_items: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsStockLineItems"] = UNSET
    stock_transfers: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsStockTransfers"] = UNSET
    available_shipping_methods: Union[
        Unset, "GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods"
    ] = UNSET
    carrier_accounts: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsCarrierAccounts"] = UNSET
    parcels: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETshipmentsResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_tshipments_response_200_data_item_relationships_attachments import (
            GETshipmentsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_available_shipping_methods import (
            GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_carrier_accounts import (
            GETshipmentsResponse200DataItemRelationshipsCarrierAccounts,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_delivery_lead_time import (
            GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_events import (
            GETshipmentsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_order import (
            GETshipmentsResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_origin_address import (
            GETshipmentsResponse200DataItemRelationshipsOriginAddress,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_parcels import (
            GETshipmentsResponse200DataItemRelationshipsParcels,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_shipment_line_items import (
            GETshipmentsResponse200DataItemRelationshipsShipmentLineItems,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_shipping_address import (
            GETshipmentsResponse200DataItemRelationshipsShippingAddress,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_shipping_category import (
            GETshipmentsResponse200DataItemRelationshipsShippingCategory,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_shipping_method import (
            GETshipmentsResponse200DataItemRelationshipsShippingMethod,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_stock_line_items import (
            GETshipmentsResponse200DataItemRelationshipsStockLineItems,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_stock_location import (
            GETshipmentsResponse200DataItemRelationshipsStockLocation,
        )
        from ..models.ge_tshipments_response_200_data_item_relationships_stock_transfers import (
            GETshipmentsResponse200DataItemRelationshipsStockTransfers,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETshipmentsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETshipmentsResponse200DataItemRelationshipsOrder.from_dict(_order)

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = GETshipmentsResponse200DataItemRelationshipsShippingCategory.from_dict(
                _shipping_category
            )

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETshipmentsResponse200DataItemRelationshipsStockLocation.from_dict(_stock_location)

        _origin_address = d.pop("origin_address", UNSET)
        origin_address: Union[Unset, GETshipmentsResponse200DataItemRelationshipsOriginAddress]
        if isinstance(_origin_address, Unset):
            origin_address = UNSET
        else:
            origin_address = GETshipmentsResponse200DataItemRelationshipsOriginAddress.from_dict(_origin_address)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = GETshipmentsResponse200DataItemRelationshipsShippingAddress.from_dict(_shipping_address)

        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, GETshipmentsResponse200DataItemRelationshipsShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = GETshipmentsResponse200DataItemRelationshipsShippingMethod.from_dict(_shipping_method)

        _delivery_lead_time = d.pop("delivery_lead_time", UNSET)
        delivery_lead_time: Union[Unset, GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime]
        if isinstance(_delivery_lead_time, Unset):
            delivery_lead_time = UNSET
        else:
            delivery_lead_time = GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTime.from_dict(
                _delivery_lead_time
            )

        _shipment_line_items = d.pop("shipment_line_items", UNSET)
        shipment_line_items: Union[Unset, GETshipmentsResponse200DataItemRelationshipsShipmentLineItems]
        if isinstance(_shipment_line_items, Unset):
            shipment_line_items = UNSET
        else:
            shipment_line_items = GETshipmentsResponse200DataItemRelationshipsShipmentLineItems.from_dict(
                _shipment_line_items
            )

        _stock_line_items = d.pop("stock_line_items", UNSET)
        stock_line_items: Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockLineItems]
        if isinstance(_stock_line_items, Unset):
            stock_line_items = UNSET
        else:
            stock_line_items = GETshipmentsResponse200DataItemRelationshipsStockLineItems.from_dict(_stock_line_items)

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, GETshipmentsResponse200DataItemRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = GETshipmentsResponse200DataItemRelationshipsStockTransfers.from_dict(_stock_transfers)

        _available_shipping_methods = d.pop("available_shipping_methods", UNSET)
        available_shipping_methods: Union[Unset, GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods]
        if isinstance(_available_shipping_methods, Unset):
            available_shipping_methods = UNSET
        else:
            available_shipping_methods = GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethods.from_dict(
                _available_shipping_methods
            )

        _carrier_accounts = d.pop("carrier_accounts", UNSET)
        carrier_accounts: Union[Unset, GETshipmentsResponse200DataItemRelationshipsCarrierAccounts]
        if isinstance(_carrier_accounts, Unset):
            carrier_accounts = UNSET
        else:
            carrier_accounts = GETshipmentsResponse200DataItemRelationshipsCarrierAccounts.from_dict(_carrier_accounts)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, GETshipmentsResponse200DataItemRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = GETshipmentsResponse200DataItemRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETshipmentsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETshipmentsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETshipmentsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETshipmentsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tshipments_response_200_data_item_relationships = cls(
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

        ge_tshipments_response_200_data_item_relationships.additional_properties = d
        return ge_tshipments_response_200_data_item_relationships

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
