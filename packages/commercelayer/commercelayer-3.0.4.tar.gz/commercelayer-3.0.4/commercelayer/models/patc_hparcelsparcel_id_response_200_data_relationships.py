from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hparcelsparcel_id_response_200_data_relationships_attachments import (
        PATCHparcelsparcelIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hparcelsparcel_id_response_200_data_relationships_events import (
        PATCHparcelsparcelIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_hparcelsparcel_id_response_200_data_relationships_package import (
        PATCHparcelsparcelIdResponse200DataRelationshipsPackage,
    )
    from ..models.patc_hparcelsparcel_id_response_200_data_relationships_parcel_line_items import (
        PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems,
    )
    from ..models.patc_hparcelsparcel_id_response_200_data_relationships_shipment import (
        PATCHparcelsparcelIdResponse200DataRelationshipsShipment,
    )


T = TypeVar("T", bound="PATCHparcelsparcelIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHparcelsparcelIdResponse200DataRelationships:
    """
    Attributes:
        shipment (Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsShipment]):
        package (Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsPackage]):
        parcel_line_items (Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems]):
        attachments (Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsEvents]):
    """

    shipment: Union[Unset, "PATCHparcelsparcelIdResponse200DataRelationshipsShipment"] = UNSET
    package: Union[Unset, "PATCHparcelsparcelIdResponse200DataRelationshipsPackage"] = UNSET
    parcel_line_items: Union[Unset, "PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems"] = UNSET
    attachments: Union[Unset, "PATCHparcelsparcelIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "PATCHparcelsparcelIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.patc_hparcelsparcel_id_response_200_data_relationships_attachments import (
            PATCHparcelsparcelIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hparcelsparcel_id_response_200_data_relationships_events import (
            PATCHparcelsparcelIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_hparcelsparcel_id_response_200_data_relationships_package import (
            PATCHparcelsparcelIdResponse200DataRelationshipsPackage,
        )
        from ..models.patc_hparcelsparcel_id_response_200_data_relationships_parcel_line_items import (
            PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems,
        )
        from ..models.patc_hparcelsparcel_id_response_200_data_relationships_shipment import (
            PATCHparcelsparcelIdResponse200DataRelationshipsShipment,
        )

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = PATCHparcelsparcelIdResponse200DataRelationshipsShipment.from_dict(_shipment)

        _package = d.pop("package", UNSET)
        package: Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = PATCHparcelsparcelIdResponse200DataRelationshipsPackage.from_dict(_package)

        _parcel_line_items = d.pop("parcel_line_items", UNSET)
        parcel_line_items: Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems]
        if isinstance(_parcel_line_items, Unset):
            parcel_line_items = UNSET
        else:
            parcel_line_items = PATCHparcelsparcelIdResponse200DataRelationshipsParcelLineItems.from_dict(
                _parcel_line_items
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHparcelsparcelIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHparcelsparcelIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHparcelsparcelIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_hparcelsparcel_id_response_200_data_relationships = cls(
            shipment=shipment,
            package=package,
            parcel_line_items=parcel_line_items,
            attachments=attachments,
            events=events,
        )

        patc_hparcelsparcel_id_response_200_data_relationships.additional_properties = d
        return patc_hparcelsparcel_id_response_200_data_relationships

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
