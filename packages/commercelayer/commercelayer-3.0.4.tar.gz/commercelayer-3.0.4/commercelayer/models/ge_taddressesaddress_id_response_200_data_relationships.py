from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_taddressesaddress_id_response_200_data_relationships_geocoder import (
        GETaddressesaddressIdResponse200DataRelationshipsGeocoder,
    )


T = TypeVar("T", bound="GETaddressesaddressIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETaddressesaddressIdResponse200DataRelationships:
    """
    Attributes:
        geocoder (Union[Unset, GETaddressesaddressIdResponse200DataRelationshipsGeocoder]):
    """

    geocoder: Union[Unset, "GETaddressesaddressIdResponse200DataRelationshipsGeocoder"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        geocoder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geocoder, Unset):
            geocoder = self.geocoder.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geocoder is not UNSET:
            field_dict["geocoder"] = geocoder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_taddressesaddress_id_response_200_data_relationships_geocoder import (
            GETaddressesaddressIdResponse200DataRelationshipsGeocoder,
        )

        d = src_dict.copy()
        _geocoder = d.pop("geocoder", UNSET)
        geocoder: Union[Unset, GETaddressesaddressIdResponse200DataRelationshipsGeocoder]
        if isinstance(_geocoder, Unset):
            geocoder = UNSET
        else:
            geocoder = GETaddressesaddressIdResponse200DataRelationshipsGeocoder.from_dict(_geocoder)

        ge_taddressesaddress_id_response_200_data_relationships = cls(
            geocoder=geocoder,
        )

        ge_taddressesaddress_id_response_200_data_relationships.additional_properties = d
        return ge_taddressesaddress_id_response_200_data_relationships

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
