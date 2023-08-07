from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_attributes_metadata import (
        PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHstockTransfersstockTransferIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHstockTransfersstockTransferIdResponse200DataAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        upcoming (Union[Unset, bool]): Send this attribute if you want to mark this stock transfer as upcoming. Example:
            True.
        picking (Union[Unset, bool]): Send this attribute if you want to start picking this stock transfer. Example:
            True.
        in_transit (Union[Unset, bool]): Send this attribute if you want to mark this stock transfer as in transit.
            Example: True.
        complete (Union[Unset, bool]): Send this attribute if you want to complete this stock transfer. Example: True.
        cancel (Union[Unset, bool]): Send this attribute if you want to cancel this stock transfer. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata]): Set of key-value
            pairs that you can attach to the resource. This can be useful for storing additional information about the
            resource in a structured format. Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    upcoming: Union[Unset, bool] = UNSET
    picking: Union[Unset, bool] = UNSET
    in_transit: Union[Unset, bool] = UNSET
    complete: Union[Unset, bool] = UNSET
    cancel: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        upcoming = self.upcoming
        picking = self.picking
        in_transit = self.in_transit
        complete = self.complete
        cancel = self.cancel
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
        if upcoming is not UNSET:
            field_dict["_upcoming"] = upcoming
        if picking is not UNSET:
            field_dict["_picking"] = picking
        if in_transit is not UNSET:
            field_dict["_in_transit"] = in_transit
        if complete is not UNSET:
            field_dict["_complete"] = complete
        if cancel is not UNSET:
            field_dict["_cancel"] = cancel
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_attributes_metadata import (
            PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        upcoming = d.pop("_upcoming", UNSET)

        picking = d.pop("_picking", UNSET)

        in_transit = d.pop("_in_transit", UNSET)

        complete = d.pop("_complete", UNSET)

        cancel = d.pop("_cancel", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHstockTransfersstockTransferIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hstock_transfersstock_transfer_id_response_200_data_attributes = cls(
            sku_code=sku_code,
            upcoming=upcoming,
            picking=picking,
            in_transit=in_transit,
            complete=complete,
            cancel=cancel,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hstock_transfersstock_transfer_id_response_200_data_attributes.additional_properties = d
        return patc_hstock_transfersstock_transfer_id_response_200_data_attributes

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
