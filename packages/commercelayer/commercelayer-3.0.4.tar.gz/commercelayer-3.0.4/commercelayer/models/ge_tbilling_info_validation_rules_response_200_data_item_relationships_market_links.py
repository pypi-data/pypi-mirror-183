from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GETbillingInfoValidationRulesResponse200DataItemRelationshipsMarketLinks")


@attr.s(auto_attribs=True)
class GETbillingInfoValidationRulesResponse200DataItemRelationshipsMarketLinks:
    """
    Attributes:
        self_ (Union[Unset, str]): URL
        related (Union[Unset, str]): URL
    """

    self_: Union[Unset, str] = UNSET
    related: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        related = self.related

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if related is not UNSET:
            field_dict["related"] = related

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        related = d.pop("related", UNSET)

        ge_tbilling_info_validation_rules_response_200_data_item_relationships_market_links = cls(
            self_=self_,
            related=related,
        )

        ge_tbilling_info_validation_rules_response_200_data_item_relationships_market_links.additional_properties = d
        return ge_tbilling_info_validation_rules_response_200_data_item_relationships_market_links

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
