from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpackagespackage_id_response_200_data_relationships_attachments import (
        GETpackagespackageIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tpackagespackage_id_response_200_data_relationships_parcels import (
        GETpackagespackageIdResponse200DataRelationshipsParcels,
    )
    from ..models.ge_tpackagespackage_id_response_200_data_relationships_stock_location import (
        GETpackagespackageIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETpackagespackageIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETpackagespackageIdResponse200DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, GETpackagespackageIdResponse200DataRelationshipsStockLocation]):
        parcels (Union[Unset, GETpackagespackageIdResponse200DataRelationshipsParcels]):
        attachments (Union[Unset, GETpackagespackageIdResponse200DataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "GETpackagespackageIdResponse200DataRelationshipsStockLocation"] = UNSET
    parcels: Union[Unset, "GETpackagespackageIdResponse200DataRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "GETpackagespackageIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tpackagespackage_id_response_200_data_relationships_attachments import (
            GETpackagespackageIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tpackagespackage_id_response_200_data_relationships_parcels import (
            GETpackagespackageIdResponse200DataRelationshipsParcels,
        )
        from ..models.ge_tpackagespackage_id_response_200_data_relationships_stock_location import (
            GETpackagespackageIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETpackagespackageIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETpackagespackageIdResponse200DataRelationshipsStockLocation.from_dict(_stock_location)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, GETpackagespackageIdResponse200DataRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = GETpackagespackageIdResponse200DataRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpackagespackageIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpackagespackageIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tpackagespackage_id_response_200_data_relationships = cls(
            stock_location=stock_location,
            parcels=parcels,
            attachments=attachments,
        )

        ge_tpackagespackage_id_response_200_data_relationships.additional_properties = d
        return ge_tpackagespackage_id_response_200_data_relationships

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
