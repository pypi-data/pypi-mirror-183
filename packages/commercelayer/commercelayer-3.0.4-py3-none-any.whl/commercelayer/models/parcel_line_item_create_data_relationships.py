from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parcel_line_item_create_data_relationships_parcel import ParcelLineItemCreateDataRelationshipsParcel
    from ..models.parcel_line_item_create_data_relationships_shipment_line_item import (
        ParcelLineItemCreateDataRelationshipsShipmentLineItem,
    )
    from ..models.parcel_line_item_create_data_relationships_stock_line_item import (
        ParcelLineItemCreateDataRelationshipsStockLineItem,
    )


T = TypeVar("T", bound="ParcelLineItemCreateDataRelationships")


@attr.s(auto_attribs=True)
class ParcelLineItemCreateDataRelationships:
    """
    Attributes:
        parcel (ParcelLineItemCreateDataRelationshipsParcel):
        stock_line_item (ParcelLineItemCreateDataRelationshipsStockLineItem):
        shipment_line_item (Union[Unset, ParcelLineItemCreateDataRelationshipsShipmentLineItem]):
    """

    parcel: "ParcelLineItemCreateDataRelationshipsParcel"
    stock_line_item: "ParcelLineItemCreateDataRelationshipsStockLineItem"
    shipment_line_item: Union[Unset, "ParcelLineItemCreateDataRelationshipsShipmentLineItem"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parcel = self.parcel.to_dict()

        stock_line_item = self.stock_line_item.to_dict()

        shipment_line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_line_item, Unset):
            shipment_line_item = self.shipment_line_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parcel": parcel,
                "stock_line_item": stock_line_item,
            }
        )
        if shipment_line_item is not UNSET:
            field_dict["shipment_line_item"] = shipment_line_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parcel_line_item_create_data_relationships_parcel import (
            ParcelLineItemCreateDataRelationshipsParcel,
        )
        from ..models.parcel_line_item_create_data_relationships_shipment_line_item import (
            ParcelLineItemCreateDataRelationshipsShipmentLineItem,
        )
        from ..models.parcel_line_item_create_data_relationships_stock_line_item import (
            ParcelLineItemCreateDataRelationshipsStockLineItem,
        )

        d = src_dict.copy()
        parcel = ParcelLineItemCreateDataRelationshipsParcel.from_dict(d.pop("parcel"))

        stock_line_item = ParcelLineItemCreateDataRelationshipsStockLineItem.from_dict(d.pop("stock_line_item"))

        _shipment_line_item = d.pop("shipment_line_item", UNSET)
        shipment_line_item: Union[Unset, ParcelLineItemCreateDataRelationshipsShipmentLineItem]
        if isinstance(_shipment_line_item, Unset):
            shipment_line_item = UNSET
        else:
            shipment_line_item = ParcelLineItemCreateDataRelationshipsShipmentLineItem.from_dict(_shipment_line_item)

        parcel_line_item_create_data_relationships = cls(
            parcel=parcel,
            stock_line_item=stock_line_item,
            shipment_line_item=shipment_line_item,
        )

        parcel_line_item_create_data_relationships.additional_properties = d
        return parcel_line_item_create_data_relationships

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
