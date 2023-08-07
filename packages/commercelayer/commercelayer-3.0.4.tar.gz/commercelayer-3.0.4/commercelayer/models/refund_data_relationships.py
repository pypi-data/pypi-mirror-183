from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refund_data_relationships_events import RefundDataRelationshipsEvents
    from ..models.refund_data_relationships_order import RefundDataRelationshipsOrder
    from ..models.refund_data_relationships_reference_capture import RefundDataRelationshipsReferenceCapture


T = TypeVar("T", bound="RefundDataRelationships")


@attr.s(auto_attribs=True)
class RefundDataRelationships:
    """
    Attributes:
        order (Union[Unset, RefundDataRelationshipsOrder]):
        reference_capture (Union[Unset, RefundDataRelationshipsReferenceCapture]):
        events (Union[Unset, RefundDataRelationshipsEvents]):
    """

    order: Union[Unset, "RefundDataRelationshipsOrder"] = UNSET
    reference_capture: Union[Unset, "RefundDataRelationshipsReferenceCapture"] = UNSET
    events: Union[Unset, "RefundDataRelationshipsEvents"] = UNSET
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
        from ..models.refund_data_relationships_events import RefundDataRelationshipsEvents
        from ..models.refund_data_relationships_order import RefundDataRelationshipsOrder
        from ..models.refund_data_relationships_reference_capture import RefundDataRelationshipsReferenceCapture

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, RefundDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = RefundDataRelationshipsOrder.from_dict(_order)

        _reference_capture = d.pop("reference_capture", UNSET)
        reference_capture: Union[Unset, RefundDataRelationshipsReferenceCapture]
        if isinstance(_reference_capture, Unset):
            reference_capture = UNSET
        else:
            reference_capture = RefundDataRelationshipsReferenceCapture.from_dict(_reference_capture)

        _events = d.pop("events", UNSET)
        events: Union[Unset, RefundDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = RefundDataRelationshipsEvents.from_dict(_events)

        refund_data_relationships = cls(
            order=order,
            reference_capture=reference_capture,
            events=events,
        )

        refund_data_relationships.additional_properties = d
        return refund_data_relationships

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
