from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location_data import (
        PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData,
    )
    from ..models.patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location_links import (
        PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks,
    )


T = TypeVar("T", bound="PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation")


@attr.s(auto_attribs=True)
class PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocation:
    """
    Attributes:
        links (Union[Unset,
            PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks]):
        data (Union[Unset,
            PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData]):
    """

    links: Union[
        Unset, "PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks"
    ] = UNSET
    data: Union[
        Unset, "PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData"
    ] = UNSET
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
        from ..models.patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location_data import (
            PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData,
        )
        from ..models.patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location_links import (
            PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHinventoryStockLocationsinventoryStockLocationIdResponse200DataRelationshipsStockLocationData.from_dict(
                _data
            )

        patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location = cls(
            links=links,
            data=data,
        )

        patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location.additional_properties = (
            d
        )
        return patc_hinventory_stock_locationsinventory_stock_location_id_response_200_data_relationships_stock_location

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
