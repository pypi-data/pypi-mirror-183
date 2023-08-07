from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses_data import (
        POSTgoogleGeocodersResponse201DataRelationshipsAddressesData,
    )
    from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses_links import (
        POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks,
    )


T = TypeVar("T", bound="POSTgoogleGeocodersResponse201DataRelationshipsAddresses")


@attr.s(auto_attribs=True)
class POSTgoogleGeocodersResponse201DataRelationshipsAddresses:
    """
    Attributes:
        links (Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks]):
        data (Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddressesData]):
    """

    links: Union[Unset, "POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks"] = UNSET
    data: Union[Unset, "POSTgoogleGeocodersResponse201DataRelationshipsAddressesData"] = UNSET
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
        from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses_data import (
            POSTgoogleGeocodersResponse201DataRelationshipsAddressesData,
        )
        from ..models.pos_tgoogle_geocoders_response_201_data_relationships_addresses_links import (
            POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTgoogleGeocodersResponse201DataRelationshipsAddressesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTgoogleGeocodersResponse201DataRelationshipsAddressesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTgoogleGeocodersResponse201DataRelationshipsAddressesData.from_dict(_data)

        pos_tgoogle_geocoders_response_201_data_relationships_addresses = cls(
            links=links,
            data=data,
        )

        pos_tgoogle_geocoders_response_201_data_relationships_addresses.additional_properties = d
        return pos_tgoogle_geocoders_response_201_data_relationships_addresses

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
