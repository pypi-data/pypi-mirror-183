from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_trefunds_response_200_data_item_relationships_events import (
        GETrefundsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_trefunds_response_200_data_item_relationships_order import (
        GETrefundsResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_trefunds_response_200_data_item_relationships_reference_capture import (
        GETrefundsResponse200DataItemRelationshipsReferenceCapture,
    )


T = TypeVar("T", bound="GETrefundsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETrefundsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETrefundsResponse200DataItemRelationshipsOrder]):
        reference_capture (Union[Unset, GETrefundsResponse200DataItemRelationshipsReferenceCapture]):
        events (Union[Unset, GETrefundsResponse200DataItemRelationshipsEvents]):
    """

    order: Union[Unset, "GETrefundsResponse200DataItemRelationshipsOrder"] = UNSET
    reference_capture: Union[Unset, "GETrefundsResponse200DataItemRelationshipsReferenceCapture"] = UNSET
    events: Union[Unset, "GETrefundsResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        reference_capture: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reference_capture, Unset):
            reference_capture = self.reference_capture.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if reference_capture is not UNSET:
            field_dict["reference_capture"] = reference_capture
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_trefunds_response_200_data_item_relationships_events import (
            GETrefundsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_trefunds_response_200_data_item_relationships_order import (
            GETrefundsResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_trefunds_response_200_data_item_relationships_reference_capture import (
            GETrefundsResponse200DataItemRelationshipsReferenceCapture,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETrefundsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETrefundsResponse200DataItemRelationshipsOrder.from_dict(_order)

        _reference_capture = d.pop("reference_capture", UNSET)
        reference_capture: Union[Unset, GETrefundsResponse200DataItemRelationshipsReferenceCapture]
        if isinstance(_reference_capture, Unset):
            reference_capture = UNSET
        else:
            reference_capture = GETrefundsResponse200DataItemRelationshipsReferenceCapture.from_dict(_reference_capture)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETrefundsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETrefundsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_trefunds_response_200_data_item_relationships = cls(
            order=order,
            reference_capture=reference_capture,
            events=events,
        )

        ge_trefunds_response_200_data_item_relationships.additional_properties = d
        return ge_trefunds_response_200_data_item_relationships

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
