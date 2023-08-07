from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hreturnsreturn_id_response_200_data_attributes_metadata import (
        PATCHreturnsreturnIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHreturnsreturnIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHreturnsreturnIdResponse200DataAttributes:
    """
    Attributes:
        request (Union[Unset, bool]): Send this attribute if you want to activate this return. Example: True.
        approve (Union[Unset, bool]): Send this attribute if you want to mark this return as approved. Example: True.
        cancel (Union[Unset, bool]): Send this attribute if you want to mark this return as cancelled. Example: True.
        ship (Union[Unset, bool]): Send this attribute if you want to mark this return as shipped. Example: True.
        reject (Union[Unset, bool]): Send this attribute if you want to mark this return as rejected. Example: True.
        receive (Union[Unset, bool]): Send this attribute if you want to mark this return as received. Example: True.
        restock (Union[Unset, bool]): Send this attribute if you want to restock all of the return line items. Example:
            True.
        archive (Union[Unset, bool]): Send this attribute if you want to archive the return. Example: True.
        unarchive (Union[Unset, bool]): Send this attribute if you want to unarchive the return. Example: True.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHreturnsreturnIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    request: Union[Unset, bool] = UNSET
    approve: Union[Unset, bool] = UNSET
    cancel: Union[Unset, bool] = UNSET
    ship: Union[Unset, bool] = UNSET
    reject: Union[Unset, bool] = UNSET
    receive: Union[Unset, bool] = UNSET
    restock: Union[Unset, bool] = UNSET
    archive: Union[Unset, bool] = UNSET
    unarchive: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHreturnsreturnIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request = self.request
        approve = self.approve
        cancel = self.cancel
        ship = self.ship
        reject = self.reject
        receive = self.receive
        restock = self.restock
        archive = self.archive
        unarchive = self.unarchive
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["_request"] = request
        if approve is not UNSET:
            field_dict["_approve"] = approve
        if cancel is not UNSET:
            field_dict["_cancel"] = cancel
        if ship is not UNSET:
            field_dict["_ship"] = ship
        if reject is not UNSET:
            field_dict["_reject"] = reject
        if receive is not UNSET:
            field_dict["_receive"] = receive
        if restock is not UNSET:
            field_dict["_restock"] = restock
        if archive is not UNSET:
            field_dict["_archive"] = archive
        if unarchive is not UNSET:
            field_dict["_unarchive"] = unarchive
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hreturnsreturn_id_response_200_data_attributes_metadata import (
            PATCHreturnsreturnIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        request = d.pop("_request", UNSET)

        approve = d.pop("_approve", UNSET)

        cancel = d.pop("_cancel", UNSET)

        ship = d.pop("_ship", UNSET)

        reject = d.pop("_reject", UNSET)

        receive = d.pop("_receive", UNSET)

        restock = d.pop("_restock", UNSET)

        archive = d.pop("_archive", UNSET)

        unarchive = d.pop("_unarchive", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHreturnsreturnIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHreturnsreturnIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hreturnsreturn_id_response_200_data_attributes = cls(
            request=request,
            approve=approve,
            cancel=cancel,
            ship=ship,
            reject=reject,
            receive=receive,
            restock=restock,
            archive=archive,
            unarchive=unarchive,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hreturnsreturn_id_response_200_data_attributes.additional_properties = d
        return patc_hreturnsreturn_id_response_200_data_attributes

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
