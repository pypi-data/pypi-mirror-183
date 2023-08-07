from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tvoids_response_200_data_item_relationships_order_data import (
        GETvoidsResponse200DataItemRelationshipsOrderData,
    )
    from ..models.ge_tvoids_response_200_data_item_relationships_order_links import (
        GETvoidsResponse200DataItemRelationshipsOrderLinks,
    )


T = TypeVar("T", bound="GETvoidsResponse200DataItemRelationshipsOrder")


@attr.s(auto_attribs=True)
class GETvoidsResponse200DataItemRelationshipsOrder:
    """
    Attributes:
        links (Union[Unset, GETvoidsResponse200DataItemRelationshipsOrderLinks]):
        data (Union[Unset, GETvoidsResponse200DataItemRelationshipsOrderData]):
    """

    links: Union[Unset, "GETvoidsResponse200DataItemRelationshipsOrderLinks"] = UNSET
    data: Union[Unset, "GETvoidsResponse200DataItemRelationshipsOrderData"] = UNSET
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
        from ..models.ge_tvoids_response_200_data_item_relationships_order_data import (
            GETvoidsResponse200DataItemRelationshipsOrderData,
        )
        from ..models.ge_tvoids_response_200_data_item_relationships_order_links import (
            GETvoidsResponse200DataItemRelationshipsOrderLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETvoidsResponse200DataItemRelationshipsOrderLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETvoidsResponse200DataItemRelationshipsOrderLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETvoidsResponse200DataItemRelationshipsOrderData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETvoidsResponse200DataItemRelationshipsOrderData.from_dict(_data)

        ge_tvoids_response_200_data_item_relationships_order = cls(
            links=links,
            data=data,
        )

        ge_tvoids_response_200_data_item_relationships_order.additional_properties = d
        return ge_tvoids_response_200_data_item_relationships_order

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
