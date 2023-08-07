from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manual_tax_calculator_create_data_relationships_tax_rules import (
        ManualTaxCalculatorCreateDataRelationshipsTaxRules,
    )


T = TypeVar("T", bound="ManualTaxCalculatorCreateDataRelationships")


@attr.s(auto_attribs=True)
class ManualTaxCalculatorCreateDataRelationships:
    """
    Attributes:
        tax_rules (Union[Unset, ManualTaxCalculatorCreateDataRelationshipsTaxRules]):
    """

    tax_rules: Union[Unset, "ManualTaxCalculatorCreateDataRelationshipsTaxRules"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_rules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rules, Unset):
            tax_rules = self.tax_rules.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_rules is not UNSET:
            field_dict["tax_rules"] = tax_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.manual_tax_calculator_create_data_relationships_tax_rules import (
            ManualTaxCalculatorCreateDataRelationshipsTaxRules,
        )

        d = src_dict.copy()
        _tax_rules = d.pop("tax_rules", UNSET)
        tax_rules: Union[Unset, ManualTaxCalculatorCreateDataRelationshipsTaxRules]
        if isinstance(_tax_rules, Unset):
            tax_rules = UNSET
        else:
            tax_rules = ManualTaxCalculatorCreateDataRelationshipsTaxRules.from_dict(_tax_rules)

        manual_tax_calculator_create_data_relationships = cls(
            tax_rules=tax_rules,
        )

        manual_tax_calculator_create_data_relationships.additional_properties = d
        return manual_tax_calculator_create_data_relationships

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
