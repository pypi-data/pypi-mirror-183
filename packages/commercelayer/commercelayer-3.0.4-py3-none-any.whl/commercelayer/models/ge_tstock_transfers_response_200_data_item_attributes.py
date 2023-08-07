from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_transfers_response_200_data_item_attributes_metadata import (
        GETstockTransfersResponse200DataItemAttributesMetadata,
    )


T = TypeVar("T", bound="GETstockTransfersResponse200DataItemAttributes")


@attr.s(auto_attribs=True)
class GETstockTransfersResponse200DataItemAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        status (Union[Unset, str]): The stock transfer status, one of 'draft', 'upcoming', 'picking', 'in_transit',
            'completed', or 'cancelled' Example: draft.
        quantity (Union[Unset, int]): The stock quantity to be transferred from the origin stock location to destination
            one Example: 2.
        completed_at (Union[Unset, str]): Time at which the stock transfer was completed. Example:
            2018-01-01T12:00:00.000Z.
        cancelled_at (Union[Unset, str]): Time at which the stock transfer was cancelled. Example:
            2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETstockTransfersResponse200DataItemAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    completed_at: Union[Unset, str] = UNSET
    cancelled_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETstockTransfersResponse200DataItemAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        status = self.status
        quantity = self.quantity
        completed_at = self.completed_at
        cancelled_at = self.cancelled_at
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
        if status is not UNSET:
            field_dict["status"] = status
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
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
        from ..models.ge_tstock_transfers_response_200_data_item_attributes_metadata import (
            GETstockTransfersResponse200DataItemAttributesMetadata,
        )

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        status = d.pop("status", UNSET)

        quantity = d.pop("quantity", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        cancelled_at = d.pop("cancelled_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETstockTransfersResponse200DataItemAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETstockTransfersResponse200DataItemAttributesMetadata.from_dict(_metadata)

        ge_tstock_transfers_response_200_data_item_attributes = cls(
            sku_code=sku_code,
            status=status,
            quantity=quantity,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tstock_transfers_response_200_data_item_attributes.additional_properties = d
        return ge_tstock_transfers_response_200_data_item_attributes

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
