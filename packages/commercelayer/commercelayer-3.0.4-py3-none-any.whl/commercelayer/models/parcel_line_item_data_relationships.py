from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parcel_line_item_data_relationships_parcel import ParcelLineItemDataRelationshipsParcel
    from ..models.parcel_line_item_data_relationships_shipment_line_item import (
        ParcelLineItemDataRelationshipsShipmentLineItem,
    )
    from ..models.parcel_line_item_data_relationships_stock_line_item import (
        ParcelLineItemDataRelationshipsStockLineItem,
    )


T = TypeVar("T", bound="ParcelLineItemDataRelationships")


@attr.s(auto_attribs=True)
class ParcelLineItemDataRelationships:
    """
    Attributes:
        parcel (Union[Unset, ParcelLineItemDataRelationshipsParcel]):
        stock_line_item (Union[Unset, ParcelLineItemDataRelationshipsStockLineItem]):
        shipment_line_item (Union[Unset, ParcelLineItemDataRelationshipsShipmentLineItem]):
    """

    parcel: Union[Unset, "ParcelLineItemDataRelationshipsParcel"] = UNSET
    stock_line_item: Union[Unset, "ParcelLineItemDataRelationshipsStockLineItem"] = UNSET
    shipment_line_item: Union[Unset, "ParcelLineItemDataRelationshipsShipmentLineItem"] = UNSET
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
        from ..models.parcel_line_item_data_relationships_parcel import ParcelLineItemDataRelationshipsParcel
        from ..models.parcel_line_item_data_relationships_shipment_line_item import (
            ParcelLineItemDataRelationshipsShipmentLineItem,
        )
        from ..models.parcel_line_item_data_relationships_stock_line_item import (
            ParcelLineItemDataRelationshipsStockLineItem,
        )

        d = src_dict.copy()
        _parcel = d.pop("parcel", UNSET)
        parcel: Union[Unset, ParcelLineItemDataRelationshipsParcel]
        if isinstance(_parcel, Unset):
            parcel = UNSET
        else:
            parcel = ParcelLineItemDataRelationshipsParcel.from_dict(_parcel)

        _stock_line_item = d.pop("stock_line_item", UNSET)
        stock_line_item: Union[Unset, ParcelLineItemDataRelationshipsStockLineItem]
        if isinstance(_stock_line_item, Unset):
            stock_line_item = UNSET
        else:
            stock_line_item = ParcelLineItemDataRelationshipsStockLineItem.from_dict(_stock_line_item)

        _shipment_line_item = d.pop("shipment_line_item", UNSET)
        shipment_line_item: Union[Unset, ParcelLineItemDataRelationshipsShipmentLineItem]
        if isinstance(_shipment_line_item, Unset):
            shipment_line_item = UNSET
        else:
            shipment_line_item = ParcelLineItemDataRelationshipsShipmentLineItem.from_dict(_shipment_line_item)

        parcel_line_item_data_relationships = cls(
            parcel=parcel,
            stock_line_item=stock_line_item,
            shipment_line_item=shipment_line_item,
        )

        parcel_line_item_data_relationships.additional_properties = d
        return parcel_line_item_data_relationships

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
