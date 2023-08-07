from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torders_response_200_data_item_relationships_available_free_skus_data import (
        GETordersResponse200DataItemRelationshipsAvailableFreeSkusData,
    )
    from ..models.ge_torders_response_200_data_item_relationships_available_free_skus_links import (
        GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks,
    )


T = TypeVar("T", bound="GETordersResponse200DataItemRelationshipsAvailableFreeSkus")


@attr.s(auto_attribs=True)
class GETordersResponse200DataItemRelationshipsAvailableFreeSkus:
    """
    Attributes:
        links (Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks]):
        data (Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkusData]):
    """

    links: Union[Unset, "GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks"] = UNSET
    data: Union[Unset, "GETordersResponse200DataItemRelationshipsAvailableFreeSkusData"] = UNSET
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
        from ..models.ge_torders_response_200_data_item_relationships_available_free_skus_data import (
            GETordersResponse200DataItemRelationshipsAvailableFreeSkusData,
        )
        from ..models.ge_torders_response_200_data_item_relationships_available_free_skus_links import (
            GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETordersResponse200DataItemRelationshipsAvailableFreeSkusLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkusData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETordersResponse200DataItemRelationshipsAvailableFreeSkusData.from_dict(_data)

        ge_torders_response_200_data_item_relationships_available_free_skus = cls(
            links=links,
            data=data,
        )

        ge_torders_response_200_data_item_relationships_available_free_skus.additional_properties = d
        return ge_torders_response_200_data_item_relationships_available_free_skus

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
