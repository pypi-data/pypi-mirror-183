from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels_data import (
        PATCHpackagespackageIdResponse200DataRelationshipsParcelsData,
    )
    from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels_links import (
        PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks,
    )


T = TypeVar("T", bound="PATCHpackagespackageIdResponse200DataRelationshipsParcels")


@attr.s(auto_attribs=True)
class PATCHpackagespackageIdResponse200DataRelationshipsParcels:
    """
    Attributes:
        links (Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks]):
        data (Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcelsData]):
    """

    links: Union[Unset, "PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks"] = UNSET
    data: Union[Unset, "PATCHpackagespackageIdResponse200DataRelationshipsParcelsData"] = UNSET
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
        from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels_data import (
            PATCHpackagespackageIdResponse200DataRelationshipsParcelsData,
        )
        from ..models.patc_hpackagespackage_id_response_200_data_relationships_parcels_links import (
            PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHpackagespackageIdResponse200DataRelationshipsParcelsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHpackagespackageIdResponse200DataRelationshipsParcelsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHpackagespackageIdResponse200DataRelationshipsParcelsData.from_dict(_data)

        patc_hpackagespackage_id_response_200_data_relationships_parcels = cls(
            links=links,
            data=data,
        )

        patc_hpackagespackage_id_response_200_data_relationships_parcels.additional_properties = d
        return patc_hpackagespackage_id_response_200_data_relationships_parcels

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
