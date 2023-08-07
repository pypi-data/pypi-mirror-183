from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes_metadata import (
        PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata,
    )
    from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes_return_reason import (
        PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason,
    )


T = TypeVar("T", bound="PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributes:
    """
    Attributes:
        quantity (Union[Unset, int]): The line item quantity. Example: 4.
        restock (Union[Unset, bool]): Send this attribute if you want to restock the line item. Example: True.
        return_reason (Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason]): Set of
            key-value pairs that you can use to add details about return reason. Example: {'size': 'was wrong'}.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    quantity: Union[Unset, int] = UNSET
    restock: Union[Unset, bool] = UNSET
    return_reason: Union[Unset, "PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason"] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        restock = self.restock
        return_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_reason, Unset):
            return_reason = self.return_reason.to_dict()

        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if restock is not UNSET:
            field_dict["_restock"] = restock
        if return_reason is not UNSET:
            field_dict["return_reason"] = return_reason
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes_metadata import (
            PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata,
        )
        from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes_return_reason import (
            PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason,
        )

        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        restock = d.pop("_restock", UNSET)

        _return_reason = d.pop("return_reason", UNSET)
        return_reason: Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason]
        if isinstance(_return_reason, Unset):
            return_reason = UNSET
        else:
            return_reason = PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesReturnReason.from_dict(
                _return_reason
            )

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHreturnLineItemsreturnLineItemIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes = cls(
            quantity=quantity,
            restock=restock,
            return_reason=return_reason,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes.additional_properties = d
        return patc_hreturn_line_itemsreturn_line_item_id_response_200_data_attributes

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
