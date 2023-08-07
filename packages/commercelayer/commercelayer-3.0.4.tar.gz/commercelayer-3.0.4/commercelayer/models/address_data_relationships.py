from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_data_relationships_geocoder import AddressDataRelationshipsGeocoder


T = TypeVar("T", bound="AddressDataRelationships")


@attr.s(auto_attribs=True)
class AddressDataRelationships:
    """
    Attributes:
        geocoder (Union[Unset, AddressDataRelationshipsGeocoder]):
    """

    geocoder: Union[Unset, "AddressDataRelationshipsGeocoder"] = UNSET
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
        from ..models.address_data_relationships_geocoder import AddressDataRelationshipsGeocoder

        d = src_dict.copy()
        _geocoder = d.pop("geocoder", UNSET)
        geocoder: Union[Unset, AddressDataRelationshipsGeocoder]
        if isinstance(_geocoder, Unset):
            geocoder = UNSET
        else:
            geocoder = AddressDataRelationshipsGeocoder.from_dict(_geocoder)

        address_data_relationships = cls(
            geocoder=geocoder,
        )

        address_data_relationships.additional_properties = d
        return address_data_relationships

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
