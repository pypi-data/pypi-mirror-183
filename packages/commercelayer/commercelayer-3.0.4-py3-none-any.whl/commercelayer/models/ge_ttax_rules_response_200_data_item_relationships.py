from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttax_rules_response_200_data_item_relationships_manual_tax_calculator import (
        GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator,
    )


T = TypeVar("T", bound="GETtaxRulesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETtaxRulesResponse200DataItemRelationships:
    """
    Attributes:
        manual_tax_calculator (Union[Unset, GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator]):
    """

    manual_tax_calculator: Union[Unset, "GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        manual_tax_calculator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manual_tax_calculator, Unset):
            manual_tax_calculator = self.manual_tax_calculator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manual_tax_calculator is not UNSET:
            field_dict["manual_tax_calculator"] = manual_tax_calculator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_ttax_rules_response_200_data_item_relationships_manual_tax_calculator import (
            GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator,
        )

        d = src_dict.copy()
        _manual_tax_calculator = d.pop("manual_tax_calculator", UNSET)
        manual_tax_calculator: Union[Unset, GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator]
        if isinstance(_manual_tax_calculator, Unset):
            manual_tax_calculator = UNSET
        else:
            manual_tax_calculator = GETtaxRulesResponse200DataItemRelationshipsManualTaxCalculator.from_dict(
                _manual_tax_calculator
            )

        ge_ttax_rules_response_200_data_item_relationships = cls(
            manual_tax_calculator=manual_tax_calculator,
        )

        ge_ttax_rules_response_200_data_item_relationships.additional_properties = d
        return ge_ttax_rules_response_200_data_item_relationships

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
