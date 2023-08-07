from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tmerchants_response_201_data_relationships_address import (
        POSTmerchantsResponse201DataRelationshipsAddress,
    )
    from ..models.pos_tmerchants_response_201_data_relationships_attachments import (
        POSTmerchantsResponse201DataRelationshipsAttachments,
    )


T = TypeVar("T", bound="POSTmerchantsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTmerchantsResponse201DataRelationships:
    """
    Attributes:
        address (Union[Unset, POSTmerchantsResponse201DataRelationshipsAddress]):
        attachments (Union[Unset, POSTmerchantsResponse201DataRelationshipsAttachments]):
    """

    address: Union[Unset, "POSTmerchantsResponse201DataRelationshipsAddress"] = UNSET
    attachments: Union[Unset, "POSTmerchantsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tmerchants_response_201_data_relationships_address import (
            POSTmerchantsResponse201DataRelationshipsAddress,
        )
        from ..models.pos_tmerchants_response_201_data_relationships_attachments import (
            POSTmerchantsResponse201DataRelationshipsAttachments,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, POSTmerchantsResponse201DataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = POSTmerchantsResponse201DataRelationshipsAddress.from_dict(_address)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTmerchantsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTmerchantsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tmerchants_response_201_data_relationships = cls(
            address=address,
            attachments=attachments,
        )

        pos_tmerchants_response_201_data_relationships.additional_properties = d
        return pos_tmerchants_response_201_data_relationships

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
