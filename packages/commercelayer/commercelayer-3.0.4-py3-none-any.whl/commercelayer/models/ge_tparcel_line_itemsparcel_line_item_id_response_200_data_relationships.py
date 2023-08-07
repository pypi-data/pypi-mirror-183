from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_parcel import (
        GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel,
    )
    from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item import (
        GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem,
    )
    from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_stock_line_item import (
        GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem,
    )


T = TypeVar("T", bound="GETparcelLineItemsparcelLineItemIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETparcelLineItemsparcelLineItemIdResponse200DataRelationships:
    """
    Attributes:
        parcel (Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel]):
        stock_line_item (Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem]):
        shipment_line_item (Union[Unset,
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem]):
    """

    parcel: Union[Unset, "GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel"] = UNSET
    stock_line_item: Union[Unset, "GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem"] = UNSET
    shipment_line_item: Union[
        Unset, "GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parcel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parcel, Unset):
            parcel = self.parcel.to_dict()

        stock_line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_line_item, Unset):
            stock_line_item = self.stock_line_item.to_dict()

        shipment_line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_line_item, Unset):
            shipment_line_item = self.shipment_line_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parcel is not UNSET:
            field_dict["parcel"] = parcel
        if stock_line_item is not UNSET:
            field_dict["stock_line_item"] = stock_line_item
        if shipment_line_item is not UNSET:
            field_dict["shipment_line_item"] = shipment_line_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_parcel import (
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel,
        )
        from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_shipment_line_item import (
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem,
        )
        from ..models.ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships_stock_line_item import (
            GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem,
        )

        d = src_dict.copy()
        _parcel = d.pop("parcel", UNSET)
        parcel: Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel]
        if isinstance(_parcel, Unset):
            parcel = UNSET
        else:
            parcel = GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsParcel.from_dict(_parcel)

        _stock_line_item = d.pop("stock_line_item", UNSET)
        stock_line_item: Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem]
        if isinstance(_stock_line_item, Unset):
            stock_line_item = UNSET
        else:
            stock_line_item = GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsStockLineItem.from_dict(
                _stock_line_item
            )

        _shipment_line_item = d.pop("shipment_line_item", UNSET)
        shipment_line_item: Union[Unset, GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem]
        if isinstance(_shipment_line_item, Unset):
            shipment_line_item = UNSET
        else:
            shipment_line_item = (
                GETparcelLineItemsparcelLineItemIdResponse200DataRelationshipsShipmentLineItem.from_dict(
                    _shipment_line_item
                )
            )

        ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships = cls(
            parcel=parcel,
            stock_line_item=stock_line_item,
            shipment_line_item=shipment_line_item,
        )

        ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships.additional_properties = d
        return ge_tparcel_line_itemsparcel_line_item_id_response_200_data_relationships

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
