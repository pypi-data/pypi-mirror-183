from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_option_data_attributes_metadata import LineItemOptionDataAttributesMetadata
    from ..models.line_item_option_data_attributes_options import LineItemOptionDataAttributesOptions


T = TypeVar("T", bound="LineItemOptionDataAttributes")


@attr.s(auto_attribs=True)
class LineItemOptionDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the line item option. When blank, it gets populated with the name of the
            associated SKU option. Example: Embossing.
        quantity (Union[Unset, int]): The line item option's quantity Example: 2.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            automatically inherited from the order's market. Example: EUR.
        unit_amount_cents (Union[Unset, int]): The unit amount of the line item option, in cents. When you add a line
            item option to an order, this is automatically populated from associated SKU option's price. Example: 990.
        unit_amount_float (Union[Unset, float]): The unit amount of the line item option, float. This can be useful to
            track the purchase on thrid party systems, e.g Google Analyitcs Enhanced Ecommerce. Example: 9.9.
        formatted_unit_amount (Union[Unset, str]): The unit amount of the line item option, formatted. This can be
            useful to display the amount with currency in you views. Example: €9,90.
        total_amount_cents (Union[Unset, int]): The unit amount x quantity, in cents. Example: 1880.
        total_amount_float (Union[Unset, float]): The unit amount x quantity, float. This can be useful to track the
            purchase on thrid party systems, e.g Google Analyitcs Enhanced Ecommerce. Example: 18.8.
        formatted_total_amount (Union[Unset, str]): The unit amount x quantity, formatted. This can be useful to display
            the amount with currency in you views. Example: €18,80.
        delay_hours (Union[Unset, int]): The shipping delay that the customer can expect when adding this option
            (hours). Inherited from the associated SKU option. Example: 48.
        delay_days (Union[Unset, int]): The shipping delay that the customer can expect when adding this option (days,
            rounded). Example: 2.
        options (Union[Unset, LineItemOptionDataAttributesOptions]): Set of key-value pairs that represent the selected
            options. Example: {'embossing_text': 'Happy Birthday!'}.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, LineItemOptionDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    currency_code: Union[Unset, str] = UNSET
    unit_amount_cents: Union[Unset, int] = UNSET
    unit_amount_float: Union[Unset, float] = UNSET
    formatted_unit_amount: Union[Unset, str] = UNSET
    total_amount_cents: Union[Unset, int] = UNSET
    total_amount_float: Union[Unset, float] = UNSET
    formatted_total_amount: Union[Unset, str] = UNSET
    delay_hours: Union[Unset, int] = UNSET
    delay_days: Union[Unset, int] = UNSET
    options: Union[Unset, "LineItemOptionDataAttributesOptions"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "LineItemOptionDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        quantity = self.quantity
        currency_code = self.currency_code
        unit_amount_cents = self.unit_amount_cents
        unit_amount_float = self.unit_amount_float
        formatted_unit_amount = self.formatted_unit_amount
        total_amount_cents = self.total_amount_cents
        total_amount_float = self.total_amount_float
        formatted_total_amount = self.formatted_total_amount
        delay_hours = self.delay_hours
        delay_days = self.delay_days
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

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
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if unit_amount_cents is not UNSET:
            field_dict["unit_amount_cents"] = unit_amount_cents
        if unit_amount_float is not UNSET:
            field_dict["unit_amount_float"] = unit_amount_float
        if formatted_unit_amount is not UNSET:
            field_dict["formatted_unit_amount"] = formatted_unit_amount
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if total_amount_float is not UNSET:
            field_dict["total_amount_float"] = total_amount_float
        if formatted_total_amount is not UNSET:
            field_dict["formatted_total_amount"] = formatted_total_amount
        if delay_hours is not UNSET:
            field_dict["delay_hours"] = delay_hours
        if delay_days is not UNSET:
            field_dict["delay_days"] = delay_days
        if options is not UNSET:
            field_dict["options"] = options
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
        from ..models.line_item_option_data_attributes_metadata import LineItemOptionDataAttributesMetadata
        from ..models.line_item_option_data_attributes_options import LineItemOptionDataAttributesOptions

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        quantity = d.pop("quantity", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        unit_amount_cents = d.pop("unit_amount_cents", UNSET)

        unit_amount_float = d.pop("unit_amount_float", UNSET)

        formatted_unit_amount = d.pop("formatted_unit_amount", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        total_amount_float = d.pop("total_amount_float", UNSET)

        formatted_total_amount = d.pop("formatted_total_amount", UNSET)

        delay_hours = d.pop("delay_hours", UNSET)

        delay_days = d.pop("delay_days", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, LineItemOptionDataAttributesOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = LineItemOptionDataAttributesOptions.from_dict(_options)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, LineItemOptionDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LineItemOptionDataAttributesMetadata.from_dict(_metadata)

        line_item_option_data_attributes = cls(
            name=name,
            quantity=quantity,
            currency_code=currency_code,
            unit_amount_cents=unit_amount_cents,
            unit_amount_float=unit_amount_float,
            formatted_unit_amount=formatted_unit_amount,
            total_amount_cents=total_amount_cents,
            total_amount_float=total_amount_float,
            formatted_total_amount=formatted_total_amount,
            delay_hours=delay_hours,
            delay_days=delay_days,
            options=options,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        line_item_option_data_attributes.additional_properties = d
        return line_item_option_data_attributes

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
