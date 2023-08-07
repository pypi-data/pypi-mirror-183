from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_transfer_update_data_relationships_destination_stock_location import (
        StockTransferUpdateDataRelationshipsDestinationStockLocation,
    )
    from ..models.stock_transfer_update_data_relationships_origin_stock_location import (
        StockTransferUpdateDataRelationshipsOriginStockLocation,
    )
    from ..models.stock_transfer_update_data_relationships_sku import StockTransferUpdateDataRelationshipsSku


T = TypeVar("T", bound="StockTransferUpdateDataRelationships")


@attr.s(auto_attribs=True)
class StockTransferUpdateDataRelationships:
    """
    Attributes:
        sku (Union[Unset, StockTransferUpdateDataRelationshipsSku]):
        origin_stock_location (Union[Unset, StockTransferUpdateDataRelationshipsOriginStockLocation]):
        destination_stock_location (Union[Unset, StockTransferUpdateDataRelationshipsDestinationStockLocation]):
    """

    sku: Union[Unset, "StockTransferUpdateDataRelationshipsSku"] = UNSET
    origin_stock_location: Union[Unset, "StockTransferUpdateDataRelationshipsOriginStockLocation"] = UNSET
    destination_stock_location: Union[Unset, "StockTransferUpdateDataRelationshipsDestinationStockLocation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        origin_stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_stock_location, Unset):
            origin_stock_location = self.origin_stock_location.to_dict()

        destination_stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination_stock_location, Unset):
            destination_stock_location = self.destination_stock_location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if origin_stock_location is not UNSET:
            field_dict["origin_stock_location"] = origin_stock_location
        if destination_stock_location is not UNSET:
            field_dict["destination_stock_location"] = destination_stock_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_transfer_update_data_relationships_destination_stock_location import (
            StockTransferUpdateDataRelationshipsDestinationStockLocation,
        )
        from ..models.stock_transfer_update_data_relationships_origin_stock_location import (
            StockTransferUpdateDataRelationshipsOriginStockLocation,
        )
        from ..models.stock_transfer_update_data_relationships_sku import StockTransferUpdateDataRelationshipsSku

        d = src_dict.copy()
        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, StockTransferUpdateDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = StockTransferUpdateDataRelationshipsSku.from_dict(_sku)

        _origin_stock_location = d.pop("origin_stock_location", UNSET)
        origin_stock_location: Union[Unset, StockTransferUpdateDataRelationshipsOriginStockLocation]
        if isinstance(_origin_stock_location, Unset):
            origin_stock_location = UNSET
        else:
            origin_stock_location = StockTransferUpdateDataRelationshipsOriginStockLocation.from_dict(
                _origin_stock_location
            )

        _destination_stock_location = d.pop("destination_stock_location", UNSET)
        destination_stock_location: Union[Unset, StockTransferUpdateDataRelationshipsDestinationStockLocation]
        if isinstance(_destination_stock_location, Unset):
            destination_stock_location = UNSET
        else:
            destination_stock_location = StockTransferUpdateDataRelationshipsDestinationStockLocation.from_dict(
                _destination_stock_location
            )

        stock_transfer_update_data_relationships = cls(
            sku=sku,
            origin_stock_location=origin_stock_location,
            destination_stock_location=destination_stock_location,
        )

        stock_transfer_update_data_relationships.additional_properties = d
        return stock_transfer_update_data_relationships

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
