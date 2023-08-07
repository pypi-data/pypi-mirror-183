from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tgeocoders_response_200_data_item_relationships_addresses import (
        GETgeocodersResponse200DataItemRelationshipsAddresses,
    )
    from ..models.ge_tgeocoders_response_200_data_item_relationships_attachments import (
        GETgeocodersResponse200DataItemRelationshipsAttachments,
    )


T = TypeVar("T", bound="GETgeocodersResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETgeocodersResponse200DataItemRelationships:
    """
    Attributes:
        addresses (Union[Unset, GETgeocodersResponse200DataItemRelationshipsAddresses]):
        attachments (Union[Unset, GETgeocodersResponse200DataItemRelationshipsAttachments]):
    """

    addresses: Union[Unset, "GETgeocodersResponse200DataItemRelationshipsAddresses"] = UNSET
    attachments: Union[Unset, "GETgeocodersResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tgeocoders_response_200_data_item_relationships_addresses import (
            GETgeocodersResponse200DataItemRelationshipsAddresses,
        )
        from ..models.ge_tgeocoders_response_200_data_item_relationships_attachments import (
            GETgeocodersResponse200DataItemRelationshipsAttachments,
        )

        d = src_dict.copy()
        _addresses = d.pop("addresses", UNSET)
        addresses: Union[Unset, GETgeocodersResponse200DataItemRelationshipsAddresses]
        if isinstance(_addresses, Unset):
            addresses = UNSET
        else:
            addresses = GETgeocodersResponse200DataItemRelationshipsAddresses.from_dict(_addresses)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETgeocodersResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETgeocodersResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tgeocoders_response_200_data_item_relationships = cls(
            addresses=addresses,
            attachments=attachments,
        )

        ge_tgeocoders_response_200_data_item_relationships.additional_properties = d
        return ge_tgeocoders_response_200_data_item_relationships

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
