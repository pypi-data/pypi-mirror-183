from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_data_relationships_attachments import PackageDataRelationshipsAttachments
    from ..models.package_data_relationships_parcels import PackageDataRelationshipsParcels
    from ..models.package_data_relationships_stock_location import PackageDataRelationshipsStockLocation


T = TypeVar("T", bound="PackageDataRelationships")


@attr.s(auto_attribs=True)
class PackageDataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, PackageDataRelationshipsStockLocation]):
        parcels (Union[Unset, PackageDataRelationshipsParcels]):
        attachments (Union[Unset, PackageDataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "PackageDataRelationshipsStockLocation"] = UNSET
    parcels: Union[Unset, "PackageDataRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "PackageDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        parcels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parcels, Unset):
            parcels = self.parcels.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if parcels is not UNSET:
            field_dict["parcels"] = parcels
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_data_relationships_attachments import PackageDataRelationshipsAttachments
        from ..models.package_data_relationships_parcels import PackageDataRelationshipsParcels
        from ..models.package_data_relationships_stock_location import PackageDataRelationshipsStockLocation

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, PackageDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = PackageDataRelationshipsStockLocation.from_dict(_stock_location)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, PackageDataRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = PackageDataRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PackageDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PackageDataRelationshipsAttachments.from_dict(_attachments)

        package_data_relationships = cls(
            stock_location=stock_location,
            parcels=parcels,
            attachments=attachments,
        )

        package_data_relationships.additional_properties = d
        return package_data_relationships

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
