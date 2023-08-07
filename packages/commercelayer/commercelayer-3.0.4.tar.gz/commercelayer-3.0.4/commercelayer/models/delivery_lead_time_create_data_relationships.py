from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.delivery_lead_time_create_data_relationships_shipping_method import (
        DeliveryLeadTimeCreateDataRelationshipsShippingMethod,
    )
    from ..models.delivery_lead_time_create_data_relationships_stock_location import (
        DeliveryLeadTimeCreateDataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="DeliveryLeadTimeCreateDataRelationships")


@attr.s(auto_attribs=True)
class DeliveryLeadTimeCreateDataRelationships:
    """
    Attributes:
        stock_location (DeliveryLeadTimeCreateDataRelationshipsStockLocation):
        shipping_method (DeliveryLeadTimeCreateDataRelationshipsShippingMethod):
    """

    stock_location: "DeliveryLeadTimeCreateDataRelationshipsStockLocation"
    shipping_method: "DeliveryLeadTimeCreateDataRelationshipsShippingMethod"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location = self.stock_location.to_dict()

        shipping_method = self.shipping_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stock_location": stock_location,
                "shipping_method": shipping_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_lead_time_create_data_relationships_shipping_method import (
            DeliveryLeadTimeCreateDataRelationshipsShippingMethod,
        )
        from ..models.delivery_lead_time_create_data_relationships_stock_location import (
            DeliveryLeadTimeCreateDataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        stock_location = DeliveryLeadTimeCreateDataRelationshipsStockLocation.from_dict(d.pop("stock_location"))

        shipping_method = DeliveryLeadTimeCreateDataRelationshipsShippingMethod.from_dict(d.pop("shipping_method"))

        delivery_lead_time_create_data_relationships = cls(
            stock_location=stock_location,
            shipping_method=shipping_method,
        )

        delivery_lead_time_create_data_relationships.additional_properties = d
        return delivery_lead_time_create_data_relationships

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
