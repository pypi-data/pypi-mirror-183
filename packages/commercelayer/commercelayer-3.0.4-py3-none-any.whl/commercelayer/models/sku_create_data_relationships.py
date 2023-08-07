from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.sku_create_data_relationships_shipping_category import SkuCreateDataRelationshipsShippingCategory


T = TypeVar("T", bound="SkuCreateDataRelationships")


@attr.s(auto_attribs=True)
class SkuCreateDataRelationships:
    """
    Attributes:
        shipping_category (SkuCreateDataRelationshipsShippingCategory):
    """

    shipping_category: "SkuCreateDataRelationshipsShippingCategory"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_category = self.shipping_category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipping_category": shipping_category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_create_data_relationships_shipping_category import SkuCreateDataRelationshipsShippingCategory

        d = src_dict.copy()
        shipping_category = SkuCreateDataRelationshipsShippingCategory.from_dict(d.pop("shipping_category"))

        sku_create_data_relationships = cls(
            shipping_category=shipping_category,
        )

        sku_create_data_relationships.additional_properties = d
        return sku_create_data_relationships

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
