from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.adyen_payment import AdyenPayment
    from ..models.braintree_payment import BraintreePayment
    from ..models.checkout_com_payment import CheckoutComPayment
    from ..models.customer_payment_source_create_data_relationships_customer import (
        CustomerPaymentSourceCreateDataRelationshipsCustomer,
    )
    from ..models.external_payment import ExternalPayment
    from ..models.klarna_payment import KlarnaPayment
    from ..models.paypal_payment import PaypalPayment
    from ..models.stripe_payment import StripePayment
    from ..models.wire_transfer import WireTransfer


T = TypeVar("T", bound="CustomerPaymentSourceCreateDataRelationships")


@attr.s(auto_attribs=True)
class CustomerPaymentSourceCreateDataRelationships:
    """
    Attributes:
        customer (CustomerPaymentSourceCreateDataRelationshipsCustomer):
        payment_source (Union['AdyenPayment', 'BraintreePayment', 'CheckoutComPayment', 'ExternalPayment',
            'KlarnaPayment', 'PaypalPayment', 'StripePayment', 'WireTransfer']):
    """

    customer: "CustomerPaymentSourceCreateDataRelationshipsCustomer"
    payment_source: Union[
        "AdyenPayment",
        "BraintreePayment",
        "CheckoutComPayment",
        "ExternalPayment",
        "KlarnaPayment",
        "PaypalPayment",
        "StripePayment",
        "WireTransfer",
    ]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.adyen_payment import AdyenPayment
        from ..models.braintree_payment import BraintreePayment
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment

        customer = self.customer.to_dict()

        payment_source: Dict[str, Any]

        if isinstance(self.payment_source, AdyenPayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, BraintreePayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, CheckoutComPayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, ExternalPayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, KlarnaPayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, PaypalPayment):
            payment_source = self.payment_source.to_dict()

        elif isinstance(self.payment_source, StripePayment):
            payment_source = self.payment_source.to_dict()

        else:
            payment_source = self.payment_source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "payment_source": payment_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_payment import AdyenPayment
        from ..models.braintree_payment import BraintreePayment
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.customer_payment_source_create_data_relationships_customer import (
            CustomerPaymentSourceCreateDataRelationshipsCustomer,
        )
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment
        from ..models.wire_transfer import WireTransfer

        d = src_dict.copy()
        customer = CustomerPaymentSourceCreateDataRelationshipsCustomer.from_dict(d.pop("customer"))

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
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_0 = AdyenPayment.from_dict(data)

                return payment_source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_1 = BraintreePayment.from_dict(data)

                return payment_source_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_2 = CheckoutComPayment.from_dict(data)

                return payment_source_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_3 = ExternalPayment.from_dict(data)

                return payment_source_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_4 = KlarnaPayment.from_dict(data)

                return payment_source_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_5 = PaypalPayment.from_dict(data)

                return payment_source_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_source_type_6 = StripePayment.from_dict(data)

                return payment_source_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payment_source_type_7 = WireTransfer.from_dict(data)

            return payment_source_type_7

        payment_source = _parse_payment_source(d.pop("payment_source"))

        customer_payment_source_create_data_relationships = cls(
            customer=customer,
            payment_source=payment_source,
        )

        customer_payment_source_create_data_relationships.additional_properties = d
        return customer_payment_source_create_data_relationships

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
