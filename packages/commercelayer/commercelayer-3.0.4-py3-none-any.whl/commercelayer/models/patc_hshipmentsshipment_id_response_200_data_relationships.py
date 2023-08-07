from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_attachments import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_available_shipping_methods import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_carrier_accounts import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_events import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_order import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_origin_address import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_parcels import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipment_line_items import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_address import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_category import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_method import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_line_items import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_location import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_transfers import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers,
    )


T = TypeVar("T", bound="PATCHshipmentsshipmentIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHshipmentsshipmentIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder]):
        shipping_category (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory]):
        stock_location (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation]):
        origin_address (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress]):
        shipping_address (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress]):
        shipping_method (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod]):
        delivery_lead_time (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime]):
        shipment_line_items (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems]):
        stock_line_items (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems]):
        stock_transfers (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers]):
        available_shipping_methods (Union[Unset,
            PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods]):
        carrier_accounts (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts]):
        parcels (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels]):
        attachments (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents]):
    """

    order: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder"] = UNSET
    shipping_category: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory"] = UNSET
    stock_location: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation"] = UNSET
    origin_address: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress"] = UNSET
    shipping_address: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress"] = UNSET
    shipping_method: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod"] = UNSET
    delivery_lead_time: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime"] = UNSET
    shipment_line_items: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems"] = UNSET
    stock_line_items: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems"] = UNSET
    stock_transfers: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers"] = UNSET
    available_shipping_methods: Union[
        Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods"
    ] = UNSET
    carrier_accounts: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts"] = UNSET
    parcels: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_attachments import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_available_shipping_methods import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_carrier_accounts import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_events import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_order import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_origin_address import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_parcels import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipment_line_items import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_address import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_category import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_shipping_method import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_line_items import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_location import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_stock_transfers import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PATCHshipmentsshipmentIdResponse200DataRelationshipsOrder.from_dict(_order)

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingCategory.from_dict(
                _shipping_category
            )

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLocation.from_dict(
                _stock_location
            )

        _origin_address = d.pop("origin_address", UNSET)
        origin_address: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress]
        if isinstance(_origin_address, Unset):
            origin_address = UNSET
        else:
            origin_address = PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddress.from_dict(
                _origin_address
            )

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingAddress.from_dict(
                _shipping_address
            )

        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = PATCHshipmentsshipmentIdResponse200DataRelationshipsShippingMethod.from_dict(
                _shipping_method
            )

        _delivery_lead_time = d.pop("delivery_lead_time", UNSET)
        delivery_lead_time: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime]
        if isinstance(_delivery_lead_time, Unset):
            delivery_lead_time = UNSET
        else:
            delivery_lead_time = PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime.from_dict(
                _delivery_lead_time
            )

        _shipment_line_items = d.pop("shipment_line_items", UNSET)
        shipment_line_items: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems]
        if isinstance(_shipment_line_items, Unset):
            shipment_line_items = UNSET
        else:
            shipment_line_items = PATCHshipmentsshipmentIdResponse200DataRelationshipsShipmentLineItems.from_dict(
                _shipment_line_items
            )

        _stock_line_items = d.pop("stock_line_items", UNSET)
        stock_line_items: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems]
        if isinstance(_stock_line_items, Unset):
            stock_line_items = UNSET
        else:
            stock_line_items = PATCHshipmentsshipmentIdResponse200DataRelationshipsStockLineItems.from_dict(
                _stock_line_items
            )

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = PATCHshipmentsshipmentIdResponse200DataRelationshipsStockTransfers.from_dict(
                _stock_transfers
            )

        _available_shipping_methods = d.pop("available_shipping_methods", UNSET)
        available_shipping_methods: Union[
            Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods
        ]
        if isinstance(_available_shipping_methods, Unset):
            available_shipping_methods = UNSET
        else:
            available_shipping_methods = (
                PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethods.from_dict(
                    _available_shipping_methods
                )
            )

        _carrier_accounts = d.pop("carrier_accounts", UNSET)
        carrier_accounts: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts]
        if isinstance(_carrier_accounts, Unset):
            carrier_accounts = UNSET
        else:
            carrier_accounts = PATCHshipmentsshipmentIdResponse200DataRelationshipsCarrierAccounts.from_dict(
                _carrier_accounts
            )

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = PATCHshipmentsshipmentIdResponse200DataRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHshipmentsshipmentIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHshipmentsshipmentIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_hshipmentsshipment_id_response_200_data_relationships = cls(
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

        patc_hshipmentsshipment_id_response_200_data_relationships.additional_properties = d
        return patc_hshipmentsshipment_id_response_200_data_relationships

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
