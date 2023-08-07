from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capture_update_data_attributes_metadata import CaptureUpdateDataAttributesMetadata


T = TypeVar("T", bound="CaptureUpdateDataAttributes")


@attr.s(auto_attribs=True)
class CaptureUpdateDataAttributes:
    """
    Attributes:
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, CaptureUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
        refund (Union[Unset, bool]): Send this attribute if you want to create a refund for this capture. Example: True.
        refund_amount_cents (Union[Unset, int]): The associated refund amount, in cents. Example: 500.
    """

    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CaptureUpdateDataAttributesMetadata"] = UNSET
    refund: Union[Unset, bool] = UNSET
    refund_amount_cents: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        refund = self.refund
        refund_amount_cents = self.refund_amount_cents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if refund is not UNSET:
            field_dict["_refund"] = refund
        if refund_amount_cents is not UNSET:
            field_dict["_refund_amount_cents"] = refund_amount_cents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capture_update_data_attributes_metadata import CaptureUpdateDataAttributesMetadata

        d = src_dict.copy()
        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CaptureUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CaptureUpdateDataAttributesMetadata.from_dict(_metadata)

        refund = d.pop("_refund", UNSET)

        refund_amount_cents = d.pop("_refund_amount_cents", UNSET)

        capture_update_data_attributes = cls(
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
            refund=refund,
            refund_amount_cents=refund_amount_cents,
        )

        capture_update_data_attributes.additional_properties = d
        return capture_update_data_attributes

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
