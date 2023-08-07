from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.parcel_update_data_relationships_package_data import ParcelUpdateDataRelationshipsPackageData


T = TypeVar("T", bound="ParcelUpdateDataRelationshipsPackage")


@attr.s(auto_attribs=True)
class ParcelUpdateDataRelationshipsPackage:
    """
    Attributes:
        data (ParcelUpdateDataRelationshipsPackageData):
    """

    data: "ParcelUpdateDataRelationshipsPackageData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parcel_update_data_relationships_package_data import ParcelUpdateDataRelationshipsPackageData

        d = src_dict.copy()
        data = ParcelUpdateDataRelationshipsPackageData.from_dict(d.pop("data"))

        parcel_update_data_relationships_package = cls(
            data=data,
        )

        parcel_update_data_relationships_package.additional_properties = d
        return parcel_update_data_relationships_package

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
