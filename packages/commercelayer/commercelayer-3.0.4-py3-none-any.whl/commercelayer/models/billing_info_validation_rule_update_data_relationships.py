from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_info_validation_rule_update_data_relationships_market import (
        BillingInfoValidationRuleUpdateDataRelationshipsMarket,
    )


T = TypeVar("T", bound="BillingInfoValidationRuleUpdateDataRelationships")


@attr.s(auto_attribs=True)
class BillingInfoValidationRuleUpdateDataRelationships:
    """
    Attributes:
        market (Union[Unset, BillingInfoValidationRuleUpdateDataRelationshipsMarket]):
    """

    market: Union[Unset, "BillingInfoValidationRuleUpdateDataRelationshipsMarket"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_info_validation_rule_update_data_relationships_market import (
            BillingInfoValidationRuleUpdateDataRelationshipsMarket,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, BillingInfoValidationRuleUpdateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = BillingInfoValidationRuleUpdateDataRelationshipsMarket.from_dict(_market)

        billing_info_validation_rule_update_data_relationships = cls(
            market=market,
        )

        billing_info_validation_rule_update_data_relationships.additional_properties = d
        return billing_info_validation_rule_update_data_relationships

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
