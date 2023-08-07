from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations_data import (
        GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData,
    )
    from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations_links import (
        GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks,
    )


T = TypeVar("T", bound="GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations")


@attr.s(auto_attribs=True)
class GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocations:
    """
    Attributes:
        links (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks]):
        data (Union[Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData]):
    """

    links: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks"] = UNSET
    data: Union[Unset, "GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData"] = UNSET
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
        from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations_data import (
            GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData,
        )
        from ..models.ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations_links import (
            GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETstockLocationsResponse200DataItemRelationshipsInventoryStockLocationsData.from_dict(_data)

        ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations = cls(
            links=links,
            data=data,
        )

        ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations.additional_properties = d
        return ge_tstock_locations_response_200_data_item_relationships_inventory_stock_locations

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
