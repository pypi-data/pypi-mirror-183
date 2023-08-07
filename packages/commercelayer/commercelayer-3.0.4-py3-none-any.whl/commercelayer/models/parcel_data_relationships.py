from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parcel_data_relationships_attachments import ParcelDataRelationshipsAttachments
    from ..models.parcel_data_relationships_events import ParcelDataRelationshipsEvents
    from ..models.parcel_data_relationships_package import ParcelDataRelationshipsPackage
    from ..models.parcel_data_relationships_parcel_line_items import ParcelDataRelationshipsParcelLineItems
    from ..models.parcel_data_relationships_shipment import ParcelDataRelationshipsShipment


T = TypeVar("T", bound="ParcelDataRelationships")


@attr.s(auto_attribs=True)
class ParcelDataRelationships:
    """
    Attributes:
        shipment (Union[Unset, ParcelDataRelationshipsShipment]):
        package (Union[Unset, ParcelDataRelationshipsPackage]):
        parcel_line_items (Union[Unset, ParcelDataRelationshipsParcelLineItems]):
        attachments (Union[Unset, ParcelDataRelationshipsAttachments]):
        events (Union[Unset, ParcelDataRelationshipsEvents]):
    """

    shipment: Union[Unset, "ParcelDataRelationshipsShipment"] = UNSET
    package: Union[Unset, "ParcelDataRelationshipsPackage"] = UNSET
    parcel_line_items: Union[Unset, "ParcelDataRelationshipsParcelLineItems"] = UNSET
    attachments: Union[Unset, "ParcelDataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "ParcelDataRelationshipsEvents"] = UNSET
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
        from ..models.parcel_data_relationships_attachments import ParcelDataRelationshipsAttachments
        from ..models.parcel_data_relationships_events import ParcelDataRelationshipsEvents
        from ..models.parcel_data_relationships_package import ParcelDataRelationshipsPackage
        from ..models.parcel_data_relationships_parcel_line_items import ParcelDataRelationshipsParcelLineItems
        from ..models.parcel_data_relationships_shipment import ParcelDataRelationshipsShipment

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, ParcelDataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = ParcelDataRelationshipsShipment.from_dict(_shipment)

        _package = d.pop("package", UNSET)
        package: Union[Unset, ParcelDataRelationshipsPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = ParcelDataRelationshipsPackage.from_dict(_package)

        _parcel_line_items = d.pop("parcel_line_items", UNSET)
        parcel_line_items: Union[Unset, ParcelDataRelationshipsParcelLineItems]
        if isinstance(_parcel_line_items, Unset):
            parcel_line_items = UNSET
        else:
            parcel_line_items = ParcelDataRelationshipsParcelLineItems.from_dict(_parcel_line_items)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, ParcelDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ParcelDataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, ParcelDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = ParcelDataRelationshipsEvents.from_dict(_events)

        parcel_data_relationships = cls(
            shipment=shipment,
            package=package,
            parcel_line_items=parcel_line_items,
            attachments=attachments,
            events=events,
        )

        parcel_data_relationships.additional_properties = d
        return parcel_data_relationships

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
