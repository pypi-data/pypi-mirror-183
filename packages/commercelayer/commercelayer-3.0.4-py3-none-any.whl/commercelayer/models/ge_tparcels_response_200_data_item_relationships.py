from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tparcels_response_200_data_item_relationships_attachments import (
        GETparcelsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tparcels_response_200_data_item_relationships_events import (
        GETparcelsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_tparcels_response_200_data_item_relationships_package import (
        GETparcelsResponse200DataItemRelationshipsPackage,
    )
    from ..models.ge_tparcels_response_200_data_item_relationships_parcel_line_items import (
        GETparcelsResponse200DataItemRelationshipsParcelLineItems,
    )
    from ..models.ge_tparcels_response_200_data_item_relationships_shipment import (
        GETparcelsResponse200DataItemRelationshipsShipment,
    )


T = TypeVar("T", bound="GETparcelsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETparcelsResponse200DataItemRelationships:
    """
    Attributes:
        shipment (Union[Unset, GETparcelsResponse200DataItemRelationshipsShipment]):
        package (Union[Unset, GETparcelsResponse200DataItemRelationshipsPackage]):
        parcel_line_items (Union[Unset, GETparcelsResponse200DataItemRelationshipsParcelLineItems]):
        attachments (Union[Unset, GETparcelsResponse200DataItemRelationshipsAttachments]):
        events (Union[Unset, GETparcelsResponse200DataItemRelationshipsEvents]):
    """

    shipment: Union[Unset, "GETparcelsResponse200DataItemRelationshipsShipment"] = UNSET
    package: Union[Unset, "GETparcelsResponse200DataItemRelationshipsPackage"] = UNSET
    parcel_line_items: Union[Unset, "GETparcelsResponse200DataItemRelationshipsParcelLineItems"] = UNSET
    attachments: Union[Unset, "GETparcelsResponse200DataItemRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETparcelsResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        parcel_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel_line_items, Unset):
            parcel_line_items = self.parcel_line_items.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if package is not UNSET:
            field_dict["package"] = package
        if parcel_line_items is not UNSET:
            field_dict["parcel_line_items"] = parcel_line_items
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tparcels_response_200_data_item_relationships_attachments import (
            GETparcelsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tparcels_response_200_data_item_relationships_events import (
            GETparcelsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_tparcels_response_200_data_item_relationships_package import (
            GETparcelsResponse200DataItemRelationshipsPackage,
        )
        from ..models.ge_tparcels_response_200_data_item_relationships_parcel_line_items import (
            GETparcelsResponse200DataItemRelationshipsParcelLineItems,
        )
        from ..models.ge_tparcels_response_200_data_item_relationships_shipment import (
            GETparcelsResponse200DataItemRelationshipsShipment,
        )

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, GETparcelsResponse200DataItemRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = GETparcelsResponse200DataItemRelationshipsShipment.from_dict(_shipment)

        _package = d.pop("package", UNSET)
        package: Union[Unset, GETparcelsResponse200DataItemRelationshipsPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = GETparcelsResponse200DataItemRelationshipsPackage.from_dict(_package)

        _parcel_line_items = d.pop("parcel_line_items", UNSET)
        parcel_line_items: Union[Unset, GETparcelsResponse200DataItemRelationshipsParcelLineItems]
        if isinstance(_parcel_line_items, Unset):
            parcel_line_items = UNSET
        else:
            parcel_line_items = GETparcelsResponse200DataItemRelationshipsParcelLineItems.from_dict(_parcel_line_items)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETparcelsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETparcelsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETparcelsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETparcelsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tparcels_response_200_data_item_relationships = cls(
            shipment=shipment,
            package=package,
            parcel_line_items=parcel_line_items,
            attachments=attachments,
            events=events,
        )

        ge_tparcels_response_200_data_item_relationships.additional_properties = d
        return ge_tparcels_response_200_data_item_relationships

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
