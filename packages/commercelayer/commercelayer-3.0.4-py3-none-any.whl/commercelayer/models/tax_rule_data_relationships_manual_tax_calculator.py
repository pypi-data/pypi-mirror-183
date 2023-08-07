from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_rule_data_relationships_manual_tax_calculator_data import (
        TaxRuleDataRelationshipsManualTaxCalculatorData,
    )


T = TypeVar("T", bound="TaxRuleDataRelationshipsManualTaxCalculator")


@attr.s(auto_attribs=True)
class TaxRuleDataRelationshipsManualTaxCalculator:
    """
    Attributes:
        data (Union[Unset, TaxRuleDataRelationshipsManualTaxCalculatorData]):
    """

    data: Union[Unset, "TaxRuleDataRelationshipsManualTaxCalculatorData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_rule_data_relationships_manual_tax_calculator_data import (
            TaxRuleDataRelationshipsManualTaxCalculatorData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TaxRuleDataRelationshipsManualTaxCalculatorData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TaxRuleDataRelationshipsManualTaxCalculatorData.from_dict(_data)

        tax_rule_data_relationships_manual_tax_calculator = cls(
            data=data,
        )

        tax_rule_data_relationships_manual_tax_calculator.additional_properties = d
        return tax_rule_data_relationships_manual_tax_calculator

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
