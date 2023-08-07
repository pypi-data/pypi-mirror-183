from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tparcels_response_201_data_relationships_attachments import (
        POSTparcelsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tparcels_response_201_data_relationships_events import (
        POSTparcelsResponse201DataRelationshipsEvents,
    )
    from ..models.pos_tparcels_response_201_data_relationships_package import (
        POSTparcelsResponse201DataRelationshipsPackage,
    )
    from ..models.pos_tparcels_response_201_data_relationships_parcel_line_items import (
        POSTparcelsResponse201DataRelationshipsParcelLineItems,
    )
    from ..models.pos_tparcels_response_201_data_relationships_shipment import (
        POSTparcelsResponse201DataRelationshipsShipment,
    )


T = TypeVar("T", bound="POSTparcelsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTparcelsResponse201DataRelationships:
    """
    Attributes:
        shipment (Union[Unset, POSTparcelsResponse201DataRelationshipsShipment]):
        package (Union[Unset, POSTparcelsResponse201DataRelationshipsPackage]):
        parcel_line_items (Union[Unset, POSTparcelsResponse201DataRelationshipsParcelLineItems]):
        attachments (Union[Unset, POSTparcelsResponse201DataRelationshipsAttachments]):
        events (Union[Unset, POSTparcelsResponse201DataRelationshipsEvents]):
    """

    shipment: Union[Unset, "POSTparcelsResponse201DataRelationshipsShipment"] = UNSET
    package: Union[Unset, "POSTparcelsResponse201DataRelationshipsPackage"] = UNSET
    parcel_line_items: Union[Unset, "POSTparcelsResponse201DataRelationshipsParcelLineItems"] = UNSET
    attachments: Union[Unset, "POSTparcelsResponse201DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "POSTparcelsResponse201DataRelationshipsEvents"] = UNSET
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
        from ..models.pos_tparcels_response_201_data_relationships_attachments import (
            POSTparcelsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tparcels_response_201_data_relationships_events import (
            POSTparcelsResponse201DataRelationshipsEvents,
        )
        from ..models.pos_tparcels_response_201_data_relationships_package import (
            POSTparcelsResponse201DataRelationshipsPackage,
        )
        from ..models.pos_tparcels_response_201_data_relationships_parcel_line_items import (
            POSTparcelsResponse201DataRelationshipsParcelLineItems,
        )
        from ..models.pos_tparcels_response_201_data_relationships_shipment import (
            POSTparcelsResponse201DataRelationshipsShipment,
        )

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, POSTparcelsResponse201DataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = POSTparcelsResponse201DataRelationshipsShipment.from_dict(_shipment)

        _package = d.pop("package", UNSET)
        package: Union[Unset, POSTparcelsResponse201DataRelationshipsPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = POSTparcelsResponse201DataRelationshipsPackage.from_dict(_package)

        _parcel_line_items = d.pop("parcel_line_items", UNSET)
        parcel_line_items: Union[Unset, POSTparcelsResponse201DataRelationshipsParcelLineItems]
        if isinstance(_parcel_line_items, Unset):
            parcel_line_items = UNSET
        else:
            parcel_line_items = POSTparcelsResponse201DataRelationshipsParcelLineItems.from_dict(_parcel_line_items)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTparcelsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTparcelsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, POSTparcelsResponse201DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = POSTparcelsResponse201DataRelationshipsEvents.from_dict(_events)

        pos_tparcels_response_201_data_relationships = cls(
            shipment=shipment,
            package=package,
            parcel_line_items=parcel_line_items,
            attachments=attachments,
            events=events,
        )

        pos_tparcels_response_201_data_relationships.additional_properties = d
        return pos_tparcels_response_201_data_relationships

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
