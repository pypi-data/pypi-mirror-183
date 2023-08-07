from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manual_tax_calculator_data_relationships_attachments import (
        ManualTaxCalculatorDataRelationshipsAttachments,
    )
    from ..models.manual_tax_calculator_data_relationships_markets import ManualTaxCalculatorDataRelationshipsMarkets
    from ..models.manual_tax_calculator_data_relationships_tax_rules import ManualTaxCalculatorDataRelationshipsTaxRules


T = TypeVar("T", bound="ManualTaxCalculatorDataRelationships")


@attr.s(auto_attribs=True)
class ManualTaxCalculatorDataRelationships:
    """
    Attributes:
        markets (Union[Unset, ManualTaxCalculatorDataRelationshipsMarkets]):
        attachments (Union[Unset, ManualTaxCalculatorDataRelationshipsAttachments]):
        tax_rules (Union[Unset, ManualTaxCalculatorDataRelationshipsTaxRules]):
    """

    markets: Union[Unset, "ManualTaxCalculatorDataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "ManualTaxCalculatorDataRelationshipsAttachments"] = UNSET
    tax_rules: Union[Unset, "ManualTaxCalculatorDataRelationshipsTaxRules"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        tax_rules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rules, Unset):
            tax_rules = self.tax_rules.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markets is not UNSET:
            field_dict["markets"] = markets
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tax_rules is not UNSET:
            field_dict["tax_rules"] = tax_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.manual_tax_calculator_data_relationships_attachments import (
            ManualTaxCalculatorDataRelationshipsAttachments,
        )
        from ..models.manual_tax_calculator_data_relationships_markets import (
            ManualTaxCalculatorDataRelationshipsMarkets,
        )
        from ..models.manual_tax_calculator_data_relationships_tax_rules import (
            ManualTaxCalculatorDataRelationshipsTaxRules,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, ManualTaxCalculatorDataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = ManualTaxCalculatorDataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, ManualTaxCalculatorDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ManualTaxCalculatorDataRelationshipsAttachments.from_dict(_attachments)

        _tax_rules = d.pop("tax_rules", UNSET)
        tax_rules: Union[Unset, ManualTaxCalculatorDataRelationshipsTaxRules]
        if isinstance(_tax_rules, Unset):
            tax_rules = UNSET
        else:
            tax_rules = ManualTaxCalculatorDataRelationshipsTaxRules.from_dict(_tax_rules)

        manual_tax_calculator_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_rules=tax_rules,
        )

        manual_tax_calculator_data_relationships.additional_properties = d
        return manual_tax_calculator_data_relationships

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
