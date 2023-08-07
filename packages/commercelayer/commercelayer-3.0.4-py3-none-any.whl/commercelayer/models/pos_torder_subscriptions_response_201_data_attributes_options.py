from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="POSTorderSubscriptionsResponse201DataAttributesOptions")


@attr.s(auto_attribs=True)
class POSTorderSubscriptionsResponse201DataAttributesOptions:
    """The subscription options used to create the order copy (check order_copies for more information). For subscriptions
    the `place_target_order` is enabled by default, specify custom options to overwrite it.

        Example:
            {'place_target_order': False}

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
        pos_torder_subscriptions_response_201_data_attributes_options = cls()

        pos_torder_subscriptions_response_201_data_attributes_options.additional_properties = d
        return pos_torder_subscriptions_response_201_data_attributes_options

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
