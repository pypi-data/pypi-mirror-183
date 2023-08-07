from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_option_data_attributes_metadata import SkuOptionDataAttributesMetadata


T = TypeVar("T", bound="SkuOptionDataAttributes")


@attr.s(auto_attribs=True)
class SkuOptionDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The SKU option's internal name Example: Embossing.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        description (Union[Unset, str]): An internal description of the SKU option. Example: Lorem ipsum dolor sit amet,
            consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
        price_amount_cents (Union[Unset, int]): The price of this shipping method, in cents. Example: 1000.
        price_amount_float (Union[Unset, float]): The price of this shipping method, float. Example: 10.0.
        formatted_price_amount (Union[Unset, str]): The price of this shipping method, formatted. Example: €10,00.
        delay_hours (Union[Unset, int]): The delay time (in hours) that should be added to the delivery lead time when
            this option is purchased. Example: 48.
        delay_days (Union[Unset, int]): The delay time, in days (rounded) Example: 2.
        sku_code_regex (Union[Unset, str]): The regex that will be evaluated to match the SKU codes. Example: ^(A|B).*$.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, SkuOptionDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    price_amount_float: Union[Unset, float] = UNSET
    formatted_price_amount: Union[Unset, str] = UNSET
    delay_hours: Union[Unset, int] = UNSET
    delay_days: Union[Unset, int] = UNSET
    sku_code_regex: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "SkuOptionDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_code = self.currency_code
        description = self.description
        price_amount_cents = self.price_amount_cents
        price_amount_float = self.price_amount_float
        formatted_price_amount = self.formatted_price_amount
        delay_hours = self.delay_hours
        delay_days = self.delay_days
        sku_code_regex = self.sku_code_regex
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if price_amount_float is not UNSET:
            field_dict["price_amount_float"] = price_amount_float
        if formatted_price_amount is not UNSET:
            field_dict["formatted_price_amount"] = formatted_price_amount
        if delay_hours is not UNSET:
            field_dict["delay_hours"] = delay_hours
        if delay_days is not UNSET:
            field_dict["delay_days"] = delay_days
        if sku_code_regex is not UNSET:
            field_dict["sku_code_regex"] = sku_code_regex
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
        from ..models.sku_option_data_attributes_metadata import SkuOptionDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        description = d.pop("description", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        price_amount_float = d.pop("price_amount_float", UNSET)

        formatted_price_amount = d.pop("formatted_price_amount", UNSET)

        delay_hours = d.pop("delay_hours", UNSET)

        delay_days = d.pop("delay_days", UNSET)

        sku_code_regex = d.pop("sku_code_regex", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, SkuOptionDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SkuOptionDataAttributesMetadata.from_dict(_metadata)

        sku_option_data_attributes = cls(
            name=name,
            currency_code=currency_code,
            description=description,
            price_amount_cents=price_amount_cents,
            price_amount_float=price_amount_float,
            formatted_price_amount=formatted_price_amount,
            delay_hours=delay_hours,
            delay_days=delay_days,
            sku_code_regex=sku_code_regex,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        sku_option_data_attributes.additional_properties = d
        return sku_option_data_attributes

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
