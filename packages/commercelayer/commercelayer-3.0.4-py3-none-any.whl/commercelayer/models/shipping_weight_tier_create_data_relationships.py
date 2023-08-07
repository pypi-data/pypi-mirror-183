from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.shipping_weight_tier_create_data_relationships_shipping_method import (
        ShippingWeightTierCreateDataRelationshipsShippingMethod,
    )


T = TypeVar("T", bound="ShippingWeightTierCreateDataRelationships")


@attr.s(auto_attribs=True)
class ShippingWeightTierCreateDataRelationships:
    """
    Attributes:
        shipping_method (ShippingWeightTierCreateDataRelationshipsShippingMethod):
    """

    shipping_method: "ShippingWeightTierCreateDataRelationshipsShippingMethod"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_method = self.shipping_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipping_method": shipping_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_weight_tier_create_data_relationships_shipping_method import (
            ShippingWeightTierCreateDataRelationshipsShippingMethod,
        )

        d = src_dict.copy()
        shipping_method = ShippingWeightTierCreateDataRelationshipsShippingMethod.from_dict(d.pop("shipping_method"))

        shipping_weight_tier_create_data_relationships = cls(
            shipping_method=shipping_method,
        )

        shipping_weight_tier_create_data_relationships.additional_properties = d
        return shipping_weight_tier_create_data_relationships

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
