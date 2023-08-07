from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses import (
        POSTgoogleGeocodersResponse201DataRelationshipsAddresses,
    )
    from ..models.pos_tgoogle_geocoders_response_201_data_relationships_attachments import (
        POSTgoogleGeocodersResponse201DataRelationshipsAttachments,
    )


T = TypeVar("T", bound="POSTgoogleGeocodersResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTgoogleGeocodersResponse201DataRelationships:
    """
    Attributes:
        addresses (Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddresses]):
        attachments (Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAttachments]):
    """

    addresses: Union[Unset, "POSTgoogleGeocodersResponse201DataRelationshipsAddresses"] = UNSET
    attachments: Union[Unset, "POSTgoogleGeocodersResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses import (
            POSTgoogleGeocodersResponse201DataRelationshipsAddresses,
        )
        from ..models.pos_tgoogle_geocoders_response_201_data_relationships_attachments import (
            POSTgoogleGeocodersResponse201DataRelationshipsAttachments,
        )

        d = src_dict.copy()
        _addresses = d.pop("addresses", UNSET)
        addresses: Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddresses]
        if isinstance(_addresses, Unset):
            addresses = UNSET
        else:
            addresses = POSTgoogleGeocodersResponse201DataRelationshipsAddresses.from_dict(_addresses)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTgoogleGeocodersResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tgoogle_geocoders_response_201_data_relationships = cls(
            addresses=addresses,
            attachments=attachments,
        )

        pos_tgoogle_geocoders_response_201_data_relationships.additional_properties = d
        return pos_tgoogle_geocoders_response_201_data_relationships

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
