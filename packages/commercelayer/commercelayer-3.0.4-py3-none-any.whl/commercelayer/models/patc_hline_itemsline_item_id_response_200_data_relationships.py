from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_item import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsItem,
    )
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_line_item_options import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions,
    )
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_order import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsOrder,
    )
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_shipment_line_items import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems,
    )
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_stock_line_items import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems,
    )
    from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_stock_transfers import (
        PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers,
    )


T = TypeVar("T", bound="PATCHlineItemslineItemIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHlineItemslineItemIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsOrder]):
        item (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsItem]):
        line_item_options (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions]):
        shipment_line_items (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems]):
        stock_line_items (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems]):
        stock_transfers (Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers]):
    """

    order: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsOrder"] = UNSET
    item: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsItem"] = UNSET
    line_item_options: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions"] = UNSET
    shipment_line_items: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems"] = UNSET
    stock_line_items: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems"] = UNSET
    stock_transfers: Union[Unset, "PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        line_item_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item_options, Unset):
            line_item_options = self.line_item_options.to_dict()

        shipment_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_line_items, Unset):
            shipment_line_items = self.shipment_line_items.to_dict()

        stock_line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_line_items, Unset):
            stock_line_items = self.stock_line_items.to_dict()

        stock_transfers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_transfers, Unset):
            stock_transfers = self.stock_transfers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if item is not UNSET:
            field_dict["item"] = item
        if line_item_options is not UNSET:
            field_dict["line_item_options"] = line_item_options
        if shipment_line_items is not UNSET:
            field_dict["shipment_line_items"] = shipment_line_items
        if stock_line_items is not UNSET:
            field_dict["stock_line_items"] = stock_line_items
        if stock_transfers is not UNSET:
            field_dict["stock_transfers"] = stock_transfers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_item import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsItem,
        )
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_line_item_options import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions,
        )
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_order import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsOrder,
        )
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_shipment_line_items import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems,
        )
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_stock_line_items import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems,
        )
        from ..models.patc_hline_itemsline_item_id_response_200_data_relationships_stock_transfers import (
            PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PATCHlineItemslineItemIdResponse200DataRelationshipsOrder.from_dict(_order)

        _item = d.pop("item", UNSET)
        item: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = PATCHlineItemslineItemIdResponse200DataRelationshipsItem.from_dict(_item)

        _line_item_options = d.pop("line_item_options", UNSET)
        line_item_options: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions]
        if isinstance(_line_item_options, Unset):
            line_item_options = UNSET
        else:
            line_item_options = PATCHlineItemslineItemIdResponse200DataRelationshipsLineItemOptions.from_dict(
                _line_item_options
            )

        _shipment_line_items = d.pop("shipment_line_items", UNSET)
        shipment_line_items: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems]
        if isinstance(_shipment_line_items, Unset):
            shipment_line_items = UNSET
        else:
            shipment_line_items = PATCHlineItemslineItemIdResponse200DataRelationshipsShipmentLineItems.from_dict(
                _shipment_line_items
            )

        _stock_line_items = d.pop("stock_line_items", UNSET)
        stock_line_items: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems]
        if isinstance(_stock_line_items, Unset):
            stock_line_items = UNSET
        else:
            stock_line_items = PATCHlineItemslineItemIdResponse200DataRelationshipsStockLineItems.from_dict(
                _stock_line_items
            )

        _stock_transfers = d.pop("stock_transfers", UNSET)
        stock_transfers: Union[Unset, PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers]
        if isinstance(_stock_transfers, Unset):
            stock_transfers = UNSET
        else:
            stock_transfers = PATCHlineItemslineItemIdResponse200DataRelationshipsStockTransfers.from_dict(
                _stock_transfers
            )

        patc_hline_itemsline_item_id_response_200_data_relationships = cls(
            order=order,
            item=item,
            line_item_options=line_item_options,
            shipment_line_items=shipment_line_items,
            stock_line_items=stock_line_items,
            stock_transfers=stock_transfers,
        )

        patc_hline_itemsline_item_id_response_200_data_relationships.additional_properties = d
        return patc_hline_itemsline_item_id_response_200_data_relationships

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
