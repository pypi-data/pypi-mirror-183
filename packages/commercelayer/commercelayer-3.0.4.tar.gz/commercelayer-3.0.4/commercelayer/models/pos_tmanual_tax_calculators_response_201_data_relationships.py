from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_attachments import (
        POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_markets import (
        POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets,
    )
    from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_tax_rules import (
        POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules,
    )


T = TypeVar("T", bound="POSTmanualTaxCalculatorsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTmanualTaxCalculatorsResponse201DataRelationships:
    """
    Attributes:
        markets (Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets]):
        attachments (Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments]):
        tax_rules (Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules]):
    """

    markets: Union[Unset, "POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments"] = UNSET
    tax_rules: Union[Unset, "POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules"] = UNSET
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
        from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_attachments import (
            POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_markets import (
            POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets,
        )
        from ..models.pos_tmanual_tax_calculators_response_201_data_relationships_tax_rules import (
            POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = POSTmanualTaxCalculatorsResponse201DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTmanualTaxCalculatorsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        _tax_rules = d.pop("tax_rules", UNSET)
        tax_rules: Union[Unset, POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules]
        if isinstance(_tax_rules, Unset):
            tax_rules = UNSET
        else:
            tax_rules = POSTmanualTaxCalculatorsResponse201DataRelationshipsTaxRules.from_dict(_tax_rules)

        pos_tmanual_tax_calculators_response_201_data_relationships = cls(
            markets=markets,
            attachments=attachments,
            tax_rules=tax_rules,
        )

        pos_tmanual_tax_calculators_response_201_data_relationships.additional_properties = d
        return pos_tmanual_tax_calculators_response_201_data_relationships

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
