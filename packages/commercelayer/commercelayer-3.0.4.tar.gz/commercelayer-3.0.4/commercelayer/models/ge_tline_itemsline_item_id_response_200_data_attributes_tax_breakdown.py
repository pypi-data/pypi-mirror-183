from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GETlineItemslineItemIdResponse200DataAttributesTaxBreakdown")


@attr.s(auto_attribs=True)
class GETlineItemslineItemIdResponse200DataAttributesTaxBreakdown:
    """The tax breakdown for this line item (if calculated).

    Example:
        {'id': '1234', 'city_amount': '0.0', 'state_amount': 6.6, 'city_tax_rate': 0.0, 'county_amount': 2.78,
            'taxable_amount': 139.0, 'county_tax_rate': 0.02, 'tax_collectable': 10.08, 'special_tax_rate': 0.005,
            'combined_tax_rate': 0.0725, 'city_taxable_amount': 0.0, 'state_sales_tax_rate': 0.0475, 'state_taxable_amount':
            139.0, 'county_taxable_amount': 139.0, 'special_district_amount': 0.7, 'special_district_taxable_amount': 139.0}

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
        ge_tline_itemsline_item_id_response_200_data_attributes_tax_breakdown = cls()

        ge_tline_itemsline_item_id_response_200_data_attributes_tax_breakdown.additional_properties = d
        return ge_tline_itemsline_item_id_response_200_data_attributes_tax_breakdown

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
