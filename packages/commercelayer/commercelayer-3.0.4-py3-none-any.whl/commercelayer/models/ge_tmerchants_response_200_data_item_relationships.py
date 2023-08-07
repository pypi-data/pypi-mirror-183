from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tmerchants_response_200_data_item_relationships_address import (
        GETmerchantsResponse200DataItemRelationshipsAddress,
    )
    from ..models.ge_tmerchants_response_200_data_item_relationships_attachments import (
        GETmerchantsResponse200DataItemRelationshipsAttachments,
    )


T = TypeVar("T", bound="GETmerchantsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETmerchantsResponse200DataItemRelationships:
    """
    Attributes:
        address (Union[Unset, GETmerchantsResponse200DataItemRelationshipsAddress]):
        attachments (Union[Unset, GETmerchantsResponse200DataItemRelationshipsAttachments]):
    """

    address: Union[Unset, "GETmerchantsResponse200DataItemRelationshipsAddress"] = UNSET
    attachments: Union[Unset, "GETmerchantsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tmerchants_response_200_data_item_relationships_address import (
            GETmerchantsResponse200DataItemRelationshipsAddress,
        )
        from ..models.ge_tmerchants_response_200_data_item_relationships_attachments import (
            GETmerchantsResponse200DataItemRelationshipsAttachments,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, GETmerchantsResponse200DataItemRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GETmerchantsResponse200DataItemRelationshipsAddress.from_dict(_address)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETmerchantsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETmerchantsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tmerchants_response_200_data_item_relationships = cls(
            address=address,
            attachments=attachments,
        )

        ge_tmerchants_response_200_data_item_relationships.additional_properties = d
        return ge_tmerchants_response_200_data_item_relationships

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
