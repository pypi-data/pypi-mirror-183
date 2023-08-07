from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_treturns_response_200_data_item_relationships_attachments import (
        GETreturnsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_customer import (
        GETreturnsResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_destination_address import (
        GETreturnsResponse200DataItemRelationshipsDestinationAddress,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_events import (
        GETreturnsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_order import (
        GETreturnsResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_origin_address import (
        GETreturnsResponse200DataItemRelationshipsOriginAddress,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_return_line_items import (
        GETreturnsResponse200DataItemRelationshipsReturnLineItems,
    )
    from ..models.ge_treturns_response_200_data_item_relationships_stock_location import (
        GETreturnsResponse200DataItemRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETreturnsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETreturnsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETreturnsResponse200DataItemRelationshipsOrder]):
        customer (Union[Unset, GETreturnsResponse200DataItemRelationshipsCustomer]):
        stock_location (Union[Unset, GETreturnsResponse200DataItemRelationshipsStockLocation]):
        origin_address (Union[Unset, GETreturnsResponse200DataItemRelationshipsOriginAddress]):
        destination_address (Union[Unset, GETreturnsResponse200DataItemRelationshipsDestinationAddress]):
        return_line_items (Union[Unset, GETreturnsResponse200DataItemRelationshipsReturnLineItems]):
        attachments (Union[Unset, GETreturnsResponse200DataItemRelationshipsAttachments]):
        events (Union[Unset, GETreturnsResponse200DataItemRelationshipsEvents]):
    """

    order: Union[Unset, "GETreturnsResponse200DataItemRelationshipsOrder"] = UNSET
    customer: Union[Unset, "GETreturnsResponse200DataItemRelationshipsCustomer"] = UNSET
    stock_location: Union[Unset, "GETreturnsResponse200DataItemRelationshipsStockLocation"] = UNSET
    origin_address: Union[Unset, "GETreturnsResponse200DataItemRelationshipsOriginAddress"] = UNSET
    destination_address: Union[Unset, "GETreturnsResponse200DataItemRelationshipsDestinationAddress"] = UNSET
    return_line_items: Union[Unset, "GETreturnsResponse200DataItemRelationshipsReturnLineItems"] = UNSET
    attachments: Union[Unset, "GETreturnsResponse200DataItemRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETreturnsResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        origin_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_address, Unset):
            origin_address = self.origin_address.to_dict()

        destination_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination_address, Unset):
            destination_address = self.destination_address.to_dict()

        return_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_line_items, Unset):
            return_line_items = self.return_line_items.to_dict()

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
        if customer is not UNSET:
            field_dict["customer"] = customer
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if origin_address is not UNSET:
            field_dict["origin_address"] = origin_address
        if destination_address is not UNSET:
            field_dict["destination_address"] = destination_address
        if return_line_items is not UNSET:
            field_dict["return_line_items"] = return_line_items
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_treturns_response_200_data_item_relationships_attachments import (
            GETreturnsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_customer import (
            GETreturnsResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_destination_address import (
            GETreturnsResponse200DataItemRelationshipsDestinationAddress,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_events import (
            GETreturnsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_order import (
            GETreturnsResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_origin_address import (
            GETreturnsResponse200DataItemRelationshipsOriginAddress,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_return_line_items import (
            GETreturnsResponse200DataItemRelationshipsReturnLineItems,
        )
        from ..models.ge_treturns_response_200_data_item_relationships_stock_location import (
            GETreturnsResponse200DataItemRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETreturnsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETreturnsResponse200DataItemRelationshipsOrder.from_dict(_order)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETreturnsResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETreturnsResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETreturnsResponse200DataItemRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETreturnsResponse200DataItemRelationshipsStockLocation.from_dict(_stock_location)

        _origin_address = d.pop("origin_address", UNSET)
        origin_address: Union[Unset, GETreturnsResponse200DataItemRelationshipsOriginAddress]
        if isinstance(_origin_address, Unset):
            origin_address = UNSET
        else:
            origin_address = GETreturnsResponse200DataItemRelationshipsOriginAddress.from_dict(_origin_address)

        _destination_address = d.pop("destination_address", UNSET)
        destination_address: Union[Unset, GETreturnsResponse200DataItemRelationshipsDestinationAddress]
        if isinstance(_destination_address, Unset):
            destination_address = UNSET
        else:
            destination_address = GETreturnsResponse200DataItemRelationshipsDestinationAddress.from_dict(
                _destination_address
            )

        _return_line_items = d.pop("return_line_items", UNSET)
        return_line_items: Union[Unset, GETreturnsResponse200DataItemRelationshipsReturnLineItems]
        if isinstance(_return_line_items, Unset):
            return_line_items = UNSET
        else:
            return_line_items = GETreturnsResponse200DataItemRelationshipsReturnLineItems.from_dict(_return_line_items)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETreturnsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETreturnsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETreturnsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETreturnsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_treturns_response_200_data_item_relationships = cls(
            order=order,
            customer=customer,
            stock_location=stock_location,
            origin_address=origin_address,
            destination_address=destination_address,
            return_line_items=return_line_items,
            attachments=attachments,
            events=events,
        )

        ge_treturns_response_200_data_item_relationships.additional_properties = d
        return ge_treturns_response_200_data_item_relationships

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
