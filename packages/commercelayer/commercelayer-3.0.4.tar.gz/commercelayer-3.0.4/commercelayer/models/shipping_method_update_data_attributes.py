from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_method_update_data_attributes_metadata import ShippingMethodUpdateDataAttributesMetadata


T = TypeVar("T", bound="ShippingMethodUpdateDataAttributes")


@attr.s(auto_attribs=True)
class ShippingMethodUpdateDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The shipping method's name Example: Standard shipping.
        scheme (Union[Unset, str]): The shipping method's scheme, one of 'flat' or 'weight_tiered'. Example: flat.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard.
            Example: EUR.
        disable (Union[Unset, bool]): Send this attribute if you want to mark the shipping method as disabled. Example:
            True.
        enable (Union[Unset, bool]): Send this attribute if you want to mark the shipping method as enabled. Example:
            True.
        price_amount_cents (Union[Unset, int]): The price of this shipping method, in cents. Example: 1000.
        free_over_amount_cents (Union[Unset, int]): Apply free shipping if the order amount is over this value, in
            cents. Example: 9900.
        min_weight (Union[Unset, float]): The minimum weight for which this shipping method is available. Example: 3.0.
        max_weight (Union[Unset, float]): The maximum weight for which this shipping method is available. Example:
            300.0.
        unit_of_weight (Union[Unset, str]): Can be one of 'gr', 'lb', or 'oz' Example: gr.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, ShippingMethodUpdateDataAttributesMetadata]): Set of key-value pairs that you can attach
            to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    name: Union[Unset, str] = UNSET
    scheme: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    disable: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    price_amount_cents: Union[Unset, int] = UNSET
    free_over_amount_cents: Union[Unset, int] = UNSET
    min_weight: Union[Unset, float] = UNSET
    max_weight: Union[Unset, float] = UNSET
    unit_of_weight: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ShippingMethodUpdateDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        scheme = self.scheme
        currency_code = self.currency_code
        disable = self.disable
        enable = self.enable
        price_amount_cents = self.price_amount_cents
        free_over_amount_cents = self.free_over_amount_cents
        min_weight = self.min_weight
        max_weight = self.max_weight
        unit_of_weight = self.unit_of_weight
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
        if disable is not UNSET:
            field_dict["_disable"] = disable
        if enable is not UNSET:
            field_dict["_enable"] = enable
        if price_amount_cents is not UNSET:
            field_dict["price_amount_cents"] = price_amount_cents
        if free_over_amount_cents is not UNSET:
            field_dict["free_over_amount_cents"] = free_over_amount_cents
        if min_weight is not UNSET:
            field_dict["min_weight"] = min_weight
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if unit_of_weight is not UNSET:
            field_dict["unit_of_weight"] = unit_of_weight
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_origin is not UNSET:
            field_dict["reference_origin"] = reference_origin
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_method_update_data_attributes_metadata import ShippingMethodUpdateDataAttributesMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        scheme = d.pop("scheme", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        disable = d.pop("_disable", UNSET)

        enable = d.pop("_enable", UNSET)

        price_amount_cents = d.pop("price_amount_cents", UNSET)

        free_over_amount_cents = d.pop("free_over_amount_cents", UNSET)

        min_weight = d.pop("min_weight", UNSET)

        max_weight = d.pop("max_weight", UNSET)

        unit_of_weight = d.pop("unit_of_weight", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ShippingMethodUpdateDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ShippingMethodUpdateDataAttributesMetadata.from_dict(_metadata)

        shipping_method_update_data_attributes = cls(
            name=name,
            scheme=scheme,
            currency_code=currency_code,
            disable=disable,
            enable=enable,
            price_amount_cents=price_amount_cents,
            free_over_amount_cents=free_over_amount_cents,
            min_weight=min_weight,
            max_weight=max_weight,
            unit_of_weight=unit_of_weight,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        shipping_method_update_data_attributes.additional_properties = d
        return shipping_method_update_data_attributes

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
