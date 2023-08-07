from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_item_create_data_relationships_sku import StockItemCreateDataRelationshipsSku
    from ..models.stock_item_create_data_relationships_stock_location import (
        StockItemCreateDataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="StockItemCreateDataRelationships")


@attr.s(auto_attribs=True)
class StockItemCreateDataRelationships:
    """
    Attributes:
        stock_location (StockItemCreateDataRelationshipsStockLocation):
        sku (Union[Unset, StockItemCreateDataRelationshipsSku]):
    """

    stock_location: "StockItemCreateDataRelationshipsStockLocation"
    sku: Union[Unset, "StockItemCreateDataRelationshipsSku"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location = self.stock_location.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stock_location": stock_location,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_item_create_data_relationships_sku import StockItemCreateDataRelationshipsSku
        from ..models.stock_item_create_data_relationships_stock_location import (
            StockItemCreateDataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        stock_location = StockItemCreateDataRelationshipsStockLocation.from_dict(d.pop("stock_location"))

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, StockItemCreateDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = StockItemCreateDataRelationshipsSku.from_dict(_sku)

        stock_item_create_data_relationships = cls(
            stock_location=stock_location,
            sku=sku,
        )

        stock_item_create_data_relationships.additional_properties = d
        return stock_item_create_data_relationships

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
