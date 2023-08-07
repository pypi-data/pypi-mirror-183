from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_geocoder_data_relationships_attachments_data import (
        GoogleGeocoderDataRelationshipsAttachmentsData,
    )


T = TypeVar("T", bound="GoogleGeocoderDataRelationshipsAttachments")


@attr.s(auto_attribs=True)
class GoogleGeocoderDataRelationshipsAttachments:
    """
    Attributes:
        data (Union[Unset, GoogleGeocoderDataRelationshipsAttachmentsData]):
    """

    data: Union[Unset, "GoogleGeocoderDataRelationshipsAttachmentsData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_geocoder_data_relationships_attachments_data import (
            GoogleGeocoderDataRelationshipsAttachmentsData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, GoogleGeocoderDataRelationshipsAttachmentsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GoogleGeocoderDataRelationshipsAttachmentsData.from_dict(_data)

        google_geocoder_data_relationships_attachments = cls(
            data=data,
        )

        google_geocoder_data_relationships_attachments.additional_properties = d
        return google_geocoder_data_relationships_attachments

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
