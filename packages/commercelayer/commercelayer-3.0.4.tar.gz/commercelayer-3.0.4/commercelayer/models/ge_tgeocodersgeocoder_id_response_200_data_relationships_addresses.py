from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses_data import (
        GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData,
    )
    from ..models.ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses_links import (
        GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks,
    )


T = TypeVar("T", bound="GETgeocodersgeocoderIdResponse200DataRelationshipsAddresses")


@attr.s(auto_attribs=True)
class GETgeocodersgeocoderIdResponse200DataRelationshipsAddresses:
    """
    Attributes:
        links (Union[Unset, GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks]):
        data (Union[Unset, GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData]):
    """

    links: Union[Unset, "GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks"] = UNSET
    data: Union[Unset, "GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData"] = UNSET
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
        from ..models.ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses_data import (
            GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData,
        )
        from ..models.ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses_links import (
            GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETgeocodersgeocoderIdResponse200DataRelationshipsAddressesData.from_dict(_data)

        ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses = cls(
            links=links,
            data=data,
        )

        ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses.additional_properties = d
        return ge_tgeocodersgeocoder_id_response_200_data_relationships_addresses

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
