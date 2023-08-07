from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_update_data_relationships_price_list import PriceUpdateDataRelationshipsPriceList
    from ..models.price_update_data_relationships_price_tiers import PriceUpdateDataRelationshipsPriceTiers
    from ..models.price_update_data_relationships_sku import PriceUpdateDataRelationshipsSku


T = TypeVar("T", bound="PriceUpdateDataRelationships")


@attr.s(auto_attribs=True)
class PriceUpdateDataRelationships:
    """
    Attributes:
        price_list (Union[Unset, PriceUpdateDataRelationshipsPriceList]):
        sku (Union[Unset, PriceUpdateDataRelationshipsSku]):
        price_tiers (Union[Unset, PriceUpdateDataRelationshipsPriceTiers]):
    """

    price_list: Union[Unset, "PriceUpdateDataRelationshipsPriceList"] = UNSET
    sku: Union[Unset, "PriceUpdateDataRelationshipsSku"] = UNSET
    price_tiers: Union[Unset, "PriceUpdateDataRelationshipsPriceTiers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_list, Unset):
            price_list = self.price_list.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        price_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_tiers, Unset):
            price_tiers = self.price_tiers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_list is not UNSET:
            field_dict["price_list"] = price_list
        if sku is not UNSET:
            field_dict["sku"] = sku
        if price_tiers is not UNSET:
            field_dict["price_tiers"] = price_tiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_update_data_relationships_price_list import PriceUpdateDataRelationshipsPriceList
        from ..models.price_update_data_relationships_price_tiers import PriceUpdateDataRelationshipsPriceTiers
        from ..models.price_update_data_relationships_sku import PriceUpdateDataRelationshipsSku

        d = src_dict.copy()
        _price_list = d.pop("price_list", UNSET)
        price_list: Union[Unset, PriceUpdateDataRelationshipsPriceList]
        if isinstance(_price_list, Unset):
            price_list = UNSET
        else:
            price_list = PriceUpdateDataRelationshipsPriceList.from_dict(_price_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, PriceUpdateDataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = PriceUpdateDataRelationshipsSku.from_dict(_sku)

        _price_tiers = d.pop("price_tiers", UNSET)
        price_tiers: Union[Unset, PriceUpdateDataRelationshipsPriceTiers]
        if isinstance(_price_tiers, Unset):
            price_tiers = UNSET
        else:
            price_tiers = PriceUpdateDataRelationshipsPriceTiers.from_dict(_price_tiers)

        price_update_data_relationships = cls(
            price_list=price_list,
            sku=sku,
            price_tiers=price_tiers,
        )

        price_update_data_relationships.additional_properties = d
        return price_update_data_relationships

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
