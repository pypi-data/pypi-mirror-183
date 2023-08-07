from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_update_data_relationships_shipping_category import SkuUpdateDataRelationshipsShippingCategory


T = TypeVar("T", bound="SkuUpdateDataRelationships")


@attr.s(auto_attribs=True)
class SkuUpdateDataRelationships:
    """
    Attributes:
        shipping_category (Union[Unset, SkuUpdateDataRelationshipsShippingCategory]):
    """

    shipping_category: Union[Unset, "SkuUpdateDataRelationshipsShippingCategory"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_category, Unset):
            shipping_category = self.shipping_category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_category is not UNSET:
            field_dict["shipping_category"] = shipping_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_update_data_relationships_shipping_category import SkuUpdateDataRelationshipsShippingCategory

        d = src_dict.copy()
        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, SkuUpdateDataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = SkuUpdateDataRelationshipsShippingCategory.from_dict(_shipping_category)

        sku_update_data_relationships = cls(
            shipping_category=shipping_category,
        )

        sku_update_data_relationships.additional_properties = d
        return sku_update_data_relationships

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
