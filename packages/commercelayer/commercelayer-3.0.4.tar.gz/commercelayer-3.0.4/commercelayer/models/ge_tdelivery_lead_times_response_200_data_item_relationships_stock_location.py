from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location_data import (
        GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData,
    )
    from ..models.ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location_links import (
        GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks,
    )


T = TypeVar("T", bound="GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocation")


@attr.s(auto_attribs=True)
class GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocation:
    """
    Attributes:
        links (Union[Unset, GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks]):
        data (Union[Unset, GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData]):
    """

    links: Union[Unset, "GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks"] = UNSET
    data: Union[Unset, "GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData"] = UNSET
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
        from ..models.ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location_data import (
            GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData,
        )
        from ..models.ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location_links import (
            GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETdeliveryLeadTimesResponse200DataItemRelationshipsStockLocationData.from_dict(_data)

        ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location = cls(
            links=links,
            data=data,
        )

        ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location.additional_properties = d
        return ge_tdelivery_lead_times_response_200_data_item_relationships_stock_location

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
