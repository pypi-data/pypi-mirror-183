from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tordersorder_id_response_200_data_attributes_metadata import (
        GETordersorderIdResponse200DataAttributesMetadata,
    )
    from ..models.ge_tordersorder_id_response_200_data_attributes_payment_source_details import (
        GETordersorderIdResponse200DataAttributesPaymentSourceDetails,
    )


T = TypeVar("T", bound="GETordersorderIdResponse200DataAttributes")


@attr.s(auto_attribs=True)
class GETordersorderIdResponse200DataAttributes:
    """
    Attributes:
        number (Union[Unset, int]): Unique identifier for the order (numeric). Example: 1234.
        autorefresh (Union[Unset, bool]): Save this attribute as 'false' if you want prevent the order to be refreshed
            automatically at each change (much faster). Example: True.
        status (Union[Unset, str]): The order status. One of 'draft' (default), 'pending', 'placed', 'approved', or
            'cancelled'. Example: draft.
        payment_status (Union[Unset, str]): The order's payment status. One of 'unpaid' (default), 'authorized', 'paid',
            'voided', or 'refunded'. Example: unpaid.
        fulfillment_status (Union[Unset, str]): The order's fulfillment status. One of 'unfulfilled' (default),
            'in_progress', or 'fulfilled'. Example: unfulfilled.
        guest (Union[Unset, bool]): Indicates if the order has been placed as guest. Example: True.
        editable (Union[Unset, bool]): Indicates if the order can be edited. Example: True.
        customer_email (Union[Unset, str]): The email address of the associated customer. When creating or updating an
            order, this is a shortcut to find or create the associated customer by email. Example: john@example.com.
        language_code (Union[Unset, str]): The preferred language code (ISO 639-1) to be used when communicating with
            the customer. This can be useful when sending the order to 3rd party marketing tools and CRMs. If the language
            is supported, the hosted checkout will be localized accordingly. Example: it.
        currency_code (Union[Unset, str]): The international 3-letter currency code as defined by the ISO 4217 standard,
            automatically inherited from the order's market. Example: EUR.
        tax_included (Union[Unset, bool]): Indicates if taxes are included in the order amounts, automatically inherited
            from the order's price list. Example: True.
        tax_rate (Union[Unset, float]): The tax rate for this order (if calculated). Example: 0.22.
        freight_taxable (Union[Unset, bool]): Indicates if taxes are applied to shipping costs. Example: True.
        requires_billing_info (Union[Unset, bool]): Indicates if the billing address associated to this order requires
            billing info to be present.
        country_code (Union[Unset, str]): The international 2-letter country code as defined by the ISO 3166-1 standard,
            automatically inherited from the order's shipping address. Example: IT.
        shipping_country_code_lock (Union[Unset, str]): The country code that you want the shipping address to be locked
            to. This can be useful to make sure the shipping address belongs to a given shipping country, e.g. the one
            selected in a country selector page. Example: IT.
        coupon_code (Union[Unset, str]): The coupon code to be used for the order. If valid, it triggers a promotion
            adding a discount line item to the order. Example: SUMMERDISCOUNT.
        gift_card_code (Union[Unset, str]): The gift card code (at least the first 8 characters) to be used for the
            order. If valid, it uses the gift card balance to pay for the order. Example:
            cc92c23e-967e-48b2-a323-59add603301f.
        gift_card_or_coupon_code (Union[Unset, str]): The gift card or coupon code (at least the first 8 characters) to
            be used for the order. If a gift card mathes, it uses the gift card balance to pay for the order. Otherwise it
            tries to find a valid coupon code and applies the associated discount. Example:
            cc92c23e-967e-48b2-a323-59add603301f.
        subtotal_amount_cents (Union[Unset, int]): The sum of all the SKU line items total amounts, in cents. Example:
            5000.
        subtotal_amount_float (Union[Unset, float]): The sum of all the SKU line items total amounts, float. Example:
            50.0.
        formatted_subtotal_amount (Union[Unset, str]): The sum of all the SKU line items total amounts, formatted.
            Example: €50,00.
        shipping_amount_cents (Union[Unset, int]): The sum of all the shipping costs, in cents. Example: 1200.
        shipping_amount_float (Union[Unset, float]): The sum of all the shipping costs, float. Example: 12.0.
        formatted_shipping_amount (Union[Unset, str]): The sum of all the shipping costs, formatted. Example: €12,00.
        payment_method_amount_cents (Union[Unset, int]): The payment method costs, in cents.
        payment_method_amount_float (Union[Unset, float]): The payment method costs, float.
        formatted_payment_method_amount (Union[Unset, str]): The payment method costs, formatted. Example: €0,00.
        discount_amount_cents (Union[Unset, int]): The sum of all the discounts applied to the order, in cents (negative
            amount). Example: -500.
        discount_amount_float (Union[Unset, float]): The sum of all the discounts applied to the order, float. Example:
            -5.0.
        formatted_discount_amount (Union[Unset, str]): The sum of all the discounts applied to the order, formatted.
            Example: -€5,00.
        adjustment_amount_cents (Union[Unset, int]): The sum of all the adjustments applied to the order, in cents.
            Example: 1500.
        adjustment_amount_float (Union[Unset, float]): The sum of all the adjustments applied to the order, float.
            Example: 15.0.
        formatted_adjustment_amount (Union[Unset, str]): The sum of all the adjustments applied to the order, formatted.
            Example: €15,00.
        gift_card_amount_cents (Union[Unset, int]): The sum of all the gift_cards applied to the order, in cents.
            Example: 1500.
        gift_card_amount_float (Union[Unset, float]): The sum of all the gift_cards applied to the order, float.
            Example: 15.0.
        formatted_gift_card_amount (Union[Unset, str]): The sum of all the gift_cards applied to the order, formatted.
            Example: €15,00.
        total_tax_amount_cents (Union[Unset, int]): The sum of all the taxes applied to the order, in cents. Example:
            1028.
        total_tax_amount_float (Union[Unset, float]): The sum of all the taxes applied to the order, float. Example:
            10.28.
        formatted_total_tax_amount (Union[Unset, str]): The sum of all the taxes applied to the order, formatted.
            Example: €10,28.
        subtotal_tax_amount_cents (Union[Unset, int]): The taxes applied to the order's subtotal, in cents. Example:
            902.
        subtotal_tax_amount_float (Union[Unset, float]): The taxes applied to the order's subtotal, float. Example:
            9.02.
        formatted_subtotal_tax_amount (Union[Unset, str]): The taxes applied to the order's subtotal, formatted.
            Example: €9,02.
        shipping_tax_amount_cents (Union[Unset, int]): The taxes applied to the order's shipping costs, in cents.
            Example: 216.
        shipping_tax_amount_float (Union[Unset, float]): The taxes applied to the order's shipping costs, float.
            Example: 2.16.
        formatted_shipping_tax_amount (Union[Unset, str]): The taxes applied to the order's shipping costs, formatted.
            Example: €2,16.
        payment_method_tax_amount_cents (Union[Unset, int]): The taxes applied to the order's payment method costs, in
            cents.
        payment_method_tax_amount_float (Union[Unset, float]): The taxes applied to the order's payment method costs,
            float.
        formatted_payment_method_tax_amount (Union[Unset, str]): The taxes applied to the order's payment method costs,
            formatted. Example: €0,00.
        adjustment_tax_amount_cents (Union[Unset, int]): The taxes applied to the order adjustments, in cents. Example:
            900.
        adjustment_tax_amount_float (Union[Unset, float]): The taxes applied to the order adjustments, float. Example:
            9.0.
        formatted_adjustment_tax_amount (Union[Unset, str]): The taxes applied to the order adjustments, formatted.
            Example: €9,00.
        total_amount_cents (Union[Unset, int]): The order's total amount, in cents. Example: 5700.
        total_amount_float (Union[Unset, float]): The order's total amount, float. Example: 57.0.
        formatted_total_amount (Union[Unset, str]): The order's total amount, formatted. Example: €57,00.
        total_taxable_amount_cents (Union[Unset, int]): The order's total taxable amount, in cents (without discounts).
            Example: 4672.
        total_taxable_amount_float (Union[Unset, float]): The order's total taxable amount, float. Example: 46.72.
        formatted_total_taxable_amount (Union[Unset, str]): The order's total taxable amount, formatted. Example:
            €46,72.
        subtotal_taxable_amount_cents (Union[Unset, int]): The order's subtotal taxable amount, in cents (equal to
            subtotal_amount_cents when prices don't include taxes). Example: 4098.
        subtotal_taxable_amount_float (Union[Unset, float]): The order's subtotal taxable amount, float. Example: 40.98.
        formatted_subtotal_taxable_amount (Union[Unset, str]): The order's subtotal taxable amount, formatted. Example:
            €40,98.
        shipping_taxable_amount_cents (Union[Unset, int]): The order's shipping taxable amount, in cents (equal to
            shipping_amount_cents when prices don't include taxes). Example: 984.
        shipping_taxable_amount_float (Union[Unset, float]): The order's shipping taxable amount, float. Example: 9.84.
        formatted_shipping_taxable_amount (Union[Unset, str]): The order's shipping taxable amount, formatted. Example:
            €9,84.
        payment_method_taxable_amount_cents (Union[Unset, int]): The order's payment method taxable amount, in cents
            (equal to payment_method_amount_cents when prices don't include taxes).
        payment_method_taxable_amount_float (Union[Unset, float]): The order's payment method taxable amount, float.
        formatted_payment_method_taxable_amount (Union[Unset, str]): The order's payment method taxable amount,
            formatted. Example: €0,00.
        adjustment_taxable_amount_cents (Union[Unset, int]): The order's adjustment taxable amount, in cents (equal to
            discount_adjustment_cents when prices don't include taxes). Example: 120.
        adjustment_taxable_amount_float (Union[Unset, float]): The order's adjustment taxable amount, float. Example:
            1.2.
        formatted_adjustment_taxable_amount (Union[Unset, str]): The order's adjustment taxable amount, formatted.
            Example: €1,20.
        total_amount_with_taxes_cents (Union[Unset, int]): The order's total amount (when prices include taxes) or the
            order's total + taxes amount (when prices don't include taxes, e.g. US Markets or B2B). Example: 5700.
        total_amount_with_taxes_float (Union[Unset, float]): The order's total amount with taxes, float. Example: 57.0.
        formatted_total_amount_with_taxes (Union[Unset, str]): The order's total amount with taxes, formatted. Example:
            €57,00.
        fees_amount_cents (Union[Unset, int]): The fees amount that is applied by Commerce Layer, in cents.
        fees_amount_float (Union[Unset, float]): The fees amount that is applied by Commerce Layer, float.
        formatted_fees_amount (Union[Unset, str]): The fees amount that is applied by Commerce Layer, formatted.
            Example: €0,00.
        duty_amount_cents (Union[Unset, int]): The duty amount that is calculated by external services, in cents.
        duty_amount_float (Union[Unset, float]): The duty amount that is calculated by external services, float.
        formatted_duty_amount (Union[Unset, str]): The duty amount that is calculated by external services, formatted.
            Example: €0,00.
        skus_count (Union[Unset, int]): The total number of SKUs in the order's line items. This can be useful to
            display a preview of the customer shopping cart content. Example: 2.
        line_item_options_count (Union[Unset, int]): The total number of line item options. This can be useful to
            display a preview of the customer shopping cart content. Example: 1.
        shipments_count (Union[Unset, int]): The total number of shipments. This can be useful to manage the shipping
            method(s) selection during checkout. Example: 1.
        tax_calculations_count (Union[Unset, int]): The total number of tax calculations. This can be useful to monitor
            external tax service usage. Example: 1.
        payment_source_details (Union[Unset, GETordersorderIdResponse200DataAttributesPaymentSourceDetails]): An object
            that contains the shareable details of the order's payment source. Example: {'foo': 'bar'}.
        token (Union[Unset, str]): A unique token that can be shared more securely instead of the order's id. Example:
            1c0994cc4e996e8c6ee56a2198f66f3c.
        cart_url (Union[Unset, str]): The cart url on your site. If present, it will be used on our hosted checkout
            application. Example: https://yourdomain.com/cart.
        return_url (Union[Unset, str]): The return url on your site. If present, it will be used on our hosted checkout
            application. Example: https://yourdomain.com/.
        terms_url (Union[Unset, str]): The terms and conditions url on your site. If present, it will be used on our
            hosted checkout application. Example: https://yourdomain.com/terms.
        privacy_url (Union[Unset, str]): The privacy policy url on your site. If present, it will be used on our hosted
            checkout application. Example: https://yourdomain.com/privacy.
        checkout_url (Union[Unset, str]): The checkout url that was automatically generated for the order. Send the
            customers to this url to let them checkout the order securely on our hosted checkout application. Example:
            https://yourdomain.commercelayer.io/checkout/1c0994cc4e996e8c6ee56a2198f66f3c.
        placed_at (Union[Unset, str]): Time at which the order was placed. Example: 2018-01-01T12:00:00.000Z.
        approved_at (Union[Unset, str]): Time at which the order was approved. Example: 2018-01-01T12:00:00.000Z.
        cancelled_at (Union[Unset, str]): Time at which the order was cancelled. Example: 2018-01-01T12:00:00.000Z.
        payment_updated_at (Union[Unset, str]): Time at which the order's payment status was last updated. Example:
            2018-01-01T12:00:00.000Z.
        fulfillment_updated_at (Union[Unset, str]): Time at which the order's fulfillment status was last updated.
            Example: 2018-01-01T12:00:00.000Z.
        refreshed_at (Union[Unset, str]): Last time at which an order was manually refreshed. Example:
            2018-01-01T12:00:00.000Z.
        archived_at (Union[Unset, str]): Time at which the resource has been archived. Example:
            2018-01-01T12:00:00.000Z.
        expires_at (Union[Unset, str]): Time at which an order is marked for cleanup. Any order will start with a
            default expire time of 2 months. Expiration is reset once a line item is added to the order. Example:
            2018-01-01T12:00:00.000Z.
        created_at (Union[Unset, str]): Time at which the resource was created. Example: 2018-01-01T12:00:00.000Z.
        updated_at (Union[Unset, str]): Time at which the resource was last updated. Example: 2018-01-01T12:00:00.000Z.
        reference (Union[Unset, str]): A string that you can use to add any external identifier to the resource. This
            can be useful for integrating the resource to an external system, like an ERP, a marketing tool, a CRM, or
            whatever. Example: ANY-EXTERNAL-REFEFERNCE.
        reference_origin (Union[Unset, str]): Any identifier of the third party system that defines the reference code
            Example: ANY-EXTERNAL-REFEFERNCE-ORIGIN.
        metadata (Union[Unset, GETordersorderIdResponse200DataAttributesMetadata]): Set of key-value pairs that you can
            attach to the resource. This can be useful for storing additional information about the resource in a structured
            format. Example: {'foo': 'bar'}.
    """

    number: Union[Unset, int] = UNSET
    autorefresh: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    payment_status: Union[Unset, str] = UNSET
    fulfillment_status: Union[Unset, str] = UNSET
    guest: Union[Unset, bool] = UNSET
    editable: Union[Unset, bool] = UNSET
    customer_email: Union[Unset, str] = UNSET
    language_code: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    tax_included: Union[Unset, bool] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    freight_taxable: Union[Unset, bool] = UNSET
    requires_billing_info: Union[Unset, bool] = UNSET
    country_code: Union[Unset, str] = UNSET
    shipping_country_code_lock: Union[Unset, str] = UNSET
    coupon_code: Union[Unset, str] = UNSET
    gift_card_code: Union[Unset, str] = UNSET
    gift_card_or_coupon_code: Union[Unset, str] = UNSET
    subtotal_amount_cents: Union[Unset, int] = UNSET
    subtotal_amount_float: Union[Unset, float] = UNSET
    formatted_subtotal_amount: Union[Unset, str] = UNSET
    shipping_amount_cents: Union[Unset, int] = UNSET
    shipping_amount_float: Union[Unset, float] = UNSET
    formatted_shipping_amount: Union[Unset, str] = UNSET
    payment_method_amount_cents: Union[Unset, int] = UNSET
    payment_method_amount_float: Union[Unset, float] = UNSET
    formatted_payment_method_amount: Union[Unset, str] = UNSET
    discount_amount_cents: Union[Unset, int] = UNSET
    discount_amount_float: Union[Unset, float] = UNSET
    formatted_discount_amount: Union[Unset, str] = UNSET
    adjustment_amount_cents: Union[Unset, int] = UNSET
    adjustment_amount_float: Union[Unset, float] = UNSET
    formatted_adjustment_amount: Union[Unset, str] = UNSET
    gift_card_amount_cents: Union[Unset, int] = UNSET
    gift_card_amount_float: Union[Unset, float] = UNSET
    formatted_gift_card_amount: Union[Unset, str] = UNSET
    total_tax_amount_cents: Union[Unset, int] = UNSET
    total_tax_amount_float: Union[Unset, float] = UNSET
    formatted_total_tax_amount: Union[Unset, str] = UNSET
    subtotal_tax_amount_cents: Union[Unset, int] = UNSET
    subtotal_tax_amount_float: Union[Unset, float] = UNSET
    formatted_subtotal_tax_amount: Union[Unset, str] = UNSET
    shipping_tax_amount_cents: Union[Unset, int] = UNSET
    shipping_tax_amount_float: Union[Unset, float] = UNSET
    formatted_shipping_tax_amount: Union[Unset, str] = UNSET
    payment_method_tax_amount_cents: Union[Unset, int] = UNSET
    payment_method_tax_amount_float: Union[Unset, float] = UNSET
    formatted_payment_method_tax_amount: Union[Unset, str] = UNSET
    adjustment_tax_amount_cents: Union[Unset, int] = UNSET
    adjustment_tax_amount_float: Union[Unset, float] = UNSET
    formatted_adjustment_tax_amount: Union[Unset, str] = UNSET
    total_amount_cents: Union[Unset, int] = UNSET
    total_amount_float: Union[Unset, float] = UNSET
    formatted_total_amount: Union[Unset, str] = UNSET
    total_taxable_amount_cents: Union[Unset, int] = UNSET
    total_taxable_amount_float: Union[Unset, float] = UNSET
    formatted_total_taxable_amount: Union[Unset, str] = UNSET
    subtotal_taxable_amount_cents: Union[Unset, int] = UNSET
    subtotal_taxable_amount_float: Union[Unset, float] = UNSET
    formatted_subtotal_taxable_amount: Union[Unset, str] = UNSET
    shipping_taxable_amount_cents: Union[Unset, int] = UNSET
    shipping_taxable_amount_float: Union[Unset, float] = UNSET
    formatted_shipping_taxable_amount: Union[Unset, str] = UNSET
    payment_method_taxable_amount_cents: Union[Unset, int] = UNSET
    payment_method_taxable_amount_float: Union[Unset, float] = UNSET
    formatted_payment_method_taxable_amount: Union[Unset, str] = UNSET
    adjustment_taxable_amount_cents: Union[Unset, int] = UNSET
    adjustment_taxable_amount_float: Union[Unset, float] = UNSET
    formatted_adjustment_taxable_amount: Union[Unset, str] = UNSET
    total_amount_with_taxes_cents: Union[Unset, int] = UNSET
    total_amount_with_taxes_float: Union[Unset, float] = UNSET
    formatted_total_amount_with_taxes: Union[Unset, str] = UNSET
    fees_amount_cents: Union[Unset, int] = UNSET
    fees_amount_float: Union[Unset, float] = UNSET
    formatted_fees_amount: Union[Unset, str] = UNSET
    duty_amount_cents: Union[Unset, int] = UNSET
    duty_amount_float: Union[Unset, float] = UNSET
    formatted_duty_amount: Union[Unset, str] = UNSET
    skus_count: Union[Unset, int] = UNSET
    line_item_options_count: Union[Unset, int] = UNSET
    shipments_count: Union[Unset, int] = UNSET
    tax_calculations_count: Union[Unset, int] = UNSET
    payment_source_details: Union[Unset, "GETordersorderIdResponse200DataAttributesPaymentSourceDetails"] = UNSET
    token: Union[Unset, str] = UNSET
    cart_url: Union[Unset, str] = UNSET
    return_url: Union[Unset, str] = UNSET
    terms_url: Union[Unset, str] = UNSET
    privacy_url: Union[Unset, str] = UNSET
    checkout_url: Union[Unset, str] = UNSET
    placed_at: Union[Unset, str] = UNSET
    approved_at: Union[Unset, str] = UNSET
    cancelled_at: Union[Unset, str] = UNSET
    payment_updated_at: Union[Unset, str] = UNSET
    fulfillment_updated_at: Union[Unset, str] = UNSET
    refreshed_at: Union[Unset, str] = UNSET
    archived_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reference_origin: Union[Unset, str] = UNSET
    metadata: Union[Unset, "GETordersorderIdResponse200DataAttributesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        autorefresh = self.autorefresh
        status = self.status
        payment_status = self.payment_status
        fulfillment_status = self.fulfillment_status
        guest = self.guest
        editable = self.editable
        customer_email = self.customer_email
        language_code = self.language_code
        currency_code = self.currency_code
        tax_included = self.tax_included
        tax_rate = self.tax_rate
        freight_taxable = self.freight_taxable
        requires_billing_info = self.requires_billing_info
        country_code = self.country_code
        shipping_country_code_lock = self.shipping_country_code_lock
        coupon_code = self.coupon_code
        gift_card_code = self.gift_card_code
        gift_card_or_coupon_code = self.gift_card_or_coupon_code
        subtotal_amount_cents = self.subtotal_amount_cents
        subtotal_amount_float = self.subtotal_amount_float
        formatted_subtotal_amount = self.formatted_subtotal_amount
        shipping_amount_cents = self.shipping_amount_cents
        shipping_amount_float = self.shipping_amount_float
        formatted_shipping_amount = self.formatted_shipping_amount
        payment_method_amount_cents = self.payment_method_amount_cents
        payment_method_amount_float = self.payment_method_amount_float
        formatted_payment_method_amount = self.formatted_payment_method_amount
        discount_amount_cents = self.discount_amount_cents
        discount_amount_float = self.discount_amount_float
        formatted_discount_amount = self.formatted_discount_amount
        adjustment_amount_cents = self.adjustment_amount_cents
        adjustment_amount_float = self.adjustment_amount_float
        formatted_adjustment_amount = self.formatted_adjustment_amount
        gift_card_amount_cents = self.gift_card_amount_cents
        gift_card_amount_float = self.gift_card_amount_float
        formatted_gift_card_amount = self.formatted_gift_card_amount
        total_tax_amount_cents = self.total_tax_amount_cents
        total_tax_amount_float = self.total_tax_amount_float
        formatted_total_tax_amount = self.formatted_total_tax_amount
        subtotal_tax_amount_cents = self.subtotal_tax_amount_cents
        subtotal_tax_amount_float = self.subtotal_tax_amount_float
        formatted_subtotal_tax_amount = self.formatted_subtotal_tax_amount
        shipping_tax_amount_cents = self.shipping_tax_amount_cents
        shipping_tax_amount_float = self.shipping_tax_amount_float
        formatted_shipping_tax_amount = self.formatted_shipping_tax_amount
        payment_method_tax_amount_cents = self.payment_method_tax_amount_cents
        payment_method_tax_amount_float = self.payment_method_tax_amount_float
        formatted_payment_method_tax_amount = self.formatted_payment_method_tax_amount
        adjustment_tax_amount_cents = self.adjustment_tax_amount_cents
        adjustment_tax_amount_float = self.adjustment_tax_amount_float
        formatted_adjustment_tax_amount = self.formatted_adjustment_tax_amount
        total_amount_cents = self.total_amount_cents
        total_amount_float = self.total_amount_float
        formatted_total_amount = self.formatted_total_amount
        total_taxable_amount_cents = self.total_taxable_amount_cents
        total_taxable_amount_float = self.total_taxable_amount_float
        formatted_total_taxable_amount = self.formatted_total_taxable_amount
        subtotal_taxable_amount_cents = self.subtotal_taxable_amount_cents
        subtotal_taxable_amount_float = self.subtotal_taxable_amount_float
        formatted_subtotal_taxable_amount = self.formatted_subtotal_taxable_amount
        shipping_taxable_amount_cents = self.shipping_taxable_amount_cents
        shipping_taxable_amount_float = self.shipping_taxable_amount_float
        formatted_shipping_taxable_amount = self.formatted_shipping_taxable_amount
        payment_method_taxable_amount_cents = self.payment_method_taxable_amount_cents
        payment_method_taxable_amount_float = self.payment_method_taxable_amount_float
        formatted_payment_method_taxable_amount = self.formatted_payment_method_taxable_amount
        adjustment_taxable_amount_cents = self.adjustment_taxable_amount_cents
        adjustment_taxable_amount_float = self.adjustment_taxable_amount_float
        formatted_adjustment_taxable_amount = self.formatted_adjustment_taxable_amount
        total_amount_with_taxes_cents = self.total_amount_with_taxes_cents
        total_amount_with_taxes_float = self.total_amount_with_taxes_float
        formatted_total_amount_with_taxes = self.formatted_total_amount_with_taxes
        fees_amount_cents = self.fees_amount_cents
        fees_amount_float = self.fees_amount_float
        formatted_fees_amount = self.formatted_fees_amount
        duty_amount_cents = self.duty_amount_cents
        duty_amount_float = self.duty_amount_float
        formatted_duty_amount = self.formatted_duty_amount
        skus_count = self.skus_count
        line_item_options_count = self.line_item_options_count
        shipments_count = self.shipments_count
        tax_calculations_count = self.tax_calculations_count
        payment_source_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_source_details, Unset):
            payment_source_details = self.payment_source_details.to_dict()

        token = self.token
        cart_url = self.cart_url
        return_url = self.return_url
        terms_url = self.terms_url
        privacy_url = self.privacy_url
        checkout_url = self.checkout_url
        placed_at = self.placed_at
        approved_at = self.approved_at
        cancelled_at = self.cancelled_at
        payment_updated_at = self.payment_updated_at
        fulfillment_updated_at = self.fulfillment_updated_at
        refreshed_at = self.refreshed_at
        archived_at = self.archived_at
        expires_at = self.expires_at
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
        if number is not UNSET:
            field_dict["number"] = number
        if autorefresh is not UNSET:
            field_dict["autorefresh"] = autorefresh
        if status is not UNSET:
            field_dict["status"] = status
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if fulfillment_status is not UNSET:
            field_dict["fulfillment_status"] = fulfillment_status
        if guest is not UNSET:
            field_dict["guest"] = guest
        if editable is not UNSET:
            field_dict["editable"] = editable
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if tax_included is not UNSET:
            field_dict["tax_included"] = tax_included
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if freight_taxable is not UNSET:
            field_dict["freight_taxable"] = freight_taxable
        if requires_billing_info is not UNSET:
            field_dict["requires_billing_info"] = requires_billing_info
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if shipping_country_code_lock is not UNSET:
            field_dict["shipping_country_code_lock"] = shipping_country_code_lock
        if coupon_code is not UNSET:
            field_dict["coupon_code"] = coupon_code
        if gift_card_code is not UNSET:
            field_dict["gift_card_code"] = gift_card_code
        if gift_card_or_coupon_code is not UNSET:
            field_dict["gift_card_or_coupon_code"] = gift_card_or_coupon_code
        if subtotal_amount_cents is not UNSET:
            field_dict["subtotal_amount_cents"] = subtotal_amount_cents
        if subtotal_amount_float is not UNSET:
            field_dict["subtotal_amount_float"] = subtotal_amount_float
        if formatted_subtotal_amount is not UNSET:
            field_dict["formatted_subtotal_amount"] = formatted_subtotal_amount
        if shipping_amount_cents is not UNSET:
            field_dict["shipping_amount_cents"] = shipping_amount_cents
        if shipping_amount_float is not UNSET:
            field_dict["shipping_amount_float"] = shipping_amount_float
        if formatted_shipping_amount is not UNSET:
            field_dict["formatted_shipping_amount"] = formatted_shipping_amount
        if payment_method_amount_cents is not UNSET:
            field_dict["payment_method_amount_cents"] = payment_method_amount_cents
        if payment_method_amount_float is not UNSET:
            field_dict["payment_method_amount_float"] = payment_method_amount_float
        if formatted_payment_method_amount is not UNSET:
            field_dict["formatted_payment_method_amount"] = formatted_payment_method_amount
        if discount_amount_cents is not UNSET:
            field_dict["discount_amount_cents"] = discount_amount_cents
        if discount_amount_float is not UNSET:
            field_dict["discount_amount_float"] = discount_amount_float
        if formatted_discount_amount is not UNSET:
            field_dict["formatted_discount_amount"] = formatted_discount_amount
        if adjustment_amount_cents is not UNSET:
            field_dict["adjustment_amount_cents"] = adjustment_amount_cents
        if adjustment_amount_float is not UNSET:
            field_dict["adjustment_amount_float"] = adjustment_amount_float
        if formatted_adjustment_amount is not UNSET:
            field_dict["formatted_adjustment_amount"] = formatted_adjustment_amount
        if gift_card_amount_cents is not UNSET:
            field_dict["gift_card_amount_cents"] = gift_card_amount_cents
        if gift_card_amount_float is not UNSET:
            field_dict["gift_card_amount_float"] = gift_card_amount_float
        if formatted_gift_card_amount is not UNSET:
            field_dict["formatted_gift_card_amount"] = formatted_gift_card_amount
        if total_tax_amount_cents is not UNSET:
            field_dict["total_tax_amount_cents"] = total_tax_amount_cents
        if total_tax_amount_float is not UNSET:
            field_dict["total_tax_amount_float"] = total_tax_amount_float
        if formatted_total_tax_amount is not UNSET:
            field_dict["formatted_total_tax_amount"] = formatted_total_tax_amount
        if subtotal_tax_amount_cents is not UNSET:
            field_dict["subtotal_tax_amount_cents"] = subtotal_tax_amount_cents
        if subtotal_tax_amount_float is not UNSET:
            field_dict["subtotal_tax_amount_float"] = subtotal_tax_amount_float
        if formatted_subtotal_tax_amount is not UNSET:
            field_dict["formatted_subtotal_tax_amount"] = formatted_subtotal_tax_amount
        if shipping_tax_amount_cents is not UNSET:
            field_dict["shipping_tax_amount_cents"] = shipping_tax_amount_cents
        if shipping_tax_amount_float is not UNSET:
            field_dict["shipping_tax_amount_float"] = shipping_tax_amount_float
        if formatted_shipping_tax_amount is not UNSET:
            field_dict["formatted_shipping_tax_amount"] = formatted_shipping_tax_amount
        if payment_method_tax_amount_cents is not UNSET:
            field_dict["payment_method_tax_amount_cents"] = payment_method_tax_amount_cents
        if payment_method_tax_amount_float is not UNSET:
            field_dict["payment_method_tax_amount_float"] = payment_method_tax_amount_float
        if formatted_payment_method_tax_amount is not UNSET:
            field_dict["formatted_payment_method_tax_amount"] = formatted_payment_method_tax_amount
        if adjustment_tax_amount_cents is not UNSET:
            field_dict["adjustment_tax_amount_cents"] = adjustment_tax_amount_cents
        if adjustment_tax_amount_float is not UNSET:
            field_dict["adjustment_tax_amount_float"] = adjustment_tax_amount_float
        if formatted_adjustment_tax_amount is not UNSET:
            field_dict["formatted_adjustment_tax_amount"] = formatted_adjustment_tax_amount
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if total_amount_float is not UNSET:
            field_dict["total_amount_float"] = total_amount_float
        if formatted_total_amount is not UNSET:
            field_dict["formatted_total_amount"] = formatted_total_amount
        if total_taxable_amount_cents is not UNSET:
            field_dict["total_taxable_amount_cents"] = total_taxable_amount_cents
        if total_taxable_amount_float is not UNSET:
            field_dict["total_taxable_amount_float"] = total_taxable_amount_float
        if formatted_total_taxable_amount is not UNSET:
            field_dict["formatted_total_taxable_amount"] = formatted_total_taxable_amount
        if subtotal_taxable_amount_cents is not UNSET:
            field_dict["subtotal_taxable_amount_cents"] = subtotal_taxable_amount_cents
        if subtotal_taxable_amount_float is not UNSET:
            field_dict["subtotal_taxable_amount_float"] = subtotal_taxable_amount_float
        if formatted_subtotal_taxable_amount is not UNSET:
            field_dict["formatted_subtotal_taxable_amount"] = formatted_subtotal_taxable_amount
        if shipping_taxable_amount_cents is not UNSET:
            field_dict["shipping_taxable_amount_cents"] = shipping_taxable_amount_cents
        if shipping_taxable_amount_float is not UNSET:
            field_dict["shipping_taxable_amount_float"] = shipping_taxable_amount_float
        if formatted_shipping_taxable_amount is not UNSET:
            field_dict["formatted_shipping_taxable_amount"] = formatted_shipping_taxable_amount
        if payment_method_taxable_amount_cents is not UNSET:
            field_dict["payment_method_taxable_amount_cents"] = payment_method_taxable_amount_cents
        if payment_method_taxable_amount_float is not UNSET:
            field_dict["payment_method_taxable_amount_float"] = payment_method_taxable_amount_float
        if formatted_payment_method_taxable_amount is not UNSET:
            field_dict["formatted_payment_method_taxable_amount"] = formatted_payment_method_taxable_amount
        if adjustment_taxable_amount_cents is not UNSET:
            field_dict["adjustment_taxable_amount_cents"] = adjustment_taxable_amount_cents
        if adjustment_taxable_amount_float is not UNSET:
            field_dict["adjustment_taxable_amount_float"] = adjustment_taxable_amount_float
        if formatted_adjustment_taxable_amount is not UNSET:
            field_dict["formatted_adjustment_taxable_amount"] = formatted_adjustment_taxable_amount
        if total_amount_with_taxes_cents is not UNSET:
            field_dict["total_amount_with_taxes_cents"] = total_amount_with_taxes_cents
        if total_amount_with_taxes_float is not UNSET:
            field_dict["total_amount_with_taxes_float"] = total_amount_with_taxes_float
        if formatted_total_amount_with_taxes is not UNSET:
            field_dict["formatted_total_amount_with_taxes"] = formatted_total_amount_with_taxes
        if fees_amount_cents is not UNSET:
            field_dict["fees_amount_cents"] = fees_amount_cents
        if fees_amount_float is not UNSET:
            field_dict["fees_amount_float"] = fees_amount_float
        if formatted_fees_amount is not UNSET:
            field_dict["formatted_fees_amount"] = formatted_fees_amount
        if duty_amount_cents is not UNSET:
            field_dict["duty_amount_cents"] = duty_amount_cents
        if duty_amount_float is not UNSET:
            field_dict["duty_amount_float"] = duty_amount_float
        if formatted_duty_amount is not UNSET:
            field_dict["formatted_duty_amount"] = formatted_duty_amount
        if skus_count is not UNSET:
            field_dict["skus_count"] = skus_count
        if line_item_options_count is not UNSET:
            field_dict["line_item_options_count"] = line_item_options_count
        if shipments_count is not UNSET:
            field_dict["shipments_count"] = shipments_count
        if tax_calculations_count is not UNSET:
            field_dict["tax_calculations_count"] = tax_calculations_count
        if payment_source_details is not UNSET:
            field_dict["payment_source_details"] = payment_source_details
        if token is not UNSET:
            field_dict["token"] = token
        if cart_url is not UNSET:
            field_dict["cart_url"] = cart_url
        if return_url is not UNSET:
            field_dict["return_url"] = return_url
        if terms_url is not UNSET:
            field_dict["terms_url"] = terms_url
        if privacy_url is not UNSET:
            field_dict["privacy_url"] = privacy_url
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if placed_at is not UNSET:
            field_dict["placed_at"] = placed_at
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if payment_updated_at is not UNSET:
            field_dict["payment_updated_at"] = payment_updated_at
        if fulfillment_updated_at is not UNSET:
            field_dict["fulfillment_updated_at"] = fulfillment_updated_at
        if refreshed_at is not UNSET:
            field_dict["refreshed_at"] = refreshed_at
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
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
        from ..models.ge_tordersorder_id_response_200_data_attributes_metadata import (
            GETordersorderIdResponse200DataAttributesMetadata,
        )
        from ..models.ge_tordersorder_id_response_200_data_attributes_payment_source_details import (
            GETordersorderIdResponse200DataAttributesPaymentSourceDetails,
        )

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        autorefresh = d.pop("autorefresh", UNSET)

        status = d.pop("status", UNSET)

        payment_status = d.pop("payment_status", UNSET)

        fulfillment_status = d.pop("fulfillment_status", UNSET)

        guest = d.pop("guest", UNSET)

        editable = d.pop("editable", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        language_code = d.pop("language_code", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        tax_included = d.pop("tax_included", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        freight_taxable = d.pop("freight_taxable", UNSET)

        requires_billing_info = d.pop("requires_billing_info", UNSET)

        country_code = d.pop("country_code", UNSET)

        shipping_country_code_lock = d.pop("shipping_country_code_lock", UNSET)

        coupon_code = d.pop("coupon_code", UNSET)

        gift_card_code = d.pop("gift_card_code", UNSET)

        gift_card_or_coupon_code = d.pop("gift_card_or_coupon_code", UNSET)

        subtotal_amount_cents = d.pop("subtotal_amount_cents", UNSET)

        subtotal_amount_float = d.pop("subtotal_amount_float", UNSET)

        formatted_subtotal_amount = d.pop("formatted_subtotal_amount", UNSET)

        shipping_amount_cents = d.pop("shipping_amount_cents", UNSET)

        shipping_amount_float = d.pop("shipping_amount_float", UNSET)

        formatted_shipping_amount = d.pop("formatted_shipping_amount", UNSET)

        payment_method_amount_cents = d.pop("payment_method_amount_cents", UNSET)

        payment_method_amount_float = d.pop("payment_method_amount_float", UNSET)

        formatted_payment_method_amount = d.pop("formatted_payment_method_amount", UNSET)

        discount_amount_cents = d.pop("discount_amount_cents", UNSET)

        discount_amount_float = d.pop("discount_amount_float", UNSET)

        formatted_discount_amount = d.pop("formatted_discount_amount", UNSET)

        adjustment_amount_cents = d.pop("adjustment_amount_cents", UNSET)

        adjustment_amount_float = d.pop("adjustment_amount_float", UNSET)

        formatted_adjustment_amount = d.pop("formatted_adjustment_amount", UNSET)

        gift_card_amount_cents = d.pop("gift_card_amount_cents", UNSET)

        gift_card_amount_float = d.pop("gift_card_amount_float", UNSET)

        formatted_gift_card_amount = d.pop("formatted_gift_card_amount", UNSET)

        total_tax_amount_cents = d.pop("total_tax_amount_cents", UNSET)

        total_tax_amount_float = d.pop("total_tax_amount_float", UNSET)

        formatted_total_tax_amount = d.pop("formatted_total_tax_amount", UNSET)

        subtotal_tax_amount_cents = d.pop("subtotal_tax_amount_cents", UNSET)

        subtotal_tax_amount_float = d.pop("subtotal_tax_amount_float", UNSET)

        formatted_subtotal_tax_amount = d.pop("formatted_subtotal_tax_amount", UNSET)

        shipping_tax_amount_cents = d.pop("shipping_tax_amount_cents", UNSET)

        shipping_tax_amount_float = d.pop("shipping_tax_amount_float", UNSET)

        formatted_shipping_tax_amount = d.pop("formatted_shipping_tax_amount", UNSET)

        payment_method_tax_amount_cents = d.pop("payment_method_tax_amount_cents", UNSET)

        payment_method_tax_amount_float = d.pop("payment_method_tax_amount_float", UNSET)

        formatted_payment_method_tax_amount = d.pop("formatted_payment_method_tax_amount", UNSET)

        adjustment_tax_amount_cents = d.pop("adjustment_tax_amount_cents", UNSET)

        adjustment_tax_amount_float = d.pop("adjustment_tax_amount_float", UNSET)

        formatted_adjustment_tax_amount = d.pop("formatted_adjustment_tax_amount", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        total_amount_float = d.pop("total_amount_float", UNSET)

        formatted_total_amount = d.pop("formatted_total_amount", UNSET)

        total_taxable_amount_cents = d.pop("total_taxable_amount_cents", UNSET)

        total_taxable_amount_float = d.pop("total_taxable_amount_float", UNSET)

        formatted_total_taxable_amount = d.pop("formatted_total_taxable_amount", UNSET)

        subtotal_taxable_amount_cents = d.pop("subtotal_taxable_amount_cents", UNSET)

        subtotal_taxable_amount_float = d.pop("subtotal_taxable_amount_float", UNSET)

        formatted_subtotal_taxable_amount = d.pop("formatted_subtotal_taxable_amount", UNSET)

        shipping_taxable_amount_cents = d.pop("shipping_taxable_amount_cents", UNSET)

        shipping_taxable_amount_float = d.pop("shipping_taxable_amount_float", UNSET)

        formatted_shipping_taxable_amount = d.pop("formatted_shipping_taxable_amount", UNSET)

        payment_method_taxable_amount_cents = d.pop("payment_method_taxable_amount_cents", UNSET)

        payment_method_taxable_amount_float = d.pop("payment_method_taxable_amount_float", UNSET)

        formatted_payment_method_taxable_amount = d.pop("formatted_payment_method_taxable_amount", UNSET)

        adjustment_taxable_amount_cents = d.pop("adjustment_taxable_amount_cents", UNSET)

        adjustment_taxable_amount_float = d.pop("adjustment_taxable_amount_float", UNSET)

        formatted_adjustment_taxable_amount = d.pop("formatted_adjustment_taxable_amount", UNSET)

        total_amount_with_taxes_cents = d.pop("total_amount_with_taxes_cents", UNSET)

        total_amount_with_taxes_float = d.pop("total_amount_with_taxes_float", UNSET)

        formatted_total_amount_with_taxes = d.pop("formatted_total_amount_with_taxes", UNSET)

        fees_amount_cents = d.pop("fees_amount_cents", UNSET)

        fees_amount_float = d.pop("fees_amount_float", UNSET)

        formatted_fees_amount = d.pop("formatted_fees_amount", UNSET)

        duty_amount_cents = d.pop("duty_amount_cents", UNSET)

        duty_amount_float = d.pop("duty_amount_float", UNSET)

        formatted_duty_amount = d.pop("formatted_duty_amount", UNSET)

        skus_count = d.pop("skus_count", UNSET)

        line_item_options_count = d.pop("line_item_options_count", UNSET)

        shipments_count = d.pop("shipments_count", UNSET)

        tax_calculations_count = d.pop("tax_calculations_count", UNSET)

        _payment_source_details = d.pop("payment_source_details", UNSET)
        payment_source_details: Union[Unset, GETordersorderIdResponse200DataAttributesPaymentSourceDetails]
        if isinstance(_payment_source_details, Unset):
            payment_source_details = UNSET
        else:
            payment_source_details = GETordersorderIdResponse200DataAttributesPaymentSourceDetails.from_dict(
                _payment_source_details
            )

        token = d.pop("token", UNSET)

        cart_url = d.pop("cart_url", UNSET)

        return_url = d.pop("return_url", UNSET)

        terms_url = d.pop("terms_url", UNSET)

        privacy_url = d.pop("privacy_url", UNSET)

        checkout_url = d.pop("checkout_url", UNSET)

        placed_at = d.pop("placed_at", UNSET)

        approved_at = d.pop("approved_at", UNSET)

        cancelled_at = d.pop("cancelled_at", UNSET)

        payment_updated_at = d.pop("payment_updated_at", UNSET)

        fulfillment_updated_at = d.pop("fulfillment_updated_at", UNSET)

        refreshed_at = d.pop("refreshed_at", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        reference = d.pop("reference", UNSET)

        reference_origin = d.pop("reference_origin", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GETordersorderIdResponse200DataAttributesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GETordersorderIdResponse200DataAttributesMetadata.from_dict(_metadata)

        ge_tordersorder_id_response_200_data_attributes = cls(
            number=number,
            autorefresh=autorefresh,
            status=status,
            payment_status=payment_status,
            fulfillment_status=fulfillment_status,
            guest=guest,
            editable=editable,
            customer_email=customer_email,
            language_code=language_code,
            currency_code=currency_code,
            tax_included=tax_included,
            tax_rate=tax_rate,
            freight_taxable=freight_taxable,
            requires_billing_info=requires_billing_info,
            country_code=country_code,
            shipping_country_code_lock=shipping_country_code_lock,
            coupon_code=coupon_code,
            gift_card_code=gift_card_code,
            gift_card_or_coupon_code=gift_card_or_coupon_code,
            subtotal_amount_cents=subtotal_amount_cents,
            subtotal_amount_float=subtotal_amount_float,
            formatted_subtotal_amount=formatted_subtotal_amount,
            shipping_amount_cents=shipping_amount_cents,
            shipping_amount_float=shipping_amount_float,
            formatted_shipping_amount=formatted_shipping_amount,
            payment_method_amount_cents=payment_method_amount_cents,
            payment_method_amount_float=payment_method_amount_float,
            formatted_payment_method_amount=formatted_payment_method_amount,
            discount_amount_cents=discount_amount_cents,
            discount_amount_float=discount_amount_float,
            formatted_discount_amount=formatted_discount_amount,
            adjustment_amount_cents=adjustment_amount_cents,
            adjustment_amount_float=adjustment_amount_float,
            formatted_adjustment_amount=formatted_adjustment_amount,
            gift_card_amount_cents=gift_card_amount_cents,
            gift_card_amount_float=gift_card_amount_float,
            formatted_gift_card_amount=formatted_gift_card_amount,
            total_tax_amount_cents=total_tax_amount_cents,
            total_tax_amount_float=total_tax_amount_float,
            formatted_total_tax_amount=formatted_total_tax_amount,
            subtotal_tax_amount_cents=subtotal_tax_amount_cents,
            subtotal_tax_amount_float=subtotal_tax_amount_float,
            formatted_subtotal_tax_amount=formatted_subtotal_tax_amount,
            shipping_tax_amount_cents=shipping_tax_amount_cents,
            shipping_tax_amount_float=shipping_tax_amount_float,
            formatted_shipping_tax_amount=formatted_shipping_tax_amount,
            payment_method_tax_amount_cents=payment_method_tax_amount_cents,
            payment_method_tax_amount_float=payment_method_tax_amount_float,
            formatted_payment_method_tax_amount=formatted_payment_method_tax_amount,
            adjustment_tax_amount_cents=adjustment_tax_amount_cents,
            adjustment_tax_amount_float=adjustment_tax_amount_float,
            formatted_adjustment_tax_amount=formatted_adjustment_tax_amount,
            total_amount_cents=total_amount_cents,
            total_amount_float=total_amount_float,
            formatted_total_amount=formatted_total_amount,
            total_taxable_amount_cents=total_taxable_amount_cents,
            total_taxable_amount_float=total_taxable_amount_float,
            formatted_total_taxable_amount=formatted_total_taxable_amount,
            subtotal_taxable_amount_cents=subtotal_taxable_amount_cents,
            subtotal_taxable_amount_float=subtotal_taxable_amount_float,
            formatted_subtotal_taxable_amount=formatted_subtotal_taxable_amount,
            shipping_taxable_amount_cents=shipping_taxable_amount_cents,
            shipping_taxable_amount_float=shipping_taxable_amount_float,
            formatted_shipping_taxable_amount=formatted_shipping_taxable_amount,
            payment_method_taxable_amount_cents=payment_method_taxable_amount_cents,
            payment_method_taxable_amount_float=payment_method_taxable_amount_float,
            formatted_payment_method_taxable_amount=formatted_payment_method_taxable_amount,
            adjustment_taxable_amount_cents=adjustment_taxable_amount_cents,
            adjustment_taxable_amount_float=adjustment_taxable_amount_float,
            formatted_adjustment_taxable_amount=formatted_adjustment_taxable_amount,
            total_amount_with_taxes_cents=total_amount_with_taxes_cents,
            total_amount_with_taxes_float=total_amount_with_taxes_float,
            formatted_total_amount_with_taxes=formatted_total_amount_with_taxes,
            fees_amount_cents=fees_amount_cents,
            fees_amount_float=fees_amount_float,
            formatted_fees_amount=formatted_fees_amount,
            duty_amount_cents=duty_amount_cents,
            duty_amount_float=duty_amount_float,
            formatted_duty_amount=formatted_duty_amount,
            skus_count=skus_count,
            line_item_options_count=line_item_options_count,
            shipments_count=shipments_count,
            tax_calculations_count=tax_calculations_count,
            payment_source_details=payment_source_details,
            token=token,
            cart_url=cart_url,
            return_url=return_url,
            terms_url=terms_url,
            privacy_url=privacy_url,
            checkout_url=checkout_url,
            placed_at=placed_at,
            approved_at=approved_at,
            cancelled_at=cancelled_at,
            payment_updated_at=payment_updated_at,
            fulfillment_updated_at=fulfillment_updated_at,
            refreshed_at=refreshed_at,
            archived_at=archived_at,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            reference_origin=reference_origin,
            metadata=metadata,
        )

        ge_tordersorder_id_response_200_data_attributes.additional_properties = d
        return ge_tordersorder_id_response_200_data_attributes

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
