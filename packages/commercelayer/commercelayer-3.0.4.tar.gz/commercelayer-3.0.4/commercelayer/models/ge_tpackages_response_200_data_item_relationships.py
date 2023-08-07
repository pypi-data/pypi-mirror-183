from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpackages_response_200_data_item_relationships_attachments import (
        GETpackagesResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tpackages_response_200_data_item_relationships_parcels import (
        GETpackagesResponse200DataItemRelationshipsParcels,
    )
    from ..models.ge_tpackages_response_200_data_item_relationships_stock_location import (
        GETpackagesResponse200DataItemRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETpackagesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpackagesResponse200DataItemRelationships:
    """
    Attributes:
        stock_location (Union[Unset, GETpackagesResponse200DataItemRelationshipsStockLocation]):
        parcels (Union[Unset, GETpackagesResponse200DataItemRelationshipsParcels]):
        attachments (Union[Unset, GETpackagesResponse200DataItemRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "GETpackagesResponse200DataItemRelationshipsStockLocation"] = UNSET
    parcels: Union[Unset, "GETpackagesResponse200DataItemRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "GETpackagesResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tpackages_response_200_data_item_relationships_attachments import (
            GETpackagesResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tpackages_response_200_data_item_relationships_parcels import (
            GETpackagesResponse200DataItemRelationshipsParcels,
        )
        from ..models.ge_tpackages_response_200_data_item_relationships_stock_location import (
            GETpackagesResponse200DataItemRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETpackagesResponse200DataItemRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETpackagesResponse200DataItemRelationshipsStockLocation.from_dict(_stock_location)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, GETpackagesResponse200DataItemRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = GETpackagesResponse200DataItemRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpackagesResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpackagesResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tpackages_response_200_data_item_relationships = cls(
            stock_location=stock_location,
            parcels=parcels,
            attachments=attachments,
        )

        ge_tpackages_response_200_data_item_relationships.additional_properties = d
        return ge_tpackages_response_200_data_item_relationships

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
