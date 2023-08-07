from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_data_attributes_metadata import PriceDataAttributesMetadata


T = TypeVar("T", bound="PriceDataAttributes")


@attr.s(auto_attribs=True)
class PriceDataAttributes:
    """
    Attributes:
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            inherited from the associated price list. Example: EUR.
        sku_code (Union[Unset, str]): The code of the associated SKU. When creating a price, either a valid sku_code or
            a SKU relationship must be present. Example: TSHIRTMM000000FFFFFFXLXX.
        amount_cents (Union[Unset, int]): The SKU price amount for the associated price list, in cents. Example: 10000.
        amount_float (Union[Unset, float]): The SKU price amount for the associated price list, float. Example: 100.0.
        formatted_amount (Union[Unset, str]): The SKU price amount for the associated price list, formatted. Example:
            €100,00.
        compare_at_amount_cents (Union[Unset, int]): The compared price amount, in cents. Useful to display a percentage
            discount. Example: 13000.
        compare_at_amount_float (Union[Unset, float]): The compared price amount, float. Example: 130.0.
        formatted_compare_at_amount (Union[Unset, str]): The compared price amount, formatted. Example: €130,00.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, PriceDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    currency_code: Union[Unset, str] = UNSET
    sku_code: Union[Unset, str] = UNSET
    amount_cents: Union[Unset, int] = UNSET
    amount_float: Union[Unset, float] = UNSET
    formatted_amount: Union[Unset, str] = UNSET
    compare_at_amount_cents: Union[Unset, int] = UNSET
    compare_at_amount_float: Union[Unset, float] = UNSET
    formatted_compare_at_amount: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PriceDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        sku_code = self.sku_code
        amount_cents = self.amount_cents
        amount_float = self.amount_float
        formatted_amount = self.formatted_amount
        compare_at_amount_cents = self.compare_at_amount_cents
        compare_at_amount_float = self.compare_at_amount_float
        formatted_compare_at_amount = self.formatted_compare_at_amount
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
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if amount_float is not UNSET:
            field_dict["amount_float"] = amount_float
        if formatted_amount is not UNSET:
            field_dict["formatted_amount"] = formatted_amount
        if compare_at_amount_cents is not UNSET:
            field_dict["compare_at_amount_cents"] = compare_at_amount_cents
        if compare_at_amount_float is not UNSET:
            field_dict["compare_at_amount_float"] = compare_at_amount_float
        if formatted_compare_at_amount is not UNSET:
            field_dict["formatted_compare_at_amount"] = formatted_compare_at_amount
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
        from ..models.price_data_attributes_metadata import PriceDataAttributesMetadata

        d = src_dict.copy()
        currency_code = d.pop("currency_code", UNSET)

        sku_code = d.pop("sku_code", UNSET)

        amount_cents = d.pop("amount_cents", UNSET)

        amount_float = d.pop("amount_float", UNSET)

        formatted_amount = d.pop("formatted_amount", UNSET)

        compare_at_amount_cents = d.pop("compare_at_amount_cents", UNSET)

        compare_at_amount_float = d.pop("compare_at_amount_float", UNSET)

        formatted_compare_at_amount = d.pop("formatted_compare_at_amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PriceDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PriceDataAttributesMetadata.from_dict(_metadata)

        price_data_attributes = cls(
            currency_code=currency_code,
            sku_code=sku_code,
            amount_cents=amount_cents,
            amount_float=amount_float,
            formatted_amount=formatted_amount,
            compare_at_amount_cents=compare_at_amount_cents,
            compare_at_amount_float=compare_at_amount_float,
            formatted_compare_at_amount=formatted_compare_at_amount,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        price_data_attributes.additional_properties = d
        return price_data_attributes

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
