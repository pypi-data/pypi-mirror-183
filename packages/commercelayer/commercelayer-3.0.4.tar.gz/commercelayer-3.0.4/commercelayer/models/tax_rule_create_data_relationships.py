from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.tax_rule_create_data_relationships_manual_tax_calculator import (
        TaxRuleCreateDataRelationshipsManualTaxCalculator,
    )


T = TypeVar("T", bound="TaxRuleCreateDataRelationships")


@attr.s(auto_attribs=True)
class TaxRuleCreateDataRelationships:
    """
    Attributes:
        manual_tax_calculator (TaxRuleCreateDataRelationshipsManualTaxCalculator):
    """

    manual_tax_calculator: "TaxRuleCreateDataRelationshipsManualTaxCalculator"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        manual_tax_calculator = self.manual_tax_calculator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manual_tax_calculator": manual_tax_calculator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_rule_create_data_relationships_manual_tax_calculator import (
            TaxRuleCreateDataRelationshipsManualTaxCalculator,
        )

        d = src_dict.copy()
        manual_tax_calculator = TaxRuleCreateDataRelationshipsManualTaxCalculator.from_dict(
            d.pop("manual_tax_calculator")
        )

        tax_rule_create_data_relationships = cls(
            manual_tax_calculator=manual_tax_calculator,
        )

        tax_rule_create_data_relationships.additional_properties = d
        return tax_rule_create_data_relationships

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
