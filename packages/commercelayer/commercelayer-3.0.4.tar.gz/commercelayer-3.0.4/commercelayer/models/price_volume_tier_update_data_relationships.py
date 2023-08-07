from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_volume_tier_update_data_relationships_price import PriceVolumeTierUpdateDataRelationshipsPrice


T = TypeVar("T", bound="PriceVolumeTierUpdateDataRelationships")


@attr.s(auto_attribs=True)
class PriceVolumeTierUpdateDataRelationships:
    """
    Attributes:
        price (Union[Unset, PriceVolumeTierUpdateDataRelationshipsPrice]):
    """

    price: Union[Unset, "PriceVolumeTierUpdateDataRelationshipsPrice"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_volume_tier_update_data_relationships_price import (
            PriceVolumeTierUpdateDataRelationshipsPrice,
        )

        d = src_dict.copy()
        _price = d.pop("price", UNSET)
        price: Union[Unset, PriceVolumeTierUpdateDataRelationshipsPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = PriceVolumeTierUpdateDataRelationshipsPrice.from_dict(_price)

        price_volume_tier_update_data_relationships = cls(
            price=price,
        )

        price_volume_tier_update_data_relationships.additional_properties = d
        return price_volume_tier_update_data_relationships

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
