from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.price_volume_tier_create_data_relationships_price import PriceVolumeTierCreateDataRelationshipsPrice


T = TypeVar("T", bound="PriceVolumeTierCreateDataRelationships")


@attr.s(auto_attribs=True)
class PriceVolumeTierCreateDataRelationships:
    """
    Attributes:
        price (PriceVolumeTierCreateDataRelationshipsPrice):
    """

    price: "PriceVolumeTierCreateDataRelationshipsPrice"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_volume_tier_create_data_relationships_price import (
            PriceVolumeTierCreateDataRelationshipsPrice,
        )

        d = src_dict.copy()
        price = PriceVolumeTierCreateDataRelationshipsPrice.from_dict(d.pop("price"))

        price_volume_tier_create_data_relationships = cls(
            price=price,
        )

        price_volume_tier_create_data_relationships.additional_properties = d
        return price_volume_tier_create_data_relationships

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
