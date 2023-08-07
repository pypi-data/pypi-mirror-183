from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.price_create_data_relationships_price_tiers_data import PriceCreateDataRelationshipsPriceTiersData


T = TypeVar("T", bound="PriceCreateDataRelationshipsPriceTiers")


@attr.s(auto_attribs=True)
class PriceCreateDataRelationshipsPriceTiers:
    """
    Attributes:
        data (PriceCreateDataRelationshipsPriceTiersData):
    """

    data: "PriceCreateDataRelationshipsPriceTiersData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_create_data_relationships_price_tiers_data import PriceCreateDataRelationshipsPriceTiersData

        d = src_dict.copy()
        data = PriceCreateDataRelationshipsPriceTiersData.from_dict(d.pop("data"))

        price_create_data_relationships_price_tiers = cls(
            data=data,
        )

        price_create_data_relationships_price_tiers.additional_properties = d
        return price_create_data_relationships_price_tiers

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
