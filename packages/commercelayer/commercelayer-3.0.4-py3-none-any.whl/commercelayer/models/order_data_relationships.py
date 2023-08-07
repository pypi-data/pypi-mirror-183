from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_payment import AdyenPayment
    from ..models.authorization import Authorization
    from ..models.braintree_payment import BraintreePayment
    from ..models.capture import Capture
    from ..models.checkout_com_payment import CheckoutComPayment
    from ..models.external_payment import ExternalPayment
    from ..models.klarna_payment import KlarnaPayment
    from ..models.order_data_relationships_attachments import OrderDataRelationshipsAttachments
    from ..models.order_data_relationships_authorizations import OrderDataRelationshipsAuthorizations
    from ..models.order_data_relationships_available_customer_payment_sources import (
        OrderDataRelationshipsAvailableCustomerPaymentSources,
    )
    from ..models.order_data_relationships_available_free_bundles import OrderDataRelationshipsAvailableFreeBundles
    from ..models.order_data_relationships_available_free_skus import OrderDataRelationshipsAvailableFreeSkus
    from ..models.order_data_relationships_available_payment_methods import (
        OrderDataRelationshipsAvailablePaymentMethods,
    )
    from ..models.order_data_relationships_billing_address import OrderDataRelationshipsBillingAddress
    from ..models.order_data_relationships_captures import OrderDataRelationshipsCaptures
    from ..models.order_data_relationships_customer import OrderDataRelationshipsCustomer
    from ..models.order_data_relationships_events import OrderDataRelationshipsEvents
    from ..models.order_data_relationships_line_items import OrderDataRelationshipsLineItems
    from ..models.order_data_relationships_market import OrderDataRelationshipsMarket
    from ..models.order_data_relationships_order_copies import OrderDataRelationshipsOrderCopies
    from ..models.order_data_relationships_order_subscriptions import OrderDataRelationshipsOrderSubscriptions
    from ..models.order_data_relationships_payment_method import OrderDataRelationshipsPaymentMethod
    from ..models.order_data_relationships_refunds import OrderDataRelationshipsRefunds
    from ..models.order_data_relationships_shipments import OrderDataRelationshipsShipments
    from ..models.order_data_relationships_shipping_address import OrderDataRelationshipsShippingAddress
    from ..models.order_data_relationships_voids import OrderDataRelationshipsVoids
    from ..models.paypal_payment import PaypalPayment
    from ..models.refund import Refund
    from ..models.stripe_payment import StripePayment
    from ..models.void import Void
    from ..models.wire_transfer import WireTransfer


T = TypeVar("T", bound="OrderDataRelationships")


@attr.s(auto_attribs=True)
class OrderDataRelationships:
    """
    Attributes:
        market (Union[Unset, OrderDataRelationshipsMarket]):
        customer (Union[Unset, OrderDataRelationshipsCustomer]):
        shipping_address (Union[Unset, OrderDataRelationshipsShippingAddress]):
        billing_address (Union[Unset, OrderDataRelationshipsBillingAddress]):
        available_payment_methods (Union[Unset, OrderDataRelationshipsAvailablePaymentMethods]):
        available_customer_payment_sources (Union[Unset, OrderDataRelationshipsAvailableCustomerPaymentSources]):
        available_free_skus (Union[Unset, OrderDataRelationshipsAvailableFreeSkus]):
        available_free_bundles (Union[Unset, OrderDataRelationshipsAvailableFreeBundles]):
        payment_method (Union[Unset, OrderDataRelationshipsPaymentMethod]):
        payment_source (Union['AdyenPayment', 'BraintreePayment', 'CheckoutComPayment', 'ExternalPayment',
            'KlarnaPayment', 'PaypalPayment', 'StripePayment', 'WireTransfer', Unset]):
        line_items (Union[Unset, OrderDataRelationshipsLineItems]):
        shipments (Union[Unset, OrderDataRelationshipsShipments]):
        transactions (Union['Authorization', 'Capture', 'Refund', 'Void', Unset]):
        authorizations (Union[Unset, OrderDataRelationshipsAuthorizations]):
        captures (Union[Unset, OrderDataRelationshipsCaptures]):
        voids (Union[Unset, OrderDataRelationshipsVoids]):
        refunds (Union[Unset, OrderDataRelationshipsRefunds]):
        order_subscriptions (Union[Unset, OrderDataRelationshipsOrderSubscriptions]):
        order_copies (Union[Unset, OrderDataRelationshipsOrderCopies]):
        attachments (Union[Unset, OrderDataRelationshipsAttachments]):
        events (Union[Unset, OrderDataRelationshipsEvents]):
    """

    market: Union[Unset, "OrderDataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "OrderDataRelationshipsCustomer"] = UNSET
    shipping_address: Union[Unset, "OrderDataRelationshipsShippingAddress"] = UNSET
    billing_address: Union[Unset, "OrderDataRelationshipsBillingAddress"] = UNSET
    available_payment_methods: Union[Unset, "OrderDataRelationshipsAvailablePaymentMethods"] = UNSET
    available_customer_payment_sources: Union[Unset, "OrderDataRelationshipsAvailableCustomerPaymentSources"] = UNSET
    available_free_skus: Union[Unset, "OrderDataRelationshipsAvailableFreeSkus"] = UNSET
    available_free_bundles: Union[Unset, "OrderDataRelationshipsAvailableFreeBundles"] = UNSET
    payment_method: Union[Unset, "OrderDataRelationshipsPaymentMethod"] = UNSET
    payment_source: Union[
        "AdyenPayment",
        "BraintreePayment",
        "CheckoutComPayment",
        "ExternalPayment",
        "KlarnaPayment",
        "PaypalPayment",
        "StripePayment",
        "WireTransfer",
        Unset,
    ] = UNSET
    line_items: Union[Unset, "OrderDataRelationshipsLineItems"] = UNSET
    shipments: Union[Unset, "OrderDataRelationshipsShipments"] = UNSET
    transactions: Union["Authorization", "Capture", "Refund", "Void", Unset] = UNSET
    authorizations: Union[Unset, "OrderDataRelationshipsAuthorizations"] = UNSET
    captures: Union[Unset, "OrderDataRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "OrderDataRelationshipsVoids"] = UNSET
    refunds: Union[Unset, "OrderDataRelationshipsRefunds"] = UNSET
    order_subscriptions: Union[Unset, "OrderDataRelationshipsOrderSubscriptions"] = UNSET
    order_copies: Union[Unset, "OrderDataRelationshipsOrderCopies"] = UNSET
    attachments: Union[Unset, "OrderDataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "OrderDataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.adyen_payment import AdyenPayment
        from ..models.authorization import Authorization
        from ..models.braintree_payment import BraintreePayment
        from ..models.capture import Capture
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment
        from ..models.void import Void

        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        available_payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_payment_methods, Unset):
            available_payment_methods = self.available_payment_methods.to_dict()

        available_customer_payment_sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_customer_payment_sources, Unset):
            available_customer_payment_sources = self.available_customer_payment_sources.to_dict()

        available_free_skus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_free_skus, Unset):
            available_free_skus = self.available_free_skus.to_dict()

        available_free_bundles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_free_bundles, Unset):
            available_free_bundles = self.available_free_bundles.to_dict()

        payment_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.to_dict()

        payment_source: Union[Dict[str, Any], Unset]
        if isinstance(self.payment_source, Unset):
            payment_source = UNSET

        elif isinstance(self.payment_source, AdyenPayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, BraintreePayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, CheckoutComPayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, ExternalPayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, KlarnaPayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, PaypalPayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, StripePayment):
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        else:
            payment_source = UNSET
            if not isinstance(self.payment_source, Unset):
                payment_source = self.payment_source.to_dict()

        line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = self.line_items.to_dict()

        shipments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipments, Unset):
            shipments = self.shipments.to_dict()

        transactions: Union[Dict[str, Any], Unset]
        if isinstance(self.transactions, Unset):
            transactions = UNSET

        elif isinstance(self.transactions, Authorization):
            transactions = UNSET
            if not isinstance(self.transactions, Unset):
                transactions = self.transactions.to_dict()

        elif isinstance(self.transactions, Void):
            transactions = UNSET
            if not isinstance(self.transactions, Unset):
                transactions = self.transactions.to_dict()

        elif isinstance(self.transactions, Capture):
            transactions = UNSET
            if not isinstance(self.transactions, Unset):
                transactions = self.transactions.to_dict()

        else:
            transactions = UNSET
            if not isinstance(self.transactions, Unset):
                transactions = self.transactions.to_dict()

        authorizations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authorizations, Unset):
            authorizations = self.authorizations.to_dict()

        captures: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.captures, Unset):
            captures = self.captures.to_dict()

        voids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voids, Unset):
            voids = self.voids.to_dict()

        refunds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = self.refunds.to_dict()

        order_subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_subscriptions, Unset):
            order_subscriptions = self.order_subscriptions.to_dict()

        order_copies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_copies, Unset):
            order_copies = self.order_copies.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if customer is not UNSET:
            field_dict["customer"] = customer
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if available_payment_methods is not UNSET:
            field_dict["available_payment_methods"] = available_payment_methods
        if available_customer_payment_sources is not UNSET:
            field_dict["available_customer_payment_sources"] = available_customer_payment_sources
        if available_free_skus is not UNSET:
            field_dict["available_free_skus"] = available_free_skus
        if available_free_bundles is not UNSET:
            field_dict["available_free_bundles"] = available_free_bundles
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_source is not UNSET:
            field_dict["payment_source"] = payment_source
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if shipments is not UNSET:
            field_dict["shipments"] = shipments
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if authorizations is not UNSET:
            field_dict["authorizations"] = authorizations
        if captures is not UNSET:
            field_dict["captures"] = captures
        if voids is not UNSET:
            field_dict["voids"] = voids
        if refunds is not UNSET:
            field_dict["refunds"] = refunds
        if order_subscriptions is not UNSET:
            field_dict["order_subscriptions"] = order_subscriptions
        if order_copies is not UNSET:
            field_dict["order_copies"] = order_copies
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_payment import AdyenPayment
        from ..models.authorization import Authorization
        from ..models.braintree_payment import BraintreePayment
        from ..models.capture import Capture
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.order_data_relationships_attachments import OrderDataRelationshipsAttachments
        from ..models.order_data_relationships_authorizations import OrderDataRelationshipsAuthorizations
        from ..models.order_data_relationships_available_customer_payment_sources import (
            OrderDataRelationshipsAvailableCustomerPaymentSources,
        )
        from ..models.order_data_relationships_available_free_bundles import OrderDataRelationshipsAvailableFreeBundles
        from ..models.order_data_relationships_available_free_skus import OrderDataRelationshipsAvailableFreeSkus
        from ..models.order_data_relationships_available_payment_methods import (
            OrderDataRelationshipsAvailablePaymentMethods,
        )
        from ..models.order_data_relationships_billing_address import OrderDataRelationshipsBillingAddress
        from ..models.order_data_relationships_captures import OrderDataRelationshipsCaptures
        from ..models.order_data_relationships_customer import OrderDataRelationshipsCustomer
        from ..models.order_data_relationships_events import OrderDataRelationshipsEvents
        from ..models.order_data_relationships_line_items import OrderDataRelationshipsLineItems
        from ..models.order_data_relationships_market import OrderDataRelationshipsMarket
        from ..models.order_data_relationships_order_copies import OrderDataRelationshipsOrderCopies
        from ..models.order_data_relationships_order_subscriptions import OrderDataRelationshipsOrderSubscriptions
        from ..models.order_data_relationships_payment_method import OrderDataRelationshipsPaymentMethod
        from ..models.order_data_relationships_refunds import OrderDataRelationshipsRefunds
        from ..models.order_data_relationships_shipments import OrderDataRelationshipsShipments
        from ..models.order_data_relationships_shipping_address import OrderDataRelationshipsShippingAddress
        from ..models.order_data_relationships_voids import OrderDataRelationshipsVoids
        from ..models.paypal_payment import PaypalPayment
        from ..models.refund import Refund
        from ..models.stripe_payment import StripePayment
        from ..models.void import Void
        from ..models.wire_transfer import WireTransfer

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, OrderDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = OrderDataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, OrderDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = OrderDataRelationshipsCustomer.from_dict(_customer)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, OrderDataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = OrderDataRelationshipsShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, OrderDataRelationshipsBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = OrderDataRelationshipsBillingAddress.from_dict(_billing_address)

        _available_payment_methods = d.pop("available_payment_methods", UNSET)
        available_payment_methods: Union[Unset, OrderDataRelationshipsAvailablePaymentMethods]
        if isinstance(_available_payment_methods, Unset):
            available_payment_methods = UNSET
        else:
            available_payment_methods = OrderDataRelationshipsAvailablePaymentMethods.from_dict(
                _available_payment_methods
            )

        _available_customer_payment_sources = d.pop("available_customer_payment_sources", UNSET)
        available_customer_payment_sources: Union[Unset, OrderDataRelationshipsAvailableCustomerPaymentSources]
        if isinstance(_available_customer_payment_sources, Unset):
            available_customer_payment_sources = UNSET
        else:
            available_customer_payment_sources = OrderDataRelationshipsAvailableCustomerPaymentSources.from_dict(
                _available_customer_payment_sources
            )

        _available_free_skus = d.pop("available_free_skus", UNSET)
        available_free_skus: Union[Unset, OrderDataRelationshipsAvailableFreeSkus]
        if isinstance(_available_free_skus, Unset):
            available_free_skus = UNSET
        else:
            available_free_skus = OrderDataRelationshipsAvailableFreeSkus.from_dict(_available_free_skus)

        _available_free_bundles = d.pop("available_free_bundles", UNSET)
        available_free_bundles: Union[Unset, OrderDataRelationshipsAvailableFreeBundles]
        if isinstance(_available_free_bundles, Unset):
            available_free_bundles = UNSET
        else:
            available_free_bundles = OrderDataRelationshipsAvailableFreeBundles.from_dict(_available_free_bundles)

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, OrderDataRelationshipsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = OrderDataRelationshipsPaymentMethod.from_dict(_payment_method)

        def _parse_payment_source(
            data: object,
        ) -> Union[
            "AdyenPayment",
            "BraintreePayment",
            "CheckoutComPayment",
            "ExternalPayment",
            "KlarnaPayment",
            "PaypalPayment",
            "StripePayment",
            "WireTransfer",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_0 = data
                payment_source_type_0: Union[Unset, AdyenPayment]
                if isinstance(_payment_source_type_0, Unset):
                    payment_source_type_0 = UNSET
                else:
                    payment_source_type_0 = AdyenPayment.from_dict(_payment_source_type_0)

                return payment_source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_1 = data
                payment_source_type_1: Union[Unset, BraintreePayment]
                if isinstance(_payment_source_type_1, Unset):
                    payment_source_type_1 = UNSET
                else:
                    payment_source_type_1 = BraintreePayment.from_dict(_payment_source_type_1)

                return payment_source_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_2 = data
                payment_source_type_2: Union[Unset, CheckoutComPayment]
                if isinstance(_payment_source_type_2, Unset):
                    payment_source_type_2 = UNSET
                else:
                    payment_source_type_2 = CheckoutComPayment.from_dict(_payment_source_type_2)

                return payment_source_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_3 = data
                payment_source_type_3: Union[Unset, ExternalPayment]
                if isinstance(_payment_source_type_3, Unset):
                    payment_source_type_3 = UNSET
                else:
                    payment_source_type_3 = ExternalPayment.from_dict(_payment_source_type_3)

                return payment_source_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_4 = data
                payment_source_type_4: Union[Unset, KlarnaPayment]
                if isinstance(_payment_source_type_4, Unset):
                    payment_source_type_4 = UNSET
                else:
                    payment_source_type_4 = KlarnaPayment.from_dict(_payment_source_type_4)

                return payment_source_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_5 = data
                payment_source_type_5: Union[Unset, PaypalPayment]
                if isinstance(_payment_source_type_5, Unset):
                    payment_source_type_5 = UNSET
                else:
                    payment_source_type_5 = PaypalPayment.from_dict(_payment_source_type_5)

                return payment_source_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payment_source_type_6 = data
                payment_source_type_6: Union[Unset, StripePayment]
                if isinstance(_payment_source_type_6, Unset):
                    payment_source_type_6 = UNSET
                else:
                    payment_source_type_6 = StripePayment.from_dict(_payment_source_type_6)

                return payment_source_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _payment_source_type_7 = data
            payment_source_type_7: Union[Unset, WireTransfer]
            if isinstance(_payment_source_type_7, Unset):
                payment_source_type_7 = UNSET
            else:
                payment_source_type_7 = WireTransfer.from_dict(_payment_source_type_7)

            return payment_source_type_7

        payment_source = _parse_payment_source(d.pop("payment_source", UNSET))

        _line_items = d.pop("line_items", UNSET)
        line_items: Union[Unset, OrderDataRelationshipsLineItems]
        if isinstance(_line_items, Unset):
            line_items = UNSET
        else:
            line_items = OrderDataRelationshipsLineItems.from_dict(_line_items)

        _shipments = d.pop("shipments", UNSET)
        shipments: Union[Unset, OrderDataRelationshipsShipments]
        if isinstance(_shipments, Unset):
            shipments = UNSET
        else:
            shipments = OrderDataRelationshipsShipments.from_dict(_shipments)

        def _parse_transactions(data: object) -> Union["Authorization", "Capture", "Refund", "Void", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _transactions_type_0 = data
                transactions_type_0: Union[Unset, Authorization]
                if isinstance(_transactions_type_0, Unset):
                    transactions_type_0 = UNSET
                else:
                    transactions_type_0 = Authorization.from_dict(_transactions_type_0)

                return transactions_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _transactions_type_1 = data
                transactions_type_1: Union[Unset, Void]
                if isinstance(_transactions_type_1, Unset):
                    transactions_type_1 = UNSET
                else:
                    transactions_type_1 = Void.from_dict(_transactions_type_1)

                return transactions_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _transactions_type_2 = data
                transactions_type_2: Union[Unset, Capture]
                if isinstance(_transactions_type_2, Unset):
                    transactions_type_2 = UNSET
                else:
                    transactions_type_2 = Capture.from_dict(_transactions_type_2)

                return transactions_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _transactions_type_3 = data
            transactions_type_3: Union[Unset, Refund]
            if isinstance(_transactions_type_3, Unset):
                transactions_type_3 = UNSET
            else:
                transactions_type_3 = Refund.from_dict(_transactions_type_3)

            return transactions_type_3

        transactions = _parse_transactions(d.pop("transactions", UNSET))

        _authorizations = d.pop("authorizations", UNSET)
        authorizations: Union[Unset, OrderDataRelationshipsAuthorizations]
        if isinstance(_authorizations, Unset):
            authorizations = UNSET
        else:
            authorizations = OrderDataRelationshipsAuthorizations.from_dict(_authorizations)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, OrderDataRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = OrderDataRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, OrderDataRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = OrderDataRelationshipsVoids.from_dict(_voids)

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, OrderDataRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = OrderDataRelationshipsRefunds.from_dict(_refunds)

        _order_subscriptions = d.pop("order_subscriptions", UNSET)
        order_subscriptions: Union[Unset, OrderDataRelationshipsOrderSubscriptions]
        if isinstance(_order_subscriptions, Unset):
            order_subscriptions = UNSET
        else:
            order_subscriptions = OrderDataRelationshipsOrderSubscriptions.from_dict(_order_subscriptions)

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, OrderDataRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = OrderDataRelationshipsOrderCopies.from_dict(_order_copies)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, OrderDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = OrderDataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, OrderDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = OrderDataRelationshipsEvents.from_dict(_events)

        order_data_relationships = cls(
            market=market,
            customer=customer,
            shipping_address=shipping_address,
            billing_address=billing_address,
            available_payment_methods=available_payment_methods,
            available_customer_payment_sources=available_customer_payment_sources,
            available_free_skus=available_free_skus,
            available_free_bundles=available_free_bundles,
            payment_method=payment_method,
            payment_source=payment_source,
            line_items=line_items,
            shipments=shipments,
            transactions=transactions,
            authorizations=authorizations,
            captures=captures,
            voids=voids,
            refunds=refunds,
            order_subscriptions=order_subscriptions,
            order_copies=order_copies,
            attachments=attachments,
            events=events,
        )

        order_data_relationships.additional_properties = d
        return order_data_relationships

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
