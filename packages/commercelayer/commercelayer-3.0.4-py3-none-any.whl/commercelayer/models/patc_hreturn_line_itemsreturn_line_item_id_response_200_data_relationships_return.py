from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return_data import (
        PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData,
    )
    from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return_links import (
        PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks,
    )


T = TypeVar("T", bound="PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturn")


@attr.s(auto_attribs=True)
class PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturn:
    """
    Attributes:
        links (Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks]):
        data (Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData]):
    """

    links: Union[Unset, "PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks"] = UNSET
    data: Union[Unset, "PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData"] = UNSET
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
        from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return_data import (
            PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData,
        )
        from ..models.patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return_links import (
            PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnData.from_dict(_data)

        patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return = cls(
            links=links,
            data=data,
        )

        patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return.additional_properties = d
        return patc_hreturn_line_itemsreturn_line_item_id_response_200_data_relationships_return

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
