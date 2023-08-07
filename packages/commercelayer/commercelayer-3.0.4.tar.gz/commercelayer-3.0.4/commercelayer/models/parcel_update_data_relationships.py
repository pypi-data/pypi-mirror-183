from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parcel_update_data_relationships_package import ParcelUpdateDataRelationshipsPackage
    from ..models.parcel_update_data_relationships_shipment import ParcelUpdateDataRelationshipsShipment


T = TypeVar("T", bound="ParcelUpdateDataRelationships")


@attr.s(auto_attribs=True)
class ParcelUpdateDataRelationships:
    """
    Attributes:
        shipment (Union[Unset, ParcelUpdateDataRelationshipsShipment]):
        package (Union[Unset, ParcelUpdateDataRelationshipsPackage]):
    """

    shipment: Union[Unset, "ParcelUpdateDataRelationshipsShipment"] = UNSET
    package: Union[Unset, "ParcelUpdateDataRelationshipsPackage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parcel_update_data_relationships_package import ParcelUpdateDataRelationshipsPackage
        from ..models.parcel_update_data_relationships_shipment import ParcelUpdateDataRelationshipsShipment

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, ParcelUpdateDataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = ParcelUpdateDataRelationshipsShipment.from_dict(_shipment)

        _package = d.pop("package", UNSET)
        package: Union[Unset, ParcelUpdateDataRelationshipsPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = ParcelUpdateDataRelationshipsPackage.from_dict(_package)

        parcel_update_data_relationships = cls(
            shipment=shipment,
            package=package,
        )

        parcel_update_data_relationships.additional_properties = d
        return parcel_update_data_relationships

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
