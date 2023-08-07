from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location_data import (
        GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location_links import (
        GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks,
    )


T = TypeVar("T", bound="GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation")


@attr.s(auto_attribs=True)
class GETstockTransfersResponse200DataItemRelationshipsOriginStockLocation:
    """
    Attributes:
        links (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks]):
        data (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData]):
    """

    links: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks"] = UNSET
    data: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData"] = UNSET
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
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location_data import (
            GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location_links import (
            GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETstockTransfersResponse200DataItemRelationshipsOriginStockLocationData.from_dict(_data)

        ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location = cls(
            links=links,
            data=data,
        )

        ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location.additional_properties = d
        return ge_tstock_transfers_response_200_data_item_relationships_origin_stock_location

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
