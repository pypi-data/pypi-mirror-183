from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttax_rulestax_rule_id_response_200_data_attributes_breakdown import (
        GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown,
    )
    from ..models.ge_ttax_rulestax_rule_id_response_200_data_attributes_metadata import (
        GETtaxRulestaxRuleIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="GETtaxRulestaxRuleIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETtaxRulestaxRuleIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The tax rule internal name. Example: Fixed 22%.
        tax_rate (Union[Unset, float]): The tax rate for this rule. Example: 0.22.
        country_code_regex (Union[Unset, str]): The regex that will be evaluated to match the shipping address country
            code. Example: AT|BE|BG|CZ|DK|EE|DE|HU|LV|LT.
        not_country_code_regex (Union[Unset, str]): The regex that will be evaluated as negative match for the shipping
            address country code. Example: AT|BE|BG|CZ|DK|EE|DE.
        state_code_regex (Union[Unset, str]): The regex that will be evaluated to match the shipping address state code.
            Example: A[KLRZ]|C[AOT]|D[CE]|FL.
        not_state_code_regex (Union[Unset, str]): The regex that will be evaluated as negative match for the shipping
            address state code. Example: A[KLRZ]|C[AOT].
        zip_code_regex (Union[Unset, str]): The regex that will be evaluated to match the shipping address zip code.
            Example: (?i)(JE1|JE2|JE3|JE4|JE5).
        not_zip_code_regex (Union[Unset, str]): The regex that will be evaluated as negative match for the shipping zip
            country code. Example: (?i)(JE1|JE2|JE3).
        freight_taxable (Union[Unset, bool]): Indicates if the freight is taxable.
        payment_method_taxable (Union[Unset, bool]): Indicates if the payment method is taxable.
        gift_card_taxable (Union[Unset, bool]): Indicates if gift cards are taxable.
        adjustment_taxable (Union[Unset, bool]): Indicates if adjustemnts are taxable.
        breakdown (Union[Unset, GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown]): The breakdown for this tax
            rule (if calculated). Example: {'41': {'tax_rate': 0.22}}.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETtaxRulestaxRuleIdResponse200DataAttributesMetadata]): Set of key-value pairs that you
            can attach to the resource. This can be useful for storing additional information about the resource in a
            structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    country_code_regex: Union[Unset, str] = UNSET
    not_country_code_regex: Union[Unset, str] = UNSET
    state_code_regex: Union[Unset, str] = UNSET
    not_state_code_regex: Union[Unset, str] = UNSET
    zip_code_regex: Union[Unset, str] = UNSET
    not_zip_code_regex: Union[Unset, str] = UNSET
    freight_taxable: Union[Unset, bool] = UNSET
    payment_method_taxable: Union[Unset, bool] = UNSET
    gift_card_taxable: Union[Unset, bool] = UNSET
    adjustment_taxable: Union[Unset, bool] = UNSET
    breakdown: Union[Unset, "GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETtaxRulestaxRuleIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        tax_rate = self.tax_rate
        country_code_regex = self.country_code_regex
        not_country_code_regex = self.not_country_code_regex
        state_code_regex = self.state_code_regex
        not_state_code_regex = self.not_state_code_regex
        zip_code_regex = self.zip_code_regex
        not_zip_code_regex = self.not_zip_code_regex
        freight_taxable = self.freight_taxable
        payment_method_taxable = self.payment_method_taxable
        gift_card_taxable = self.gift_card_taxable
        adjustment_taxable = self.adjustment_taxable
        breakdown: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown.to_dict()

        created_at = self.created_at
        updated_at = self.updated_at
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if country_code_regex is not UNSET:
            field_dict["country_code_regex"] = country_code_regex
        if not_country_code_regex is not UNSET:
            field_dict["not_country_code_regex"] = not_country_code_regex
        if state_code_regex is not UNSET:
            field_dict["state_code_regex"] = state_code_regex
        if not_state_code_regex is not UNSET:
            field_dict["not_state_code_regex"] = not_state_code_regex
        if zip_code_regex is not UNSET:
            field_dict["zip_code_regex"] = zip_code_regex
        if not_zip_code_regex is not UNSET:
            field_dict["not_zip_code_regex"] = not_zip_code_regex
        if freight_taxable is not UNSET:
            field_dict["freight_taxable"] = freight_taxable
        if payment_method_taxable is not UNSET:
            field_dict["payment_method_taxable"] = payment_method_taxable
        if gift_card_taxable is not UNSET:
            field_dict["gift_card_taxable"] = gift_card_taxable
        if adjustment_taxable is not UNSET:
            field_dict["adjustment_taxable"] = adjustment_taxable
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_ttax_rulestax_rule_id_response_200_data_attributes_breakdown import (
            GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown,
        )
        from ..models.ge_ttax_rulestax_rule_id_response_200_data_attributes_metadata import (
            GETtaxRulestaxRuleIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        country_code_regex = d.pop("country_code_regex", UNSET)

        not_country_code_regex = d.pop("not_country_code_regex", UNSET)

        state_code_regex = d.pop("state_code_regex", UNSET)

        not_state_code_regex = d.pop("not_state_code_regex", UNSET)

        zip_code_regex = d.pop("zip_code_regex", UNSET)

        not_zip_code_regex = d.pop("not_zip_code_regex", UNSET)

        freight_taxable = d.pop("freight_taxable", UNSET)

        payment_method_taxable = d.pop("payment_method_taxable", UNSET)

        gift_card_taxable = d.pop("gift_card_taxable", UNSET)

        adjustment_taxable = d.pop("adjustment_taxable", UNSET)

        _breakdown = d.pop("breakdown", UNSET)
        breakdown: Union[Unset, GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown]
        if isinstance(_breakdown, Unset):
            breakdown = UNSET
        else:
            breakdown = GETtaxRulestaxRuleIdResponse200DataAttributesBreakdown.from_dict(_breakdown)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETtaxRulestaxRuleIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETtaxRulestaxRuleIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_ttax_rulestax_rule_id_response_200_data_attributes = cls(
            name=name,
            tax_rate=tax_rate,
            country_code_regex=country_code_regex,
            not_country_code_regex=not_country_code_regex,
            state_code_regex=state_code_regex,
            not_state_code_regex=not_state_code_regex,
            zip_code_regex=zip_code_regex,
            not_zip_code_regex=not_zip_code_regex,
            freight_taxable=freight_taxable,
            payment_method_taxable=payment_method_taxable,
            gift_card_taxable=gift_card_taxable,
            adjustment_taxable=adjustment_taxable,
            breakdown=breakdown,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_ttax_rulestax_rule_id_response_200_data_attributes.additional_properties = d
        return ge_ttax_rulestax_rule_id_response_200_data_attributes

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
