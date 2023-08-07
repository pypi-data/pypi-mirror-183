from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpackagespackage_id_response_200_data_relationships_attachments import (
        PATCHpackagespackageIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels import (
        PATCHpackagespackageIdResponse200DataRelationshipsParcels,
    )
    from ..models.patc_hpackagespackage_id_response_200_data_relationships_stock_location import (
        PATCHpackagespackageIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="PATCHpackagespackageIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHpackagespackageIdResponse200DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsStockLocation]):
        parcels (Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcels]):
        attachments (Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "PATCHpackagespackageIdResponse200DataRelationshipsStockLocation"] = UNSET
    parcels: Union[Unset, "PATCHpackagespackageIdResponse200DataRelationshipsParcels"] = UNSET
    attachments: Union[Unset, "PATCHpackagespackageIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.patc_hpackagespackage_id_response_200_data_relationships_attachments import (
            PATCHpackagespackageIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels import (
            PATCHpackagespackageIdResponse200DataRelationshipsParcels,
        )
        from ..models.patc_hpackagespackage_id_response_200_data_relationships_stock_location import (
            PATCHpackagespackageIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = PATCHpackagespackageIdResponse200DataRelationshipsStockLocation.from_dict(_stock_location)

        _parcels = d.pop("parcels", UNSET)
        parcels: Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcels]
        if isinstance(_parcels, Unset):
            parcels = UNSET
        else:
            parcels = PATCHpackagespackageIdResponse200DataRelationshipsParcels.from_dict(_parcels)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHpackagespackageIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        patc_hpackagespackage_id_response_200_data_relationships = cls(
            stock_location=stock_location,
            parcels=parcels,
            attachments=attachments,
        )

        patc_hpackagespackage_id_response_200_data_relationships.additional_properties = d
        return patc_hpackagespackage_id_response_200_data_relationships

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
