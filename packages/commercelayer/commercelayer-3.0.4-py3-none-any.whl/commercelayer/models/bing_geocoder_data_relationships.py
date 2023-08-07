from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bing_geocoder_data_relationships_addresses import BingGeocoderDataRelationshipsAddresses
    from ..models.bing_geocoder_data_relationships_attachments import BingGeocoderDataRelationshipsAttachments


T = TypeVar("T", bound="BingGeocoderDataRelationships")


@attr.s(auto_attribs=True)
class BingGeocoderDataRelationships:
    """
    Attributes:
        addresses (Union[Unset, BingGeocoderDataRelationshipsAddresses]):
        attachments (Union[Unset, BingGeocoderDataRelationshipsAttachments]):
    """

    addresses: Union[Unset, "BingGeocoderDataRelationshipsAddresses"] = UNSET
    attachments: Union[Unset, "BingGeocoderDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addresses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bing_geocoder_data_relationships_addresses import BingGeocoderDataRelationshipsAddresses
        from ..models.bing_geocoder_data_relationships_attachments import BingGeocoderDataRelationshipsAttachments

        d = src_dict.copy()
        _addresses = d.pop("addresses", UNSET)
        addresses: Union[Unset, BingGeocoderDataRelationshipsAddresses]
        if isinstance(_addresses, Unset):
            addresses = UNSET
        else:
            addresses = BingGeocoderDataRelationshipsAddresses.from_dict(_addresses)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, BingGeocoderDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = BingGeocoderDataRelationshipsAttachments.from_dict(_attachments)

        bing_geocoder_data_relationships = cls(
            addresses=addresses,
            attachments=attachments,
        )

        bing_geocoder_data_relationships.additional_properties = d
        return bing_geocoder_data_relationships

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
