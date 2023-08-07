from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.return_update_data_relationships_stock_location import ReturnUpdateDataRelationshipsStockLocation


T = TypeVar("T", bound="ReturnUpdateDataRelationships")


@attr.s(auto_attribs=True)
class ReturnUpdateDataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, ReturnUpdateDataRelationshipsStockLocation]):
    """

    stock_location: Union[Unset, "ReturnUpdateDataRelationshipsStockLocation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.return_update_data_relationships_stock_location import ReturnUpdateDataRelationshipsStockLocation

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, ReturnUpdateDataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = ReturnUpdateDataRelationshipsStockLocation.from_dict(_stock_location)

        return_update_data_relationships = cls(
            stock_location=stock_location,
        )

        return_update_data_relationships.additional_properties = d
        return return_update_data_relationships

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
