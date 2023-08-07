from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.parcel_create_data_relationships_package import ParcelCreateDataRelationshipsPackage
    from ..models.parcel_create_data_relationships_shipment import ParcelCreateDataRelationshipsShipment


T = TypeVar("T", bound="ParcelCreateDataRelationships")


@attr.s(auto_attribs=True)
class ParcelCreateDataRelationships:
    """
    Attributes:
        shipment (ParcelCreateDataRelationshipsShipment):
        package (ParcelCreateDataRelationshipsPackage):
    """

    shipment: "ParcelCreateDataRelationshipsShipment"
    package: "ParcelCreateDataRelationshipsPackage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment = self.shipment.to_dict()

        package = self.package.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipment": shipment,
                "package": package,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parcel_create_data_relationships_package import ParcelCreateDataRelationshipsPackage
        from ..models.parcel_create_data_relationships_shipment import ParcelCreateDataRelationshipsShipment

        d = src_dict.copy()
        shipment = ParcelCreateDataRelationshipsShipment.from_dict(d.pop("shipment"))

        package = ParcelCreateDataRelationshipsPackage.from_dict(d.pop("package"))

        parcel_create_data_relationships = cls(
            shipment=shipment,
            package=package,
        )

        parcel_create_data_relationships.additional_properties = d
        return parcel_create_data_relationships

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
