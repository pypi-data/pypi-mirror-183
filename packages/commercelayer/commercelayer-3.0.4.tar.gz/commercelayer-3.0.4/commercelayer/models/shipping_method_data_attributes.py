from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_method_data_attributes_metadata import ShippingMethodDataAttributesMetadata


T = TypeVar("T", bound="ShippingMethodDataAttributes")


@attr.s(auto_attribs=True)
class ShippingMethodDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The shipping method's name Example: Standard shipping.
        scheme (Union[Unset, str]): The shipping method's scheme, one of 'flat' or 'weight_tiered'. Example: flat.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        disabled_at (Union[Unset, str]): Time at which the shipping method was disabled. Example:
            2018-01-01T12:00:00.000Z.
        price_amount_cents (Union[Unset, int]): The price of this shipping method, in cents. Example: 1000.
        price_amount_float (Union[Unset, float]): The price of this shipping method, float. Example: 10.0.
        formatted_price_amount (Union[Unset, str]): The price of this shipping method, formatted. Example: €10,00.
        free_over_amount_cents (Union[Unset, int]): Apply free shipping if the order amount is over this value, in
            cents. Example: 9900.
        free_over_amount_float (Union[Unset, float]): Apply free shipping if the order amount is over this value, float.
            Example: 99.0.
        formatted_free_over_amount (Union[Unset, str]): Apply free shipping if the order amount is over this value,
            formatted. Example: €99,00.
        price_amount_for_shipment_cents (Union[Unset, int]): The calculated price (zero or price amount) when associated
            to a shipment, in cents.
        price_amount_for_shipment_float (Union[Unset, float]): The calculated price (zero or price amount) when
            associated to a shipment, float.
        formatted_price_amount_for_shipment (Union[Unset, str]): The calculated price (zero or price amount) when
            associated to a shipment, formatted. Example: €0,00.
        min_weight (Union[Unset, float]): The minimum weight for which this shipping method is available. Example: 3.0.
        max_weight (Union[Unset, float]): The maximum weight for which this shipping method is available. Example:
            300.0.
        unit_of_weight (Union[Unset, str]): Can be one of 'gr', 'lb', or 'oz' Example: gr.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ShippingMethodDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    scheme: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    disabled_at: Union[Unset, str] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    price_amount_float: Union[Unset, float] = UNSET
    formatted_price_amount: Union[Unset, str] = UNSET
    free_over_amount_cents: Union[Unset, int] = UNSET
    free_over_amount_float: Union[Unset, float] = UNSET
    formatted_free_over_amount: Union[Unset, str] = UNSET
    price_amount_for_shipment_cents: Union[Unset, int] = UNSET
    price_amount_for_shipment_float: Union[Unset, float] = UNSET
    formatted_price_amount_for_shipment: Union[Unset, str] = UNSET
    min_weight: Union[Unset, float] = UNSET
    max_weight: Union[Unset, float] = UNSET
    unit_of_weight: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ShippingMethodDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        scheme = self.scheme
        currency_code = self.currency_code
        disabled_at = self.disabled_at
        price_amount_cents = self.price_amount_cents
        price_amount_float = self.price_amount_float
        formatted_price_amount = self.formatted_price_amount
        free_over_amount_cents = self.free_over_amount_cents
        free_over_amount_float = self.free_over_amount_float
        formatted_free_over_amount = self.formatted_free_over_amount
        price_amount_for_shipment_cents = self.price_amount_for_shipment_cents
        price_amount_for_shipment_float = self.price_amount_for_shipment_float
        formatted_price_amount_for_shipment = self.formatted_price_amount_for_shipment
        min_weight = self.min_weight
        max_weight = self.max_weight
        unit_of_weight = self.unit_of_weight
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
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if price_amount_float is not UNSET:
            field_dict["price_amount_float"] = price_amount_float
        if formatted_price_amount is not UNSET:
            field_dict["formatted_price_amount"] = formatted_price_amount
        if free_over_amount_cents is not UNSET:
            field_dict["free_over_amount_cents"] = free_over_amount_cents
        if free_over_amount_float is not UNSET:
            field_dict["free_over_amount_float"] = free_over_amount_float
        if formatted_free_over_amount is not UNSET:
            field_dict["formatted_free_over_amount"] = formatted_free_over_amount
        if price_amount_for_shipment_cents is not UNSET:
            field_dict["price_amount_for_shipment_cents"] = price_amount_for_shipment_cents
        if price_amount_for_shipment_float is not UNSET:
            field_dict["price_amount_for_shipment_float"] = price_amount_for_shipment_float
        if formatted_price_amount_for_shipment is not UNSET:
            field_dict["formatted_price_amount_for_shipment"] = formatted_price_amount_for_shipment
        if min_weight is not UNSET:
            field_dict["min_weight"] = min_weight
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if unit_of_weight is not UNSET:
            field_dict["unit_of_weight"] = unit_of_weight
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
        from ..models.shipping_method_data_attributes_metadata import ShippingMethodDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        scheme = d.pop("scheme", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        disabled_at = d.pop("disabled_at", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        price_amount_float = d.pop("price_amount_float", UNSET)

        formatted_price_amount = d.pop("formatted_price_amount", UNSET)

        free_over_amount_cents = d.pop("free_over_amount_cents", UNSET)

        free_over_amount_float = d.pop("free_over_amount_float", UNSET)

        formatted_free_over_amount = d.pop("formatted_free_over_amount", UNSET)

        price_amount_for_shipment_cents = d.pop("price_amount_for_shipment_cents", UNSET)

        price_amount_for_shipment_float = d.pop("price_amount_for_shipment_float", UNSET)

        formatted_price_amount_for_shipment = d.pop("formatted_price_amount_for_shipment", UNSET)

        min_weight = d.pop("min_weight", UNSET)

        max_weight = d.pop("max_weight", UNSET)

        unit_of_weight = d.pop("unit_of_weight", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ShippingMethodDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ShippingMethodDataAttributesMetadata.from_dict(_metadata)

        shipping_method_data_attributes = cls(
            name=name,
            scheme=scheme,
            currency_code=currency_code,
            disabled_at=disabled_at,
            price_amount_cents=price_amount_cents,
            price_amount_float=price_amount_float,
            formatted_price_amount=formatted_price_amount,
            free_over_amount_cents=free_over_amount_cents,
            free_over_amount_float=free_over_amount_float,
            formatted_free_over_amount=formatted_free_over_amount,
            price_amount_for_shipment_cents=price_amount_for_shipment_cents,
            price_amount_for_shipment_float=price_amount_for_shipment_float,
            formatted_price_amount_for_shipment=formatted_price_amount_for_shipment,
            min_weight=min_weight,
            max_weight=max_weight,
            unit_of_weight=unit_of_weight,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        shipping_method_data_attributes.additional_properties = d
        return shipping_method_data_attributes

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
