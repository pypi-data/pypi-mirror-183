from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item_data import (
        GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData,
    )
    from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item_links import (
        GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks,
    )


T = TypeVar("T", bound="GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem")


@attr.s(auto_attribs=True)
class GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem:
    """
    Attributes:
        links (Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks]):
        data (Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData]):
    """

    links: Union[Unset, "GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks"] = UNSET
    data: Union[Unset, "GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData"] = UNSET
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
        from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item_data import (
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData,
        )
        from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item_links import (
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItemData.from_dict(_data)

        ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item = cls(
            links=links,
            data=data,
        )

        ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item.additional_properties = (
            d
        )
        return ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item

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
