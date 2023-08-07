from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GETskuListPromotionRulesResponse200DataItemAttributesMetadata")


@attr.s(auto_attribs=True)
class GETskuListPromotionRulesResponse200DataItemAttributesMetadata:
    """Set of key-value pairs that you can attach to the resource. This can be useful for storing additional information
    about the resource in a structured format.

        Example:
            {'foo': 'bar'}

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
        ge_tsku_list_promotion_rules_response_200_data_item_attributes_metadata = cls()

        ge_tsku_list_promotion_rules_response_200_data_item_attributes_metadata.additional_properties = d
        return ge_tsku_list_promotion_rules_response_200_data_item_attributes_metadata

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
