from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_attachments import (
        PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_markets import (
        PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets,
    )
    from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_tax_rules import (
        PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules,
    )


T = TypeVar("T", bound="PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationships:
    """
    Attributes:
        markets (Union[Unset, PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets]):
        attachments (Union[Unset,
            PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments]):
        tax_rules (Union[Unset, PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules]):
    """

    markets: Union[Unset, "PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets"] = UNSET
    attachments: Union[
        Unset, "PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments"
    ] = UNSET
    tax_rules: Union[
        Unset, "PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules"
    ] = UNSET
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
        from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_attachments import (
            PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_markets import (
            PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets,
        )
        from ..models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships_tax_rules import (
            PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsMarkets.from_dict(
                _markets
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsAttachments.from_dict(
                    _attachments
                )
            )

        _tax_rules = d.pop("tax_rules", UNSET)
        tax_rules: Union[Unset, PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules]
        if isinstance(_tax_rules, Unset):
            tax_rules = UNSET
        else:
            tax_rules = PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200DataRelationshipsTaxRules.from_dict(
                _tax_rules
            )

        patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_rules=tax_rules,
        )

        patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships.additional_properties = d
        return patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200_data_relationships

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
