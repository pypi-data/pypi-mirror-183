from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_create_data_relationships_price_list import PriceCreateDataRelationshipsPriceList
    from ..models.price_create_data_relationships_price_tiers import PriceCreateDataRelationshipsPriceTiers
    from ..models.price_create_data_relationships_sku import PriceCreateDataRelationshipsSku


T = TypeVar("T", bound="PriceCreateDataRelationships")


@attr.s(auto_attribs=True)
class PriceCreateDataRelationships:
    """
    Attributes:
        price_list (PriceCreateDataRelationshipsPriceList):
        sku (PriceCreateDataRelationshipsSku):
        price_tiers (Union[Unset, PriceCreateDataRelationshipsPriceTiers]):
    """

    price_list: "PriceCreateDataRelationshipsPriceList"
    sku: "PriceCreateDataRelationshipsSku"
    price_tiers: Union[Unset, "PriceCreateDataRelationshipsPriceTiers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_list = self.price_list.to_dict()

        sku = self.sku.to_dict()

        price_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_tiers, Unset):
            price_tiers = self.price_tiers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price_list": price_list,
                "sku": sku,
            }
        )
        if price_tiers is not UNSET:
            field_dict["price_tiers"] = price_tiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_create_data_relationships_price_list import PriceCreateDataRelationshipsPriceList
        from ..models.price_create_data_relationships_price_tiers import PriceCreateDataRelationshipsPriceTiers
        from ..models.price_create_data_relationships_sku import PriceCreateDataRelationshipsSku

        d = src_dict.copy()
        price_list = PriceCreateDataRelationshipsPriceList.from_dict(d.pop("price_list"))

        sku = PriceCreateDataRelationshipsSku.from_dict(d.pop("sku"))

        _price_tiers = d.pop("price_tiers", UNSET)
        price_tiers: Union[Unset, PriceCreateDataRelationshipsPriceTiers]
        if isinstance(_price_tiers, Unset):
            price_tiers = UNSET
        else:
            price_tiers = PriceCreateDataRelationshipsPriceTiers.from_dict(_price_tiers)

        price_create_data_relationships = cls(
            price_list=price_list,
            sku=sku,
            price_tiers=price_tiers,
        )

        price_create_data_relationships.additional_properties = d
        return price_create_data_relationships

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
