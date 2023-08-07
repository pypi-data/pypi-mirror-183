from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments_data import (
        GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData,
    )
    from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments_links import (
        GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks,
    )


T = TypeVar("T", bound="GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments")


@attr.s(auto_attribs=True)
class GETpriceTierspriceTierIdResponse200DataRelationshipsAttachments:
    """
    Attributes:
        links (Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks]):
        data (Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData]):
    """

    links: Union[Unset, "GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks"] = UNSET
    data: Union[Unset, "GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData"] = UNSET
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
        from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments_data import (
            GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData,
        )
        from ..models.ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments_links import (
            GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETpriceTierspriceTierIdResponse200DataRelationshipsAttachmentsData.from_dict(_data)

        ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments = cls(
            links=links,
            data=data,
        )

        ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments.additional_properties = d
        return ge_tprice_tiersprice_tier_id_response_200_data_relationships_attachments

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
