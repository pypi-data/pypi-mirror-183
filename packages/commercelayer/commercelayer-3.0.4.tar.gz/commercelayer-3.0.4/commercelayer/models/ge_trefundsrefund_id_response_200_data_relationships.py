from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_trefundsrefund_id_response_200_data_relationships_events import (
        GETrefundsrefundIdResponse200DataRelationshipsEvents,
    )
    from ..models.ge_trefundsrefund_id_response_200_data_relationships_order import (
        GETrefundsrefundIdResponse200DataRelationshipsOrder,
    )
    from ..models.ge_trefundsrefund_id_response_200_data_relationships_reference_capture import (
        GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture,
    )


T = TypeVar("T", bound="GETrefundsrefundIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETrefundsrefundIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsOrder]):
        reference_capture (Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture]):
        events (Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsEvents]):
    """

    order: Union[Unset, "GETrefundsrefundIdResponse200DataRelationshipsOrder"] = UNSET
    reference_capture: Union[Unset, "GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture"] = UNSET
    events: Union[Unset, "GETrefundsrefundIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.ge_trefundsrefund_id_response_200_data_relationships_events import (
            GETrefundsrefundIdResponse200DataRelationshipsEvents,
        )
        from ..models.ge_trefundsrefund_id_response_200_data_relationships_order import (
            GETrefundsrefundIdResponse200DataRelationshipsOrder,
        )
        from ..models.ge_trefundsrefund_id_response_200_data_relationships_reference_capture import (
            GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETrefundsrefundIdResponse200DataRelationshipsOrder.from_dict(_order)

        _reference_capture = d.pop("reference_capture", UNSET)
        reference_capture: Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture]
        if isinstance(_reference_capture, Unset):
            reference_capture = UNSET
        else:
            reference_capture = GETrefundsrefundIdResponse200DataRelationshipsReferenceCapture.from_dict(
                _reference_capture
            )

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETrefundsrefundIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETrefundsrefundIdResponse200DataRelationshipsEvents.from_dict(_events)

        ge_trefundsrefund_id_response_200_data_relationships = cls(
            order=order,
            reference_capture=reference_capture,
            events=events,
        )

        ge_trefundsrefund_id_response_200_data_relationships.additional_properties = d
        return ge_trefundsrefund_id_response_200_data_relationships

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
