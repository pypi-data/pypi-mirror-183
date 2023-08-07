from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hsku_optionssku_option_id_response_200_data_attributes_metadata import (
        PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata,
    )


T = TypeVar("T", bound="PATCHskuOptionsskuOptionIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class PATCHskuOptionsskuOptionIdResponse200DataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The SKU option's internal name Example: Embossing.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        description (Union[Unset, str]): An internal description of the SKU option. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        price_amount_cents (Union[Unset, int]): The price of this shipping method, in cents. Example: 1000.
        delay_hours (Union[Unset, int]): The delay time (in hours) that should be added to the delivery lead time when
            this option is purchased. Example: 48.
        sku_code_regex (Union[Unset, str]): The regex that will be evaluated to match the SKU codes. Example: ^(A|B).*$.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata]): Set of key-value pairs
            that you can attach to the resource. This can be useful for storing additional information about the resource in
            a structured format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    delay_hours: Union[Unset, int] = UNSET
    sku_code_regex: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_code = self.currency_code
        description = self.description
        price_amount_cents = self.price_amount_cents
        delay_hours = self.delay_hours
        sku_code_regex = self.sku_code_regex
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if delay_hours is not UNSET:
            field_dict["delay_hours"] = delay_hours
        if sku_code_regex is not UNSET:
            field_dict["sku_code_regex"] = sku_code_regex
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hsku_optionssku_option_id_response_200_data_attributes_metadata import (
            PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        description = d.pop("description", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        delay_hours = d.pop("delay_hours", UNSET)

        sku_code_regex = d.pop("sku_code_regex", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PATCHskuOptionsskuOptionIdResponse200DataAttributesMetadata.from_dict(_metadata)

        patc_hsku_optionssku_option_id_response_200_data_attributes = cls(
            name=name,
            currency_code=currency_code,
            description=description,
            price_amount_cents=price_amount_cents,
            delay_hours=delay_hours,
            sku_code_regex=sku_code_regex,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        patc_hsku_optionssku_option_id_response_200_data_attributes.additional_properties = d
        return patc_hsku_optionssku_option_id_response_200_data_attributes

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
