from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location_data import (
        GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData,
    )
    from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location_links import (
        GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks,
    )


T = TypeVar("T", bound="GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation")


@attr.s(auto_attribs=True)
class GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocation:
    """
    Attributes:
        links (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks]):
        data (Union[Unset, GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData]):
    """

    links: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks"] = UNSET
    data: Union[Unset, "GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData"] = UNSET
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
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location_data import (
            GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData,
        )
        from ..models.ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location_links import (
            GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETstockTransfersResponse200DataItemRelationshipsDestinationStockLocationData.from_dict(_data)

        ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location = cls(
            links=links,
            data=data,
        )

        ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location.additional_properties = d
        return ge_tstock_transfers_response_200_data_item_relationships_destination_stock_location

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
