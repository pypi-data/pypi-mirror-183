from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_data_attributes_discount_breakdown import LineItemDataAttributesDiscountBreakdown
    from ..models.line_item_data_attributes_metadata import LineItemDataAttributesMetadata
    from ..models.line_item_data_attributes_tax_breakdown import LineItemDataAttributesTaxBreakdown


T = TypeVar("T", bound="LineItemDataAttributes")


@attr.s(auto_attribs=True)
class LineItemDataAttributes:
    """
    Attributes:
        sku_code (Union[Unset, str]): The code of the associated SKU. Example: TSHIRTMM000000FFFFFFXLXX.
        bundle_code (Union[Unset, str]): The code of the associated bundle. Example: BUNDLEMM000000FFFFFFXLXX.
        quantity (Union[Unset, int]): The line item quantity. Example: 4.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            automatically inherited from the order's market. Example: EUR.
        unit_amount_cents (Union[Unset, int]): The unit amount of the line item, in cents. Can be specified without an
            item, otherwise is automatically populated from the price list associated to the order's market. Example: 9900.
        unit_amount_float (Union[Unset, float]): The unit amount of the line item, float. This can be useful to track
            the purchase on thrid party systems, e.g Google Analyitcs Enhanced Ecommerce. Example: 99.0.
        formatted_unit_amount (Union[Unset, str]): The unit amount of the line item, formatted. This can be useful to
            display the amount with currency in you views. Example: €99,00.
        options_amount_cents (Union[Unset, int]): The options amount of the line item, in cents. Example: 990.
        options_amount_float (Union[Unset, float]): The options amount of the line item, float. Example: 9.9.
        formatted_options_amount (Union[Unset, str]): The options amount of the line item, formatted. Example: €9,90.
        discount_cents (Union[Unset, int]): The discount applied to the line item, in cents. When you apply a discount
            to an order, this is automatically calculated basing on the line item total_amount_cents value. Example: -900.
        discount_float (Union[Unset, float]): The discount applied to the line item, float. When you apply a discount to
            an order, this is automatically calculated basing on the line item total_amount_cents value. Example: 9.0.
        formatted_discount (Union[Unset, str]): The discount applied to the line item, fromatted. When you apply a
            discount to an order, this is automatically calculated basing on the line item total_amount_cents value.
            Example: €9,00.
        total_amount_cents (Union[Unset, int]): Calculated as unit amount x quantity + options amount, in cents.
            Example: 18800.
        total_amount_float (Union[Unset, float]): Calculated as unit amount x quantity + options amount, float. This can
            be useful to track the purchase on thrid party systems, e.g Google Analyitcs Enhanced Ecommerce. Example: 188.0.
        formatted_total_amount (Union[Unset, str]): Calculated as unit amount x quantity + options amount, formatted.
            This can be useful to display the amount with currency in you views. Example: €188,00.
        tax_amount_cents (Union[Unset, int]): The collected tax amount, otherwise calculated as total amount cents -
            discount cent * tax rate, in cents. Example: 1880.
        tax_amount_float (Union[Unset, float]): The collected tax amount, otherwise calculated as total amount cents -
            discount cent * tax rate, float. Example: 18.8.
        formatted_tax_amount (Union[Unset, str]): The collected tax amount, otherwise calculated as total amount cents -
            discount cent * tax rate, formatted. Example: €18,80.
        name (Union[Unset, str]): The name of the line item. When blank, it gets populated with the name of the
            associated item (if present). Example: Black Men T-shirt with White Logo (XL).
        image_url (Union[Unset, str]): The image_url of the line item. When blank, it gets populated with the image_url
            of the associated item (if present, SKU only). Example: https://img.yourdomain.com/skus/xYZkjABcde.png.
        discount_breakdown (Union[Unset, LineItemDataAttributesDiscountBreakdown]): The discount breakdown for this line
            item (if calculated). Example: {'41': {'cents': -900, 'weight': 0.416}}.
        tax_rate (Union[Unset, float]): The tax rate for this line item (if calculated). Example: 0.22.
        tax_breakdown (Union[Unset, LineItemDataAttributesTaxBreakdown]): The tax breakdown for this line item (if
            calculated). Example: {'id': '1234', 'city_amount': '0.0', 'state_amount': 6.6, 'city_tax_rate': 0.0,
            'county_amount': 2.78, 'taxable_amount': 139.0, 'county_tax_rate': 0.02, 'tax_collectable': 10.08,
            'special_tax_rate': 0.005, 'combined_tax_rate': 0.0725, 'city_taxable_amount': 0.0, 'state_sales_tax_rate':
            0.0475, 'state_taxable_amount': 139.0, 'county_taxable_amount': 139.0, 'special_district_amount': 0.7,
            'special_district_taxable_amount': 139.0}.
        item_type (Union[Unset, str]): The type of the associate item. Can be one of 'sku', 'bundle', 'shipment',
            'payment_method', 'adjustment', 'gift_card', or a valid promotion type. Example: sku.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, LineItemDataAttributesMetadata]): Set of key-value pairs that you can attach to the
            resource. This can be useful for storing additional information about the resource in a structured format.
            Example: {'foo': 'bar'}.
    """

    sku_code: Union[Unset, str] = UNSET
    bundle_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    currency_code: Union[Unset, str] = UNSET
    unit_amount_cents: Union[Unset, int] = UNSET
    unit_amount_float: Union[Unset, float] = UNSET
    formatted_unit_amount: Union[Unset, str] = UNSET
    options_amount_cents: Union[Unset, int] = UNSET
    options_amount_float: Union[Unset, float] = UNSET
    formatted_options_amount: Union[Unset, str] = UNSET
    discount_cents: Union[Unset, int] = UNSET
    discount_float: Union[Unset, float] = UNSET
    formatted_discount: Union[Unset, str] = UNSET
    total_amount_cents: Union[Unset, int] = UNSET
    total_amount_float: Union[Unset, float] = UNSET
    formatted_total_amount: Union[Unset, str] = UNSET
    tax_amount_cents: Union[Unset, int] = UNSET
    tax_amount_float: Union[Unset, float] = UNSET
    formatted_tax_amount: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    discount_breakdown: Union[Unset, "LineItemDataAttributesDiscountBreakdown"] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, "LineItemDataAttributesTaxBreakdown"] = UNSET
    item_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "LineItemDataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_code = self.sku_code
        bundle_code = self.bundle_code
        quantity = self.quantity
        currency_code = self.currency_code
        unit_amount_cents = self.unit_amount_cents
        unit_amount_float = self.unit_amount_float
        formatted_unit_amount = self.formatted_unit_amount
        options_amount_cents = self.options_amount_cents
        options_amount_float = self.options_amount_float
        formatted_options_amount = self.formatted_options_amount
        discount_cents = self.discount_cents
        discount_float = self.discount_float
        formatted_discount = self.formatted_discount
        total_amount_cents = self.total_amount_cents
        total_amount_float = self.total_amount_float
        formatted_total_amount = self.formatted_total_amount
        tax_amount_cents = self.tax_amount_cents
        tax_amount_float = self.tax_amount_float
        formatted_tax_amount = self.formatted_tax_amount
        name = self.name
        image_url = self.image_url
        discount_breakdown: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount_breakdown, Unset):
            discount_breakdown = self.discount_breakdown.to_dict()

        tax_rate = self.tax_rate
        tax_breakdown: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_breakdown, Unset):
            tax_breakdown = self.tax_breakdown.to_dict()

        item_type = self.item_type
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
        if sku_code is not UNSET:
            field_dict["sku_code"] = sku_code
        if bundle_code is not UNSET:
            field_dict["bundle_code"] = bundle_code
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
        if options_amount_cents is not UNSET:
            field_dict["options_amount_cents"] = options_amount_cents
        if options_amount_float is not UNSET:
            field_dict["options_amount_float"] = options_amount_float
        if formatted_options_amount is not UNSET:
            field_dict["formatted_options_amount"] = formatted_options_amount
        if discount_cents is not UNSET:
            field_dict["discount_cents"] = discount_cents
        if discount_float is not UNSET:
            field_dict["discount_float"] = discount_float
        if formatted_discount is not UNSET:
            field_dict["formatted_discount"] = formatted_discount
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if total_amount_float is not UNSET:
            field_dict["total_amount_float"] = total_amount_float
        if formatted_total_amount is not UNSET:
            field_dict["formatted_total_amount"] = formatted_total_amount
        if tax_amount_cents is not UNSET:
            field_dict["tax_amount_cents"] = tax_amount_cents
        if tax_amount_float is not UNSET:
            field_dict["tax_amount_float"] = tax_amount_float
        if formatted_tax_amount is not UNSET:
            field_dict["formatted_tax_amount"] = formatted_tax_amount
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if discount_breakdown is not UNSET:
            field_dict["discount_breakdown"] = discount_breakdown
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if tax_breakdown is not UNSET:
            field_dict["tax_breakdown"] = tax_breakdown
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
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
        from ..models.line_item_data_attributes_discount_breakdown import LineItemDataAttributesDiscountBreakdown
        from ..models.line_item_data_attributes_metadata import LineItemDataAttributesMetadata
        from ..models.line_item_data_attributes_tax_breakdown import LineItemDataAttributesTaxBreakdown

        d = src_dict.copy()
        sku_code = d.pop("sku_code", UNSET)

        bundle_code = d.pop("bundle_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        unit_amount_cents = d.pop("unit_amount_cents", UNSET)

        unit_amount_float = d.pop("unit_amount_float", UNSET)

        formatted_unit_amount = d.pop("formatted_unit_amount", UNSET)

        options_amount_cents = d.pop("options_amount_cents", UNSET)

        options_amount_float = d.pop("options_amount_float", UNSET)

        formatted_options_amount = d.pop("formatted_options_amount", UNSET)

        discount_cents = d.pop("discount_cents", UNSET)

        discount_float = d.pop("discount_float", UNSET)

        formatted_discount = d.pop("formatted_discount", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        total_amount_float = d.pop("total_amount_float", UNSET)

        formatted_total_amount = d.pop("formatted_total_amount", UNSET)

        tax_amount_cents = d.pop("tax_amount_cents", UNSET)

        tax_amount_float = d.pop("tax_amount_float", UNSET)

        formatted_tax_amount = d.pop("formatted_tax_amount", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("image_url", UNSET)

        _discount_breakdown = d.pop("discount_breakdown", UNSET)
        discount_breakdown: Union[Unset, LineItemDataAttributesDiscountBreakdown]
        if isinstance(_discount_breakdown, Unset):
            discount_breakdown = UNSET
        else:
            discount_breakdown = LineItemDataAttributesDiscountBreakdown.from_dict(_discount_breakdown)

        tax_rate = d.pop("tax_rate", UNSET)

        _tax_breakdown = d.pop("tax_breakdown", UNSET)
        tax_breakdown: Union[Unset, LineItemDataAttributesTaxBreakdown]
        if isinstance(_tax_breakdown, Unset):
            tax_breakdown = UNSET
        else:
            tax_breakdown = LineItemDataAttributesTaxBreakdown.from_dict(_tax_breakdown)

        item_type = d.pop("item_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, LineItemDataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LineItemDataAttributesMetadata.from_dict(_metadata)

        line_item_data_attributes = cls(
            sku_code=sku_code,
            bundle_code=bundle_code,
            quantity=quantity,
            currency_code=currency_code,
            unit_amount_cents=unit_amount_cents,
            unit_amount_float=unit_amount_float,
            formatted_unit_amount=formatted_unit_amount,
            options_amount_cents=options_amount_cents,
            options_amount_float=options_amount_float,
            formatted_options_amount=formatted_options_amount,
            discount_cents=discount_cents,
            discount_float=discount_float,
            formatted_discount=formatted_discount,
            total_amount_cents=total_amount_cents,
            total_amount_float=total_amount_float,
            formatted_total_amount=formatted_total_amount,
            tax_amount_cents=tax_amount_cents,
            tax_amount_float=tax_amount_float,
            formatted_tax_amount=formatted_tax_amount,
            name=name,
            image_url=image_url,
            discount_breakdown=discount_breakdown,
            tax_rate=tax_rate,
            tax_breakdown=tax_breakdown,
            item_type=item_type,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        line_item_data_attributes.additional_properties = d
        return line_item_data_attributes

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
