from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tline_items_response_200_data_item_relationships_stock_transfers_data import (
        GETlineItemsResponse200DataItemRelationshipsStockTransfersData,
    )
    from ..models.ge_tline_items_response_200_data_item_relationships_stock_transfers_links import (
        GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks,
    )


T = TypeVar("T", bound="GETlineItemsResponse200DataItemRelationshipsStockTransfers")


@attr.s(auto_attribs=True)
class GETlineItemsResponse200DataItemRelationshipsStockTransfers:
    """
    Attributes:
        links (Union[Unset, GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks]):
        data (Union[Unset, GETlineItemsResponse200DataItemRelationshipsStockTransfersData]):
    """

    links: Union[Unset, "GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks"] = UNSET
    data: Union[Unset, "GETlineItemsResponse200DataItemRelationshipsStockTransfersData"] = UNSET
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
        from ..models.ge_tline_items_response_200_data_item_relationships_stock_transfers_data import (
            GETlineItemsResponse200DataItemRelationshipsStockTransfersData,
        )
        from ..models.ge_tline_items_response_200_data_item_relationships_stock_transfers_links import (
            GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETlineItemsResponse200DataItemRelationshipsStockTransfersLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETlineItemsResponse200DataItemRelationshipsStockTransfersData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETlineItemsResponse200DataItemRelationshipsStockTransfersData.from_dict(_data)

        ge_tline_items_response_200_data_item_relationships_stock_transfers = cls(
            links=links,
            data=data,
        )

        ge_tline_items_response_200_data_item_relationships_stock_transfers.additional_properties = d
        return ge_tline_items_response_200_data_item_relationships_stock_transfers

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
