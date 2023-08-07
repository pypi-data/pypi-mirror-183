from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus_data import (
        GETshippingCategoriesResponse200DataItemRelationshipsSkusData,
    )
    from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus_links import (
        GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks,
    )


T = TypeVar("T", bound="GETshippingCategoriesResponse200DataItemRelationshipsSkus")


@attr.s(auto_attribs=True)
class GETshippingCategoriesResponse200DataItemRelationshipsSkus:
    """
    Attributes:
        links (Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks]):
        data (Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkusData]):
    """

    links: Union[Unset, "GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks"] = UNSET
    data: Union[Unset, "GETshippingCategoriesResponse200DataItemRelationshipsSkusData"] = UNSET
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
        from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus_data import (
            GETshippingCategoriesResponse200DataItemRelationshipsSkusData,
        )
        from ..models.ge_tshipping_categories_response_200_data_item_relationships_skus_links import (
            GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETshippingCategoriesResponse200DataItemRelationshipsSkusLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETshippingCategoriesResponse200DataItemRelationshipsSkusData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETshippingCategoriesResponse200DataItemRelationshipsSkusData.from_dict(_data)

        ge_tshipping_categories_response_200_data_item_relationships_skus = cls(
            links=links,
            data=data,
        )

        ge_tshipping_categories_response_200_data_item_relationships_skus.additional_properties = d
        return ge_tshipping_categories_response_200_data_item_relationships_skus

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
