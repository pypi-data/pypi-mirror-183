from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location_data import (
        POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData,
    )
    from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location_links import (
        POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks,
    )


T = TypeVar("T", bound="POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation")


@attr.s(auto_attribs=True)
class POSTinventoryStockLocationsResponse201DataRelationshipsStockLocation:
    """
    Attributes:
        links (Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks]):
        data (Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData]):
    """

    links: Union[Unset, "POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks"] = UNSET
    data: Union[Unset, "POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData"] = UNSET
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
        from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location_data import (
            POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData,
        )
        from ..models.pos_tinventory_stock_locations_response_201_data_relationships_stock_location_links import (
            POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTinventoryStockLocationsResponse201DataRelationshipsStockLocationData.from_dict(_data)

        pos_tinventory_stock_locations_response_201_data_relationships_stock_location = cls(
            links=links,
            data=data,
        )

        pos_tinventory_stock_locations_response_201_data_relationships_stock_location.additional_properties = d
        return pos_tinventory_stock_locations_response_201_data_relationships_stock_location

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
