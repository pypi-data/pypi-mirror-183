from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_payment import AdyenPayment
    from ..models.braintree_payment import BraintreePayment
    from ..models.checkout_com_payment import CheckoutComPayment
    from ..models.customer_payment_source_data_relationships_customer import (
        CustomerPaymentSourceDataRelationshipsCustomer,
    )
    from ..models.external_payment import ExternalPayment
    from ..models.klarna_payment import KlarnaPayment
    from ..models.paypal_payment import PaypalPayment
    from ..models.stripe_payment import StripePayment
    from ..models.wire_transfer import WireTransfer


T = TypeVar("T", bound="CustomerPaymentSourceDataRelationships")


@attr.s(auto_attribs=True)
class CustomerPaymentSourceDataRelationships:
    """
    Attributes:
        customer (Union[Unset, CustomerPaymentSourceDataRelationshipsCustomer]):
        payment_source (Union['AdyenPayment', 'BraintreePayment', 'CheckoutComPayment', 'ExternalPayment',
            'KlarnaPayment', 'PaypalPayment', 'StripePayment', 'WireTransfer', Unset]):
    """

    customer: Union[Unset, "CustomerPaymentSourceDataRelationshipsCustomer"] = UNSET
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

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

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
        if customer is not UNSET:
            field_dict["customer"] = customer
        if payment_source is not UNSET:
            field_dict["payment_source"] = payment_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_payment import AdyenPayment
        from ..models.braintree_payment import BraintreePayment
        from ..models.checkout_com_payment import CheckoutComPayment
        from ..models.customer_payment_source_data_relationships_customer import (
            CustomerPaymentSourceDataRelationshipsCustomer,
        )
        from ..models.external_payment import ExternalPayment
        from ..models.klarna_payment import KlarnaPayment
        from ..models.paypal_payment import PaypalPayment
        from ..models.stripe_payment import StripePayment
        from ..models.wire_transfer import WireTransfer

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CustomerPaymentSourceDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CustomerPaymentSourceDataRelationshipsCustomer.from_dict(_customer)

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

        customer_payment_source_data_relationships = cls(
            customer=customer,
            payment_source=payment_source,
        )

        customer_payment_source_data_relationships.additional_properties = d
        return customer_payment_source_data_relationships

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
