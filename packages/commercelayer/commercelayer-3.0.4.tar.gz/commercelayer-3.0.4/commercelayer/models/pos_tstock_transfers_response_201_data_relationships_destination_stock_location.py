from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tstock_transfers_response_201_data_relationships_destination_stock_location_data import (
        POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData,
    )
    from ..models.pos_tstock_transfers_response_201_data_relationships_destination_stock_location_links import (
        POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks,
    )


T = TypeVar("T", bound="POSTstockTransfersResponse201DataRelationshipsDestinationStockLocation")


@attr.s(auto_attribs=True)
class POSTstockTransfersResponse201DataRelationshipsDestinationStockLocation:
    """
    Attributes:
        links (Union[Unset, POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks]):
        data (Union[Unset, POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData]):
    """

    links: Union[Unset, "POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks"] = UNSET
    data: Union[Unset, "POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData"] = UNSET
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
        from ..models.pos_tstock_transfers_response_201_data_relationships_destination_stock_location_data import (
            POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData,
        )
        from ..models.pos_tstock_transfers_response_201_data_relationships_destination_stock_location_links import (
            POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTstockTransfersResponse201DataRelationshipsDestinationStockLocationData.from_dict(_data)

        pos_tstock_transfers_response_201_data_relationships_destination_stock_location = cls(
            links=links,
            data=data,
        )

        pos_tstock_transfers_response_201_data_relationships_destination_stock_location.additional_properties = d
        return pos_tstock_transfers_response_201_data_relationships_destination_stock_location

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
