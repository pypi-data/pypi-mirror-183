from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hmerchantsmerchant_id_response_200_data_relationships_address_data import (
        PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData,
    )
    from ..models.patc_hmerchantsmerchant_id_response_200_data_relationships_address_links import (
        PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks,
    )


T = TypeVar("T", bound="PATCHmerchantsmerchantIdResponse200DataRelationshipsAddress")


@attr.s(auto_attribs=True)
class PATCHmerchantsmerchantIdResponse200DataRelationshipsAddress:
    """
    Attributes:
        links (Union[Unset, PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks]):
        data (Union[Unset, PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData]):
    """

    links: Union[Unset, "PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks"] = UNSET
    data: Union[Unset, "PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hmerchantsmerchant_id_response_200_data_relationships_address_data import (
            PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData,
        )
        from ..models.patc_hmerchantsmerchant_id_response_200_data_relationships_address_links import (
            PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressData.from_dict(_data)

        patc_hmerchantsmerchant_id_response_200_data_relationships_address = cls(
            links=links,
            data=data,
        )

        patc_hmerchantsmerchant_id_response_200_data_relationships_address.additional_properties = d
        return patc_hmerchantsmerchant_id_response_200_data_relationships_address

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
