from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_rule_create_data_attributes_metadata import TaxRuleCreateDataAttributesMetadata


T = TypeVar("T", bound="TaxRuleCreateDataAttributes")


@attr.s(auto_attribs=True)
class TaxRuleCreateDataAttributes:
    """
    Attributes:
        name (str): The tax rule internal name. Example: Fixed 22%.
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
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, TaxRuleCreateDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: str
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
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "TaxRuleCreateDataAttributesMetadata"] = UNSET
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
        reference = self.reference
        reference_origin = self.reference_origin
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
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
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_rule_create_data_attributes_metadata import TaxRuleCreateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name")

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

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, TaxRuleCreateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TaxRuleCreateDataAttributesMetadata.from_dict(_metadata)

        tax_rule_create_data_attributes = cls(
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
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        tax_rule_create_data_attributes.additional_properties = d
        return tax_rule_create_data_attributes

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
