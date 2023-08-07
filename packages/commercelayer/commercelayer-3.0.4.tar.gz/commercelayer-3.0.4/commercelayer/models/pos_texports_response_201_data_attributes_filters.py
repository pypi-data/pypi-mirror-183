from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="POSTexportsResponse201DataAttributesFilters")


@attr.s(auto_attribs=True)
class POSTexportsResponse201DataAttributesFilters:
    """The filters used to select the records to be exported.

    Example:
        {'code_eq': 'AAA'}

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
        pos_texports_response_201_data_attributes_filters = cls()

        pos_texports_response_201_data_attributes_filters.additional_properties = d
        return pos_texports_response_201_data_attributes_filters

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
