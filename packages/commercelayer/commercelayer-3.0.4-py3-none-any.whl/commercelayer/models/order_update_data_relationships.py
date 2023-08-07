from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_payment import AdyenPayment
    from ..models.braintree_payment import BraintreePayment
    from ..models.checkout_com_payment import CheckoutComPayment
    from ..models.external_payment import ExternalPayment
    from ..models.klarna_payment import KlarnaPayment
    from ..models.order_update_data_relationships_billing_address import OrderUpdateDataRelationshipsBillingAddress
    from ..models.order_update_data_relationships_customer import OrderUpdateDataRelationshipsCustomer
    from ..models.order_update_data_relationships_market import OrderUpdateDataRelationshipsMarket
    from ..models.order_update_data_relationships_payment_method import OrderUpdateDataRelationshipsPaymentMethod
    from ..models.order_update_data_relationships_shipping_address import OrderUpdateDataRelationshipsShippingAddress
    from ..models.paypal_payment import PaypalPayment
    from ..models.stripe_payment import StripePayment
    from ..models.wire_transfer import WireTransfer


T = TypeVar("T", bound="OrderUpdateDataRelationships")


@attr.s(auto_attribs=True)
class OrderUpdateDataRelationships:
    """
    Attributes:
        market (Union[Unset, OrderUpdateDataRelationshipsMarket]):
        customer (Union[Unset, OrderUpdateDataRelationshipsCustomer]):
        shipping_address (Union[Unset, OrderUpdateDataRelationshipsShippingAddress]):
        billing_address (Union[Unset, OrderUpdateDataRelationshipsBillingAddress]):
        payment_method (Union[Unset, OrderUpdateDataRelationshipsPaymentMethod]):
        payment_source (Union['AdyenPayment', 'BraintreePayment', 'CheckoutComPayment', 'ExternalPayment',
            'KlarnaPayment', 'PaypalPayment', 'StripePayment', 'WireTransfer', Unset]):
    """

    market: Union[Unset, "OrderUpdateDataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "OrderUpdateDataRelationshipsCustomer"] = UNSET
    shipping_address: Union[Unset, "OrderUpdateDataRelationshipsShippingAddress"] = UNSET
    billing_address: Union[Unset, "OrderUpdateDataRelationshipsBillingAddress"] = UNSET
    payment_method: Union[Unset, "OrderUpdateDataRelationshipsPaymentMethod"] = UNSET
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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.adyen_payment import AdyenPayment
        from ..models.braintree_payment import BraintreePayment
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment

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
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_source is not UNSET:
            field_dict["payment_source"] = payment_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_payment import AdyenPayment
        from ..models.braintree_payment import BraintreePayment
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.order_update_data_relationships_billing_address import OrderUpdateDataRelationshipsBillingAddress
        from ..models.order_update_data_relationships_customer import OrderUpdateDataRelationshipsCustomer
        from ..models.order_update_data_relationships_market import OrderUpdateDataRelationshipsMarket
        from ..models.order_update_data_relationships_payment_method import OrderUpdateDataRelationshipsPaymentMethod
        from ..models.order_update_data_relationships_shipping_address import (
            OrderUpdateDataRelationshipsShippingAddress,
        )
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment
        from ..models.wire_transfer import WireTransfer

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, OrderUpdateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = OrderUpdateDataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, OrderUpdateDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = OrderUpdateDataRelationshipsCustomer.from_dict(_customer)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, OrderUpdateDataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = OrderUpdateDataRelationshipsShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, OrderUpdateDataRelationshipsBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = OrderUpdateDataRelationshipsBillingAddress.from_dict(_billing_address)

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, OrderUpdateDataRelationshipsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = OrderUpdateDataRelationshipsPaymentMethod.from_dict(_payment_method)

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

        order_update_data_relationships = cls(
            market=market,
            customer=customer,
            shipping_address=shipping_address,
            billing_address=billing_address,
            payment_method=payment_method,
            payment_source=payment_source,
        )

        order_update_data_relationships.additional_properties = d
        return order_update_data_relationships

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
