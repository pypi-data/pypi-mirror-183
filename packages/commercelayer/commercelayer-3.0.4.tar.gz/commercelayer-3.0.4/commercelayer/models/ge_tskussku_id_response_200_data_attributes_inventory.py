from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GETskusskuIdResponse200DataAttributesInventory")


@attr.s(auto_attribs=True)
class GETskusskuIdResponse200DataAttributesInventory:
    """Aggregated information about the SKU's inventory. Returned only when retrieving a single SKU.

    Example:
        {'available': True, 'quantity': 10, 'levels': [{'quantity': 4, 'delivery_lead_times': [{'shipping_method':
            {'name': 'Standard Shipping', 'reference': None, 'price_amount_cents': 700, 'free_over_amount_cents': 9900,
            'formatted_price_amount': '€7,00', 'formatted_free_over_amount': '€99,00'}, 'min': {'hours': 72, 'days': 3},
            'max': {'hours': 120, 'days': 5}}, {'shipping_method': {'name': 'Express Delivery', 'reference': None,
            'price_amount_cents': 1200, 'free_over_amount_cents': None, 'formatted_price_amount': '€12,00',
            'formatted_free_over_amount': None}, 'min': {'hours': 48, 'days': 2}, 'max': {'hours': 72, 'days': 3}}]},
            {'quantity': 6, 'delivery_lead_times': [{'shipping_method': {'name': 'Standard Shipping', 'reference': None,
            'price_amount_cents': 700, 'free_over_amount_cents': 9900, 'formatted_price_amount': '€7,00',
            'formatted_free_over_amount': '€99,00'}, 'min': {'hours': 96, 'days': 4}, 'max': {'hours': 144, 'days': 6}},
            {'shipping_method': {'name': 'Express Delivery', 'reference': None, 'price_amount_cents': 1200,
            'free_over_amount_cents': None, 'formatted_price_amount': '€12,00', 'formatted_free_over_amount': None}, 'min':
            {'hours': 72, 'days': 3}, 'max': {'hours': 96, 'days': 4}}]}]}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ge_tskussku_id_response_200_data_attributes_inventory = cls()

        ge_tskussku_id_response_200_data_attributes_inventory.additional_properties = d
        return ge_tskussku_id_response_200_data_attributes_inventory

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
