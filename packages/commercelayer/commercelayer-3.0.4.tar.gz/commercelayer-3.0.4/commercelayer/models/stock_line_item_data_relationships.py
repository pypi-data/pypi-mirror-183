from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_line_item_data_relationships_line_item import StockLineItemDataRelationshipsLineItem
    from ..models.stock_line_item_data_relationships_shipment import StockLineItemDataRelationshipsShipment
    from ..models.stock_line_item_data_relationships_stock_item import StockLineItemDataRelationshipsStockItem


T = TypeVar("T", bound="StockLineItemDataRelationships")


@attr.s(auto_attribs=True)
class StockLineItemDataRelationships:
    """
    Attributes:
        shipment (Union[Unset, StockLineItemDataRelationshipsShipment]):
        line_item (Union[Unset, StockLineItemDataRelationshipsLineItem]):
        stock_item (Union[Unset, StockLineItemDataRelationshipsStockItem]):
    """

    shipment: Union[Unset, "StockLineItemDataRelationshipsShipment"] = UNSET
    line_item: Union[Unset, "StockLineItemDataRelationshipsLineItem"] = UNSET
    stock_item: Union[Unset, "StockLineItemDataRelationshipsStockItem"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        stock_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_item, Unset):
            stock_item = self.stock_item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if line_item is not UNSET:
            field_dict["line_item"] = line_item
        if stock_item is not UNSET:
            field_dict["stock_item"] = stock_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_line_item_data_relationships_line_item import StockLineItemDataRelationshipsLineItem
        from ..models.stock_line_item_data_relationships_shipment import StockLineItemDataRelationshipsShipment
        from ..models.stock_line_item_data_relationships_stock_item import StockLineItemDataRelationshipsStockItem

        d = src_dict.copy()
        _shipment = d.pop("shipment", UNSET)
        shipment: Union[Unset, StockLineItemDataRelationshipsShipment]
        if isinstance(_shipment, Unset):
            shipment = UNSET
        else:
            shipment = StockLineItemDataRelationshipsShipment.from_dict(_shipment)

        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, StockLineItemDataRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = StockLineItemDataRelationshipsLineItem.from_dict(_line_item)

        _stock_item = d.pop("stock_item", UNSET)
        stock_item: Union[Unset, StockLineItemDataRelationshipsStockItem]
        if isinstance(_stock_item, Unset):
            stock_item = UNSET
        else:
            stock_item = StockLineItemDataRelationshipsStockItem.from_dict(_stock_item)

        stock_line_item_data_relationships = cls(
            shipment=shipment,
            line_item=line_item,
            stock_item=stock_item,
        )

        stock_line_item_data_relationships.additional_properties = d
        return stock_line_item_data_relationships

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
