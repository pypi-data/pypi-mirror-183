from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_attachments import (
        PATCHreturnsreturnIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_customer import (
        PATCHreturnsreturnIdResponse200DataRelationshipsCustomer,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_destination_address import (
        PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_events import (
        PATCHreturnsreturnIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_order import (
        PATCHreturnsreturnIdResponse200DataRelationshipsOrder,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_origin_address import (
        PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_return_line_items import (
        PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems,
    )
    from ..models.patc_hreturnsreturn_id_response_200_data_relationships_stock_location import (
        PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="PATCHreturnsreturnIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHreturnsreturnIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsOrder]):
        customer (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsCustomer]):
        stock_location (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation]):
        origin_address (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress]):
        destination_address (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress]):
        return_line_items (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems]):
        attachments (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsEvents]):
    """

    order: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsOrder"] = UNSET
    customer: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsCustomer"] = UNSET
    stock_location: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation"] = UNSET
    origin_address: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress"] = UNSET
    destination_address: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress"] = UNSET
    return_line_items: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems"] = UNSET
    attachments: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "PATCHreturnsreturnIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_attachments import (
            PATCHreturnsreturnIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_customer import (
            PATCHreturnsreturnIdResponse200DataRelationshipsCustomer,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_destination_address import (
            PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_events import (
            PATCHreturnsreturnIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_order import (
            PATCHreturnsreturnIdResponse200DataRelationshipsOrder,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_origin_address import (
            PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_return_line_items import (
            PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems,
        )
        from ..models.patc_hreturnsreturn_id_response_200_data_relationships_stock_location import (
            PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PATCHreturnsreturnIdResponse200DataRelationshipsOrder.from_dict(_order)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = PATCHreturnsreturnIdResponse200DataRelationshipsCustomer.from_dict(_customer)

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = PATCHreturnsreturnIdResponse200DataRelationshipsStockLocation.from_dict(_stock_location)

        _origin_address = d.pop("origin_address", UNSET)
        origin_address: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress]
        if isinstance(_origin_address, Unset):
            origin_address = UNSET
        else:
            origin_address = PATCHreturnsreturnIdResponse200DataRelationshipsOriginAddress.from_dict(_origin_address)

        _destination_address = d.pop("destination_address", UNSET)
        destination_address: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress]
        if isinstance(_destination_address, Unset):
            destination_address = UNSET
        else:
            destination_address = PATCHreturnsreturnIdResponse200DataRelationshipsDestinationAddress.from_dict(
                _destination_address
            )

        _return_line_items = d.pop("return_line_items", UNSET)
        return_line_items: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems]
        if isinstance(_return_line_items, Unset):
            return_line_items = UNSET
        else:
            return_line_items = PATCHreturnsreturnIdResponse200DataRelationshipsReturnLineItems.from_dict(
                _return_line_items
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHreturnsreturnIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHreturnsreturnIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHreturnsreturnIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_hreturnsreturn_id_response_200_data_relationships = cls(
            order=order,
            customer=customer,
            stock_location=stock_location,
            origin_address=origin_address,
            destination_address=destination_address,
            return_line_items=return_line_items,
            attachments=attachments,
            events=events,
        )

        patc_hreturnsreturn_id_response_200_data_relationships.additional_properties = d
        return patc_hreturnsreturn_id_response_200_data_relationships

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
