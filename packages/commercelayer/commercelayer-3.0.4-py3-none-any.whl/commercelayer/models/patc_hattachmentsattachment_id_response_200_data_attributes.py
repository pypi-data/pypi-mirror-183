from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hattachmentsattachment_id_response_200_data_attributes_metadata import (
        PATCHattachmentsattachmentIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHattachmentsattachmentIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHattachmentsattachmentIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The internal name of the attachment. Example: DDT transport document.
        description (Union[Unset, str]): An internal description of the attachment. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        url (Union[Unset, str]): The attachment URL. Example: https://s3.yourdomain.com/attachment.pdf.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHattachmentsattachmentIdResponse200DataAttributesMetadata]): Set of key-value pairs
            that you can attach to the resource. This can be useful for storing additional information about the resource in
            a structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHattachmentsattachmentIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        url = self.url
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hattachmentsattachment_id_response_200_data_attributes_metadata import (
            PATCHattachmentsattachmentIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHattachmentsattachmentIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHattachmentsattachmentIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hattachmentsattachment_id_response_200_data_attributes = cls(
            name=name,
            description=description,
            url=url,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hattachmentsattachment_id_response_200_data_attributes.additional_properties = d
        return patc_hattachmentsattachment_id_response_200_data_attributes

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
