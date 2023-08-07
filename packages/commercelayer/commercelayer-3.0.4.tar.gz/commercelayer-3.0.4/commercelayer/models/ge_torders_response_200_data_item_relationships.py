from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torders_response_200_data_item_relationships_attachments import (
        GETordersResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_torders_response_200_data_item_relationships_authorizations import (
        GETordersResponse200DataItemRelationshipsAuthorizations,
    )
    from ..models.ge_torders_response_200_data_item_relationships_available_customer_payment_sources import (
        GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources,
    )
    from ..models.ge_torders_response_200_data_item_relationships_available_free_bundles import (
        GETordersResponse200DataItemRelationshipsAvailableFreeBundles,
    )
    from ..models.ge_torders_response_200_data_item_relationships_available_free_skus import (
        GETordersResponse200DataItemRelationshipsAvailableFreeSkus,
    )
    from ..models.ge_torders_response_200_data_item_relationships_available_payment_methods import (
        GETordersResponse200DataItemRelationshipsAvailablePaymentMethods,
    )
    from ..models.ge_torders_response_200_data_item_relationships_billing_address import (
        GETordersResponse200DataItemRelationshipsBillingAddress,
    )
    from ..models.ge_torders_response_200_data_item_relationships_captures import (
        GETordersResponse200DataItemRelationshipsCaptures,
    )
    from ..models.ge_torders_response_200_data_item_relationships_customer import (
        GETordersResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_torders_response_200_data_item_relationships_events import (
        GETordersResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_torders_response_200_data_item_relationships_line_items import (
        GETordersResponse200DataItemRelationshipsLineItems,
    )
    from ..models.ge_torders_response_200_data_item_relationships_market import (
        GETordersResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_torders_response_200_data_item_relationships_order_copies import (
        GETordersResponse200DataItemRelationshipsOrderCopies,
    )
    from ..models.ge_torders_response_200_data_item_relationships_order_subscriptions import (
        GETordersResponse200DataItemRelationshipsOrderSubscriptions,
    )
    from ..models.ge_torders_response_200_data_item_relationships_payment_method import (
        GETordersResponse200DataItemRelationshipsPaymentMethod,
    )
    from ..models.ge_torders_response_200_data_item_relationships_payment_source import (
        GETordersResponse200DataItemRelationshipsPaymentSource,
    )
    from ..models.ge_torders_response_200_data_item_relationships_refunds import (
        GETordersResponse200DataItemRelationshipsRefunds,
    )
    from ..models.ge_torders_response_200_data_item_relationships_shipments import (
        GETordersResponse200DataItemRelationshipsShipments,
    )
    from ..models.ge_torders_response_200_data_item_relationships_shipping_address import (
        GETordersResponse200DataItemRelationshipsShippingAddress,
    )
    from ..models.ge_torders_response_200_data_item_relationships_transactions import (
        GETordersResponse200DataItemRelationshipsTransactions,
    )
    from ..models.ge_torders_response_200_data_item_relationships_voids import (
        GETordersResponse200DataItemRelationshipsVoids,
    )


T = TypeVar("T", bound="GETordersResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETordersResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETordersResponse200DataItemRelationshipsMarket]):
        customer (Union[Unset, GETordersResponse200DataItemRelationshipsCustomer]):
        shipping_address (Union[Unset, GETordersResponse200DataItemRelationshipsShippingAddress]):
        billing_address (Union[Unset, GETordersResponse200DataItemRelationshipsBillingAddress]):
        available_payment_methods (Union[Unset, GETordersResponse200DataItemRelationshipsAvailablePaymentMethods]):
        available_customer_payment_sources (Union[Unset,
            GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources]):
        available_free_skus (Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkus]):
        available_free_bundles (Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeBundles]):
        payment_method (Union[Unset, GETordersResponse200DataItemRelationshipsPaymentMethod]):
        payment_source (Union[Unset, GETordersResponse200DataItemRelationshipsPaymentSource]):
        line_items (Union[Unset, GETordersResponse200DataItemRelationshipsLineItems]):
        shipments (Union[Unset, GETordersResponse200DataItemRelationshipsShipments]):
        transactions (Union[Unset, GETordersResponse200DataItemRelationshipsTransactions]):
        authorizations (Union[Unset, GETordersResponse200DataItemRelationshipsAuthorizations]):
        captures (Union[Unset, GETordersResponse200DataItemRelationshipsCaptures]):
        voids (Union[Unset, GETordersResponse200DataItemRelationshipsVoids]):
        refunds (Union[Unset, GETordersResponse200DataItemRelationshipsRefunds]):
        order_subscriptions (Union[Unset, GETordersResponse200DataItemRelationshipsOrderSubscriptions]):
        order_copies (Union[Unset, GETordersResponse200DataItemRelationshipsOrderCopies]):
        attachments (Union[Unset, GETordersResponse200DataItemRelationshipsAttachments]):
        events (Union[Unset, GETordersResponse200DataItemRelationshipsEvents]):
    """

    market: Union[Unset, "GETordersResponse200DataItemRelationshipsMarket"] = UNSET
    customer: Union[Unset, "GETordersResponse200DataItemRelationshipsCustomer"] = UNSET
    shipping_address: Union[Unset, "GETordersResponse200DataItemRelationshipsShippingAddress"] = UNSET
    billing_address: Union[Unset, "GETordersResponse200DataItemRelationshipsBillingAddress"] = UNSET
    available_payment_methods: Union[Unset, "GETordersResponse200DataItemRelationshipsAvailablePaymentMethods"] = UNSET
    available_customer_payment_sources: Union[
        Unset, "GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources"
    ] = UNSET
    available_free_skus: Union[Unset, "GETordersResponse200DataItemRelationshipsAvailableFreeSkus"] = UNSET
    available_free_bundles: Union[Unset, "GETordersResponse200DataItemRelationshipsAvailableFreeBundles"] = UNSET
    payment_method: Union[Unset, "GETordersResponse200DataItemRelationshipsPaymentMethod"] = UNSET
    payment_source: Union[Unset, "GETordersResponse200DataItemRelationshipsPaymentSource"] = UNSET
    line_items: Union[Unset, "GETordersResponse200DataItemRelationshipsLineItems"] = UNSET
    shipments: Union[Unset, "GETordersResponse200DataItemRelationshipsShipments"] = UNSET
    transactions: Union[Unset, "GETordersResponse200DataItemRelationshipsTransactions"] = UNSET
    authorizations: Union[Unset, "GETordersResponse200DataItemRelationshipsAuthorizations"] = UNSET
    captures: Union[Unset, "GETordersResponse200DataItemRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "GETordersResponse200DataItemRelationshipsVoids"] = UNSET
    refunds: Union[Unset, "GETordersResponse200DataItemRelationshipsRefunds"] = UNSET
    order_subscriptions: Union[Unset, "GETordersResponse200DataItemRelationshipsOrderSubscriptions"] = UNSET
    order_copies: Union[Unset, "GETordersResponse200DataItemRelationshipsOrderCopies"] = UNSET
    attachments: Union[Unset, "GETordersResponse200DataItemRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETordersResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_torders_response_200_data_item_relationships_attachments import (
            GETordersResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_torders_response_200_data_item_relationships_authorizations import (
            GETordersResponse200DataItemRelationshipsAuthorizations,
        )
        from ..models.ge_torders_response_200_data_item_relationships_available_customer_payment_sources import (
            GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources,
        )
        from ..models.ge_torders_response_200_data_item_relationships_available_free_bundles import (
            GETordersResponse200DataItemRelationshipsAvailableFreeBundles,
        )
        from ..models.ge_torders_response_200_data_item_relationships_available_free_skus import (
            GETordersResponse200DataItemRelationshipsAvailableFreeSkus,
        )
        from ..models.ge_torders_response_200_data_item_relationships_available_payment_methods import (
            GETordersResponse200DataItemRelationshipsAvailablePaymentMethods,
        )
        from ..models.ge_torders_response_200_data_item_relationships_billing_address import (
            GETordersResponse200DataItemRelationshipsBillingAddress,
        )
        from ..models.ge_torders_response_200_data_item_relationships_captures import (
            GETordersResponse200DataItemRelationshipsCaptures,
        )
        from ..models.ge_torders_response_200_data_item_relationships_customer import (
            GETordersResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_torders_response_200_data_item_relationships_events import (
            GETordersResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_torders_response_200_data_item_relationships_line_items import (
            GETordersResponse200DataItemRelationshipsLineItems,
        )
        from ..models.ge_torders_response_200_data_item_relationships_market import (
            GETordersResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_torders_response_200_data_item_relationships_order_copies import (
            GETordersResponse200DataItemRelationshipsOrderCopies,
        )
        from ..models.ge_torders_response_200_data_item_relationships_order_subscriptions import (
            GETordersResponse200DataItemRelationshipsOrderSubscriptions,
        )
        from ..models.ge_torders_response_200_data_item_relationships_payment_method import (
            GETordersResponse200DataItemRelationshipsPaymentMethod,
        )
        from ..models.ge_torders_response_200_data_item_relationships_payment_source import (
            GETordersResponse200DataItemRelationshipsPaymentSource,
        )
        from ..models.ge_torders_response_200_data_item_relationships_refunds import (
            GETordersResponse200DataItemRelationshipsRefunds,
        )
        from ..models.ge_torders_response_200_data_item_relationships_shipments import (
            GETordersResponse200DataItemRelationshipsShipments,
        )
        from ..models.ge_torders_response_200_data_item_relationships_shipping_address import (
            GETordersResponse200DataItemRelationshipsShippingAddress,
        )
        from ..models.ge_torders_response_200_data_item_relationships_transactions import (
            GETordersResponse200DataItemRelationshipsTransactions,
        )
        from ..models.ge_torders_response_200_data_item_relationships_voids import (
            GETordersResponse200DataItemRelationshipsVoids,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETordersResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETordersResponse200DataItemRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETordersResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETordersResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, GETordersResponse200DataItemRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = GETordersResponse200DataItemRelationshipsShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, GETordersResponse200DataItemRelationshipsBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = GETordersResponse200DataItemRelationshipsBillingAddress.from_dict(_billing_address)

        _available_payment_methods = d.pop("available_payment_methods", UNSET)
        available_payment_methods: Union[Unset, GETordersResponse200DataItemRelationshipsAvailablePaymentMethods]
        if isinstance(_available_payment_methods, Unset):
            available_payment_methods = UNSET
        else:
            available_payment_methods = GETordersResponse200DataItemRelationshipsAvailablePaymentMethods.from_dict(
                _available_payment_methods
            )

        _available_customer_payment_sources = d.pop("available_customer_payment_sources", UNSET)
        available_customer_payment_sources: Union[
            Unset, GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources
        ]
        if isinstance(_available_customer_payment_sources, Unset):
            available_customer_payment_sources = UNSET
        else:
            available_customer_payment_sources = (
                GETordersResponse200DataItemRelationshipsAvailableCustomerPaymentSources.from_dict(
                    _available_customer_payment_sources
                )
            )

        _available_free_skus = d.pop("available_free_skus", UNSET)
        available_free_skus: Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeSkus]
        if isinstance(_available_free_skus, Unset):
            available_free_skus = UNSET
        else:
            available_free_skus = GETordersResponse200DataItemRelationshipsAvailableFreeSkus.from_dict(
                _available_free_skus
            )

        _available_free_bundles = d.pop("available_free_bundles", UNSET)
        available_free_bundles: Union[Unset, GETordersResponse200DataItemRelationshipsAvailableFreeBundles]
        if isinstance(_available_free_bundles, Unset):
            available_free_bundles = UNSET
        else:
            available_free_bundles = GETordersResponse200DataItemRelationshipsAvailableFreeBundles.from_dict(
                _available_free_bundles
            )

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, GETordersResponse200DataItemRelationshipsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = GETordersResponse200DataItemRelationshipsPaymentMethod.from_dict(_payment_method)

        _payment_source = d.pop("payment_source", UNSET)
        payment_source: Union[Unset, GETordersResponse200DataItemRelationshipsPaymentSource]
        if isinstance(_payment_source, Unset):
            payment_source = UNSET
        else:
            payment_source = GETordersResponse200DataItemRelationshipsPaymentSource.from_dict(_payment_source)

        _line_items = d.pop("line_items", UNSET)
        line_items: Union[Unset, GETordersResponse200DataItemRelationshipsLineItems]
        if isinstance(_line_items, Unset):
            line_items = UNSET
        else:
            line_items = GETordersResponse200DataItemRelationshipsLineItems.from_dict(_line_items)

        _shipments = d.pop("shipments", UNSET)
        shipments: Union[Unset, GETordersResponse200DataItemRelationshipsShipments]
        if isinstance(_shipments, Unset):
            shipments = UNSET
        else:
            shipments = GETordersResponse200DataItemRelationshipsShipments.from_dict(_shipments)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, GETordersResponse200DataItemRelationshipsTransactions]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = GETordersResponse200DataItemRelationshipsTransactions.from_dict(_transactions)

        _authorizations = d.pop("authorizations", UNSET)
        authorizations: Union[Unset, GETordersResponse200DataItemRelationshipsAuthorizations]
        if isinstance(_authorizations, Unset):
            authorizations = UNSET
        else:
            authorizations = GETordersResponse200DataItemRelationshipsAuthorizations.from_dict(_authorizations)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, GETordersResponse200DataItemRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = GETordersResponse200DataItemRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, GETordersResponse200DataItemRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = GETordersResponse200DataItemRelationshipsVoids.from_dict(_voids)

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, GETordersResponse200DataItemRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = GETordersResponse200DataItemRelationshipsRefunds.from_dict(_refunds)

        _order_subscriptions = d.pop("order_subscriptions", UNSET)
        order_subscriptions: Union[Unset, GETordersResponse200DataItemRelationshipsOrderSubscriptions]
        if isinstance(_order_subscriptions, Unset):
            order_subscriptions = UNSET
        else:
            order_subscriptions = GETordersResponse200DataItemRelationshipsOrderSubscriptions.from_dict(
                _order_subscriptions
            )

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, GETordersResponse200DataItemRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = GETordersResponse200DataItemRelationshipsOrderCopies.from_dict(_order_copies)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETordersResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETordersResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETordersResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETordersResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_torders_response_200_data_item_relationships = cls(
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

        ge_torders_response_200_data_item_relationships.additional_properties = d
        return ge_torders_response_200_data_item_relationships

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
