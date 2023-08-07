from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_treturn_line_items_response_200_data_item_attributes_metadata import (
        GETreturnLineItemsResponse200DataItemAttributesMetadata,
    )
    from ..models.ge_treturn_line_items_response_200_data_item_attributes_return_reason import (
        GETreturnLineItemsResponse200DataItemAttributesReturnReason,
    )


T = TypeVar("T", bound="GETreturnLineItemsResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETreturnLineItemsResponse200DataItemAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        bundle_code (Union[Unset, str]): The code of the associated bundle. Example: BUNDLEMM000000FFFFFFXLXX.
        name (Union[Unset, str]): The name of the line item. Example: Black Men T-shirt with White Logo (XL).
        quantity (Union[Unset, int]): The line item quantity. Example: 4.
        return_reason (Union[Unset, GETreturnLineItemsResponse200DataItemAttributesReturnReason]): Set of key-value
            pairs that you can use to add details about return reason. Example: {'size': 'was wrong'}.
        restocked_at (Union[Unset, str]): Time at which the return line item was restocked. Example:
            2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETreturnLineItemsResponse200DataItemAttributesMetadata]): Set of key-value pairs that
            you can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    bundle_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    return_reason: Union[Unset, "GETreturnLineItemsResponse200DataItemAttributesReturnReason"] = UNSET
    restocked_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETreturnLineItemsResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        bundle_code = self.bundle_code
        name = self.name
        quantity = self.quantity
        return_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_reason, Unset):
            return_reason = self.return_reason.to_dict()

        restocked_at = self.restocked_at
        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if bundle_code is not UNSET:
            field_dict["bundle_code"] = bundle_code
        if name is not UNSET:
            field_dict["name"] = name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if return_reason is not UNSET:
            field_dict["return_reason"] = return_reason
        if restocked_at is not UNSET:
            field_dict["restocked_at"] = restocked_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_treturn_line_items_response_200_data_item_attributes_metadata import (
            GETreturnLineItemsResponse200DataItemAttributesMetadata,
        )
        from ..models.ge_treturn_line_items_response_200_data_item_attributes_return_reason import (
            GETreturnLineItemsResponse200DataItemAttributesReturnReason,
        )

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        bundle_code = d.pop("bundle_code", UNSET)

        name = d.pop("name", UNSET)

        quantity = d.pop("quantity", UNSET)

        _return_reason = d.pop("return_reason", UNSET)
        return_reason: Union[Unset, GETreturnLineItemsResponse200DataItemAttributesReturnReason]
        if isinstance(_return_reason, Unset):
            return_reason = UNSET
        else:
            return_reason = GETreturnLineItemsResponse200DataItemAttributesReturnReason.from_dict(_return_reason)

        restocked_at = d.pop("restocked_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETreturnLineItemsResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETreturnLineItemsResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_treturn_line_items_response_200_data_item_attributes = cls(
            sku_code=sku_code,
            bundle_code=bundle_code,
            name=name,
            quantity=quantity,
            return_reason=return_reason,
            restocked_at=restocked_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_treturn_line_items_response_200_data_item_attributes.additional_properties = d
        return ge_treturn_line_items_response_200_data_item_attributes

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
