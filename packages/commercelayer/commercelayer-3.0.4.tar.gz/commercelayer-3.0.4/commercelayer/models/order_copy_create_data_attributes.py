from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_copy_create_data_attributes_metadata import OrderCopyCreateDataAttributesMetadata


T = TypeVar("T", bound="OrderCopyCreateDataAttributes")


@attr.s(auto_attribs=True)
class OrderCopyCreateDataAttributes:
    """
    Attributes:
        place_target_order (Union[Unset, bool]): Indicates if the target order must be placed upon copy. Example: True.
        cancel_source_order (Union[Unset, bool]): Indicates if the source order must be cancelled upon copy. Example:
            True.
        reuse_wallet (Union[Unset, bool]): Indicates if the payment source within the source order customer's wallet
            must be copied. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, OrderCopyCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to
            the resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    place_target_order: Union[Unset, bool] = UNSET
    cancel_source_order: Union[Unset, bool] = UNSET
    reuse_wallet: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "OrderCopyCreateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place_target_order = self.place_target_order
        cancel_source_order = self.cancel_source_order
        reuse_wallet = self.reuse_wallet
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place_target_order is not UNSET:
            field_dict["place_target_order"] = place_target_order
        if cancel_source_order is not UNSET:
            field_dict["cancel_source_order"] = cancel_source_order
        if reuse_wallet is not UNSET:
            field_dict["reuse_wallet"] = reuse_wallet
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_copy_create_data_attributes_metadata import OrderCopyCreateDataAttributesMetadata

        d = src_dict.copy()
        place_target_order = d.pop("place_target_order", UNSET)

        cancel_source_order = d.pop("cancel_source_order", UNSET)

        reuse_wallet = d.pop("reuse_wallet", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderCopyCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderCopyCreateDataAttributesMetadata.from_dict(_metadata)

        order_copy_create_data_attributes = cls(
            place_target_order=place_target_order,
            cancel_source_order=cancel_source_order,
            reuse_wallet=reuse_wallet,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        order_copy_create_data_attributes.additional_properties = d
        return order_copy_create_data_attributes

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
