from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tmerchantsmerchant_id_response_200_data_relationships_address import (
        GETmerchantsmerchantIdResponse200DataRelationshipsAddress,
    )
    from ..models.ge_tmerchantsmerchant_id_response_200_data_relationships_attachments import (
        GETmerchantsmerchantIdResponse200DataRelationshipsAttachments,
    )


T = TypeVar("T", bound="GETmerchantsmerchantIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETmerchantsmerchantIdResponse200DataRelationships:
    """
    Attributes:
        address (Union[Unset, GETmerchantsmerchantIdResponse200DataRelationshipsAddress]):
        attachments (Union[Unset, GETmerchantsmerchantIdResponse200DataRelationshipsAttachments]):
    """

    address: Union[Unset, "GETmerchantsmerchantIdResponse200DataRelationshipsAddress"] = UNSET
    attachments: Union[Unset, "GETmerchantsmerchantIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tmerchantsmerchant_id_response_200_data_relationships_address import (
            GETmerchantsmerchantIdResponse200DataRelationshipsAddress,
        )
        from ..models.ge_tmerchantsmerchant_id_response_200_data_relationships_attachments import (
            GETmerchantsmerchantIdResponse200DataRelationshipsAttachments,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, GETmerchantsmerchantIdResponse200DataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GETmerchantsmerchantIdResponse200DataRelationshipsAddress.from_dict(_address)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETmerchantsmerchantIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETmerchantsmerchantIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tmerchantsmerchant_id_response_200_data_relationships = cls(
            address=address,
            attachments=attachments,
        )

        ge_tmerchantsmerchant_id_response_200_data_relationships.additional_properties = d
        return ge_tmerchantsmerchant_id_response_200_data_relationships

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
