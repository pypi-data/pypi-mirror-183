from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tordersorder_id_response_200_data_relationships_attachments import (
        GETordersorderIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_authorizations import (
        GETordersorderIdResponse200DataRelationshipsAuthorizations,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_available_customer_payment_sources import (
        GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_available_free_bundles import (
        GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_available_free_skus import (
        GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_available_payment_methods import (
        GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_billing_address import (
        GETordersorderIdResponse200DataRelationshipsBillingAddress,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_captures import (
        GETordersorderIdResponse200DataRelationshipsCaptures,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_customer import (
        GETordersorderIdResponse200DataRelationshipsCustomer,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_events import (
        GETordersorderIdResponse200DataRelationshipsEvents,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_line_items import (
        GETordersorderIdResponse200DataRelationshipsLineItems,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_market import (
        GETordersorderIdResponse200DataRelationshipsMarket,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_order_copies import (
        GETordersorderIdResponse200DataRelationshipsOrderCopies,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions import (
        GETordersorderIdResponse200DataRelationshipsOrderSubscriptions,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_payment_method import (
        GETordersorderIdResponse200DataRelationshipsPaymentMethod,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_payment_source import (
        GETordersorderIdResponse200DataRelationshipsPaymentSource,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_refunds import (
        GETordersorderIdResponse200DataRelationshipsRefunds,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_shipments import (
        GETordersorderIdResponse200DataRelationshipsShipments,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_shipping_address import (
        GETordersorderIdResponse200DataRelationshipsShippingAddress,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_transactions import (
        GETordersorderIdResponse200DataRelationshipsTransactions,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_voids import (
        GETordersorderIdResponse200DataRelationshipsVoids,
    )


T = TypeVar("T", bound="GETordersorderIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETordersorderIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, GETordersorderIdResponse200DataRelationshipsMarket]):
        customer (Union[Unset, GETordersorderIdResponse200DataRelationshipsCustomer]):
        shipping_address (Union[Unset, GETordersorderIdResponse200DataRelationshipsShippingAddress]):
        billing_address (Union[Unset, GETordersorderIdResponse200DataRelationshipsBillingAddress]):
        available_payment_methods (Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods]):
        available_customer_payment_sources (Union[Unset,
            GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources]):
        available_free_skus (Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus]):
        available_free_bundles (Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles]):
        payment_method (Union[Unset, GETordersorderIdResponse200DataRelationshipsPaymentMethod]):
        payment_source (Union[Unset, GETordersorderIdResponse200DataRelationshipsPaymentSource]):
        line_items (Union[Unset, GETordersorderIdResponse200DataRelationshipsLineItems]):
        shipments (Union[Unset, GETordersorderIdResponse200DataRelationshipsShipments]):
        transactions (Union[Unset, GETordersorderIdResponse200DataRelationshipsTransactions]):
        authorizations (Union[Unset, GETordersorderIdResponse200DataRelationshipsAuthorizations]):
        captures (Union[Unset, GETordersorderIdResponse200DataRelationshipsCaptures]):
        voids (Union[Unset, GETordersorderIdResponse200DataRelationshipsVoids]):
        refunds (Union[Unset, GETordersorderIdResponse200DataRelationshipsRefunds]):
        order_subscriptions (Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptions]):
        order_copies (Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderCopies]):
        attachments (Union[Unset, GETordersorderIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, GETordersorderIdResponse200DataRelationshipsEvents]):
    """

    market: Union[Unset, "GETordersorderIdResponse200DataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "GETordersorderIdResponse200DataRelationshipsCustomer"] = UNSET
    shipping_address: Union[Unset, "GETordersorderIdResponse200DataRelationshipsShippingAddress"] = UNSET
    billing_address: Union[Unset, "GETordersorderIdResponse200DataRelationshipsBillingAddress"] = UNSET
    available_payment_methods: Union[
        Unset, "GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods"
    ] = UNSET
    available_customer_payment_sources: Union[
        Unset, "GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources"
    ] = UNSET
    available_free_skus: Union[Unset, "GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus"] = UNSET
    available_free_bundles: Union[Unset, "GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles"] = UNSET
    payment_method: Union[Unset, "GETordersorderIdResponse200DataRelationshipsPaymentMethod"] = UNSET
    payment_source: Union[Unset, "GETordersorderIdResponse200DataRelationshipsPaymentSource"] = UNSET
    line_items: Union[Unset, "GETordersorderIdResponse200DataRelationshipsLineItems"] = UNSET
    shipments: Union[Unset, "GETordersorderIdResponse200DataRelationshipsShipments"] = UNSET
    transactions: Union[Unset, "GETordersorderIdResponse200DataRelationshipsTransactions"] = UNSET
    authorizations: Union[Unset, "GETordersorderIdResponse200DataRelationshipsAuthorizations"] = UNSET
    captures: Union[Unset, "GETordersorderIdResponse200DataRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "GETordersorderIdResponse200DataRelationshipsVoids"] = UNSET
    refunds: Union[Unset, "GETordersorderIdResponse200DataRelationshipsRefunds"] = UNSET
    order_subscriptions: Union[Unset, "GETordersorderIdResponse200DataRelationshipsOrderSubscriptions"] = UNSET
    order_copies: Union[Unset, "GETordersorderIdResponse200DataRelationshipsOrderCopies"] = UNSET
    attachments: Union[Unset, "GETordersorderIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETordersorderIdResponse200DataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        payment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_source, Unset):
            payment_source = self.payment_source.to_dict()

        line_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = self.line_items.to_dict()

        shipments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipments, Unset):
            shipments = self.shipments.to_dict()

        transactions: Union[Unset, Dict[str, Any]] = UNSET
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
        from ..models.ge_tordersorder_id_response_200_data_relationships_attachments import (
            GETordersorderIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_authorizations import (
            GETordersorderIdResponse200DataRelationshipsAuthorizations,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_available_customer_payment_sources import (
            GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_available_free_bundles import (
            GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_available_free_skus import (
            GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_available_payment_methods import (
            GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_billing_address import (
            GETordersorderIdResponse200DataRelationshipsBillingAddress,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_captures import (
            GETordersorderIdResponse200DataRelationshipsCaptures,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_customer import (
            GETordersorderIdResponse200DataRelationshipsCustomer,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_events import (
            GETordersorderIdResponse200DataRelationshipsEvents,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_line_items import (
            GETordersorderIdResponse200DataRelationshipsLineItems,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_market import (
            GETordersorderIdResponse200DataRelationshipsMarket,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_order_copies import (
            GETordersorderIdResponse200DataRelationshipsOrderCopies,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions import (
            GETordersorderIdResponse200DataRelationshipsOrderSubscriptions,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_payment_method import (
            GETordersorderIdResponse200DataRelationshipsPaymentMethod,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_payment_source import (
            GETordersorderIdResponse200DataRelationshipsPaymentSource,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_refunds import (
            GETordersorderIdResponse200DataRelationshipsRefunds,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_shipments import (
            GETordersorderIdResponse200DataRelationshipsShipments,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_shipping_address import (
            GETordersorderIdResponse200DataRelationshipsShippingAddress,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_transactions import (
            GETordersorderIdResponse200DataRelationshipsTransactions,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_voids import (
            GETordersorderIdResponse200DataRelationshipsVoids,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETordersorderIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETordersorderIdResponse200DataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETordersorderIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETordersorderIdResponse200DataRelationshipsCustomer.from_dict(_customer)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, GETordersorderIdResponse200DataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = GETordersorderIdResponse200DataRelationshipsShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, GETordersorderIdResponse200DataRelationshipsBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = GETordersorderIdResponse200DataRelationshipsBillingAddress.from_dict(_billing_address)

        _available_payment_methods = d.pop("available_payment_methods", UNSET)
        available_payment_methods: Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods]
        if isinstance(_available_payment_methods, Unset):
            available_payment_methods = UNSET
        else:
            available_payment_methods = GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethods.from_dict(
                _available_payment_methods
            )

        _available_customer_payment_sources = d.pop("available_customer_payment_sources", UNSET)
        available_customer_payment_sources: Union[
            Unset, GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources
        ]
        if isinstance(_available_customer_payment_sources, Unset):
            available_customer_payment_sources = UNSET
        else:
            available_customer_payment_sources = (
                GETordersorderIdResponse200DataRelationshipsAvailableCustomerPaymentSources.from_dict(
                    _available_customer_payment_sources
                )
            )

        _available_free_skus = d.pop("available_free_skus", UNSET)
        available_free_skus: Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus]
        if isinstance(_available_free_skus, Unset):
            available_free_skus = UNSET
        else:
            available_free_skus = GETordersorderIdResponse200DataRelationshipsAvailableFreeSkus.from_dict(
                _available_free_skus
            )

        _available_free_bundles = d.pop("available_free_bundles", UNSET)
        available_free_bundles: Union[Unset, GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles]
        if isinstance(_available_free_bundles, Unset):
            available_free_bundles = UNSET
        else:
            available_free_bundles = GETordersorderIdResponse200DataRelationshipsAvailableFreeBundles.from_dict(
                _available_free_bundles
            )

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, GETordersorderIdResponse200DataRelationshipsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = GETordersorderIdResponse200DataRelationshipsPaymentMethod.from_dict(_payment_method)

        _payment_source = d.pop("payment_source", UNSET)
        payment_source: Union[Unset, GETordersorderIdResponse200DataRelationshipsPaymentSource]
        if isinstance(_payment_source, Unset):
            payment_source = UNSET
        else:
            payment_source = GETordersorderIdResponse200DataRelationshipsPaymentSource.from_dict(_payment_source)

        _line_items = d.pop("line_items", UNSET)
        line_items: Union[Unset, GETordersorderIdResponse200DataRelationshipsLineItems]
        if isinstance(_line_items, Unset):
            line_items = UNSET
        else:
            line_items = GETordersorderIdResponse200DataRelationshipsLineItems.from_dict(_line_items)

        _shipments = d.pop("shipments", UNSET)
        shipments: Union[Unset, GETordersorderIdResponse200DataRelationshipsShipments]
        if isinstance(_shipments, Unset):
            shipments = UNSET
        else:
            shipments = GETordersorderIdResponse200DataRelationshipsShipments.from_dict(_shipments)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, GETordersorderIdResponse200DataRelationshipsTransactions]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = GETordersorderIdResponse200DataRelationshipsTransactions.from_dict(_transactions)

        _authorizations = d.pop("authorizations", UNSET)
        authorizations: Union[Unset, GETordersorderIdResponse200DataRelationshipsAuthorizations]
        if isinstance(_authorizations, Unset):
            authorizations = UNSET
        else:
            authorizations = GETordersorderIdResponse200DataRelationshipsAuthorizations.from_dict(_authorizations)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, GETordersorderIdResponse200DataRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = GETordersorderIdResponse200DataRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, GETordersorderIdResponse200DataRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = GETordersorderIdResponse200DataRelationshipsVoids.from_dict(_voids)

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, GETordersorderIdResponse200DataRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = GETordersorderIdResponse200DataRelationshipsRefunds.from_dict(_refunds)

        _order_subscriptions = d.pop("order_subscriptions", UNSET)
        order_subscriptions: Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptions]
        if isinstance(_order_subscriptions, Unset):
            order_subscriptions = UNSET
        else:
            order_subscriptions = GETordersorderIdResponse200DataRelationshipsOrderSubscriptions.from_dict(
                _order_subscriptions
            )

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = GETordersorderIdResponse200DataRelationshipsOrderCopies.from_dict(_order_copies)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETordersorderIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETordersorderIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETordersorderIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETordersorderIdResponse200DataRelationshipsEvents.from_dict(_events)

        ge_tordersorder_id_response_200_data_relationships = cls(
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

        ge_tordersorder_id_response_200_data_relationships.additional_properties = d
        return ge_tordersorder_id_response_200_data_relationships

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
