from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GETtaxRulesResponse200DataItemAttributesBreakdown")


@attr.s(auto_attribs=True)
class GETtaxRulesResponse200DataItemAttributesBreakdown:
    """The breakdown for this tax rule (if calculated).

    Example:
        {'41': {'tax_rate': 0.22}}

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
        ge_ttax_rules_response_200_data_item_attributes_breakdown = cls()

        ge_ttax_rules_response_200_data_item_attributes_breakdown.additional_properties = d
        return ge_ttax_rules_response_200_data_item_attributes_breakdown

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
