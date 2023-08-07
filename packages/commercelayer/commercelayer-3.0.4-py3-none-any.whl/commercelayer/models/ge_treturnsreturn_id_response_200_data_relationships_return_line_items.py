from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_treturnsreturn_id_response_200_data_relationships_return_line_items_data import (
        GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData,
    )
    from ..models.ge_treturnsreturn_id_response_200_data_relationships_return_line_items_links import (
        GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks,
    )


T = TypeVar("T", bound="GETreturnsreturnIdResponse200DataRelationshipsReturnLineItems")


@attr.s(auto_attribs=True)
class GETreturnsreturnIdResponse200DataRelationshipsReturnLineItems:
    """
    Attributes:
        links (Union[Unset, GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks]):
        data (Union[Unset, GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData]):
    """

    links: Union[Unset, "GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks"] = UNSET
    data: Union[Unset, "GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData"] = UNSET
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
        from ..models.ge_treturnsreturn_id_response_200_data_relationships_return_line_items_data import (
            GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData,
        )
        from ..models.ge_treturnsreturn_id_response_200_data_relationships_return_line_items_links import (
            GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETreturnsreturnIdResponse200DataRelationshipsReturnLineItemsData.from_dict(_data)

        ge_treturnsreturn_id_response_200_data_relationships_return_line_items = cls(
            links=links,
            data=data,
        )

        ge_treturnsreturn_id_response_200_data_relationships_return_line_items.additional_properties = d
        return ge_treturnsreturn_id_response_200_data_relationships_return_line_items

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
