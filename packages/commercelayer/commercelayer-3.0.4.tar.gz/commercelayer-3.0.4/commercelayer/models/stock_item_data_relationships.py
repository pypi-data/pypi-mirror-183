from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_item_data_relationships_attachments import StockItemDataRelationshipsAttachments
    from ..models.stock_item_data_relationships_sku import StockItemDataRelationshipsSku
    from ..models.stock_item_data_relationships_stock_location import StockItemDataRelationshipsStockLocation


T = TypeVar("T", bound="StockItemDataRelationships")


@attr.s(auto_attribs=True)
class StockItemDataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, StockItemDataRelationshipsStockLocation]):
        sku (Union[Unset, StockItemDataRelationshipsSku]):
        attachments (Union[Unset, StockItemDataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "StockItemDataRelationshipsStockLocation"] = UNSET
    sku: Union[Unset, "StockItemDataRelationshipsSku"] = UNSET
    attachments: Union[Unset, "StockItemDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if sku is not UNSET:
            field_dict["sku"] = sku
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_item_data_relationships_attachments import StockItemDataRelationshipsAttachments
        from ..models.stock_item_data_relationships_sku import StockItemDataRelationshipsSku
        from ..models.stock_item_data_relationships_stock_location import StockItemDataRelationshipsStockLocation

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, StockItemDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = StockItemDataRelationshipsStockLocation.from_dict(_stock_location)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, StockItemDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = StockItemDataRelationshipsSku.from_dict(_sku)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, StockItemDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = StockItemDataRelationshipsAttachments.from_dict(_attachments)

        stock_item_data_relationships = cls(
            stock_location=stock_location,
            sku=sku,
            attachments=attachments,
        )

        stock_item_data_relationships.additional_properties = d
        return stock_item_data_relationships

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
