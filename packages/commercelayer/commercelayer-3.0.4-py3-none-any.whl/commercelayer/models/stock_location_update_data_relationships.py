from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_location_update_data_relationships_address import StockLocationUpdateDataRelationshipsAddress


T = TypeVar("T", bound="StockLocationUpdateDataRelationships")


@attr.s(auto_attribs=True)
class StockLocationUpdateDataRelationships:
    """
    Attributes:
        address (Union[Unset, StockLocationUpdateDataRelationshipsAddress]):
    """

    address: Union[Unset, "StockLocationUpdateDataRelationshipsAddress"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_location_update_data_relationships_address import (
            StockLocationUpdateDataRelationshipsAddress,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, StockLocationUpdateDataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = StockLocationUpdateDataRelationshipsAddress.from_dict(_address)

        stock_location_update_data_relationships = cls(
            address=address,
        )

        stock_location_update_data_relationships.additional_properties = d
        return stock_location_update_data_relationships

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
