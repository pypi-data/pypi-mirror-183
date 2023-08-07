from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tattachmentsattachment_id_response_200_data_relationships_attachable import (
        GETattachmentsattachmentIdResponse200DataRelationshipsAttachable,
    )


T = TypeVar("T", bound="GETattachmentsattachmentIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETattachmentsattachmentIdResponse200DataRelationships:
    """
    Attributes:
        attachable (Union[Unset, GETattachmentsattachmentIdResponse200DataRelationshipsAttachable]):
    """

    attachable: Union[Unset, "GETattachmentsattachmentIdResponse200DataRelationshipsAttachable"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachable, Unset):
            attachable = self.attachable.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachable is not UNSET:
            field_dict["attachable"] = attachable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tattachmentsattachment_id_response_200_data_relationships_attachable import (
            GETattachmentsattachmentIdResponse200DataRelationshipsAttachable,
        )

        d = src_dict.copy()
        _attachable = d.pop("attachable", UNSET)
        attachable: Union[Unset, GETattachmentsattachmentIdResponse200DataRelationshipsAttachable]
        if isinstance(_attachable, Unset):
            attachable = UNSET
        else:
            attachable = GETattachmentsattachmentIdResponse200DataRelationshipsAttachable.from_dict(_attachable)

        ge_tattachmentsattachment_id_response_200_data_relationships = cls(
            attachable=attachable,
        )

        ge_tattachmentsattachment_id_response_200_data_relationships.additional_properties = d
        return ge_tattachmentsattachment_id_response_200_data_relationships

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
