from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torders_response_201_data_relationships_attachments import (
        POSTordersResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_torders_response_201_data_relationships_authorizations import (
        POSTordersResponse201DataRelationshipsAuthorizations,
    )
    from ..models.pos_torders_response_201_data_relationships_available_customer_payment_sources import (
        POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources,
    )
    from ..models.pos_torders_response_201_data_relationships_available_free_bundles import (
        POSTordersResponse201DataRelationshipsAvailableFreeBundles,
    )
    from ..models.pos_torders_response_201_data_relationships_available_free_skus import (
        POSTordersResponse201DataRelationshipsAvailableFreeSkus,
    )
    from ..models.pos_torders_response_201_data_relationships_available_payment_methods import (
        POSTordersResponse201DataRelationshipsAvailablePaymentMethods,
    )
    from ..models.pos_torders_response_201_data_relationships_billing_address import (
        POSTordersResponse201DataRelationshipsBillingAddress,
    )
    from ..models.pos_torders_response_201_data_relationships_captures import (
        POSTordersResponse201DataRelationshipsCaptures,
    )
    from ..models.pos_torders_response_201_data_relationships_customer import (
        POSTordersResponse201DataRelationshipsCustomer,
    )
    from ..models.pos_torders_response_201_data_relationships_events import POSTordersResponse201DataRelationshipsEvents
    from ..models.pos_torders_response_201_data_relationships_line_items import (
        POSTordersResponse201DataRelationshipsLineItems,
    )
    from ..models.pos_torders_response_201_data_relationships_market import POSTordersResponse201DataRelationshipsMarket
    from ..models.pos_torders_response_201_data_relationships_order_copies import (
        POSTordersResponse201DataRelationshipsOrderCopies,
    )
    from ..models.pos_torders_response_201_data_relationships_order_subscriptions import (
        POSTordersResponse201DataRelationshipsOrderSubscriptions,
    )
    from ..models.pos_torders_response_201_data_relationships_payment_method import (
        POSTordersResponse201DataRelationshipsPaymentMethod,
    )
    from ..models.pos_torders_response_201_data_relationships_payment_source import (
        POSTordersResponse201DataRelationshipsPaymentSource,
    )
    from ..models.pos_torders_response_201_data_relationships_refunds import (
        POSTordersResponse201DataRelationshipsRefunds,
    )
    from ..models.pos_torders_response_201_data_relationships_shipments import (
        POSTordersResponse201DataRelationshipsShipments,
    )
    from ..models.pos_torders_response_201_data_relationships_shipping_address import (
        POSTordersResponse201DataRelationshipsShippingAddress,
    )
    from ..models.pos_torders_response_201_data_relationships_transactions import (
        POSTordersResponse201DataRelationshipsTransactions,
    )
    from ..models.pos_torders_response_201_data_relationships_voids import POSTordersResponse201DataRelationshipsVoids


T = TypeVar("T", bound="POSTordersResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTordersResponse201DataRelationships:
    """
    Attributes:
        market (Union[Unset, POSTordersResponse201DataRelationshipsMarket]):
        customer (Union[Unset, POSTordersResponse201DataRelationshipsCustomer]):
        shipping_address (Union[Unset, POSTordersResponse201DataRelationshipsShippingAddress]):
        billing_address (Union[Unset, POSTordersResponse201DataRelationshipsBillingAddress]):
        available_payment_methods (Union[Unset, POSTordersResponse201DataRelationshipsAvailablePaymentMethods]):
        available_customer_payment_sources (Union[Unset,
            POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources]):
        available_free_skus (Union[Unset, POSTordersResponse201DataRelationshipsAvailableFreeSkus]):
        available_free_bundles (Union[Unset, POSTordersResponse201DataRelationshipsAvailableFreeBundles]):
        payment_method (Union[Unset, POSTordersResponse201DataRelationshipsPaymentMethod]):
        payment_source (Union[Unset, POSTordersResponse201DataRelationshipsPaymentSource]):
        line_items (Union[Unset, POSTordersResponse201DataRelationshipsLineItems]):
        shipments (Union[Unset, POSTordersResponse201DataRelationshipsShipments]):
        transactions (Union[Unset, POSTordersResponse201DataRelationshipsTransactions]):
        authorizations (Union[Unset, POSTordersResponse201DataRelationshipsAuthorizations]):
        captures (Union[Unset, POSTordersResponse201DataRelationshipsCaptures]):
        voids (Union[Unset, POSTordersResponse201DataRelationshipsVoids]):
        refunds (Union[Unset, POSTordersResponse201DataRelationshipsRefunds]):
        order_subscriptions (Union[Unset, POSTordersResponse201DataRelationshipsOrderSubscriptions]):
        order_copies (Union[Unset, POSTordersResponse201DataRelationshipsOrderCopies]):
        attachments (Union[Unset, POSTordersResponse201DataRelationshipsAttachments]):
        events (Union[Unset, POSTordersResponse201DataRelationshipsEvents]):
    """

    market: Union[Unset, "POSTordersResponse201DataRelationshipsMarket"] = UNSET
    customer: Union[Unset, "POSTordersResponse201DataRelationshipsCustomer"] = UNSET
    shipping_address: Union[Unset, "POSTordersResponse201DataRelationshipsShippingAddress"] = UNSET
    billing_address: Union[Unset, "POSTordersResponse201DataRelationshipsBillingAddress"] = UNSET
    available_payment_methods: Union[Unset, "POSTordersResponse201DataRelationshipsAvailablePaymentMethods"] = UNSET
    available_customer_payment_sources: Union[
        Unset, "POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources"
    ] = UNSET
    available_free_skus: Union[Unset, "POSTordersResponse201DataRelationshipsAvailableFreeSkus"] = UNSET
    available_free_bundles: Union[Unset, "POSTordersResponse201DataRelationshipsAvailableFreeBundles"] = UNSET
    payment_method: Union[Unset, "POSTordersResponse201DataRelationshipsPaymentMethod"] = UNSET
    payment_source: Union[Unset, "POSTordersResponse201DataRelationshipsPaymentSource"] = UNSET
    line_items: Union[Unset, "POSTordersResponse201DataRelationshipsLineItems"] = UNSET
    shipments: Union[Unset, "POSTordersResponse201DataRelationshipsShipments"] = UNSET
    transactions: Union[Unset, "POSTordersResponse201DataRelationshipsTransactions"] = UNSET
    authorizations: Union[Unset, "POSTordersResponse201DataRelationshipsAuthorizations"] = UNSET
    captures: Union[Unset, "POSTordersResponse201DataRelationshipsCaptures"] = UNSET
    voids: Union[Unset, "POSTordersResponse201DataRelationshipsVoids"] = UNSET
    refunds: Union[Unset, "POSTordersResponse201DataRelationshipsRefunds"] = UNSET
    order_subscriptions: Union[Unset, "POSTordersResponse201DataRelationshipsOrderSubscriptions"] = UNSET
    order_copies: Union[Unset, "POSTordersResponse201DataRelationshipsOrderCopies"] = UNSET
    attachments: Union[Unset, "POSTordersResponse201DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "POSTordersResponse201DataRelationshipsEvents"] = UNSET
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
        from ..models.pos_torders_response_201_data_relationships_attachments import (
            POSTordersResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_torders_response_201_data_relationships_authorizations import (
            POSTordersResponse201DataRelationshipsAuthorizations,
        )
        from ..models.pos_torders_response_201_data_relationships_available_customer_payment_sources import (
            POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources,
        )
        from ..models.pos_torders_response_201_data_relationships_available_free_bundles import (
            POSTordersResponse201DataRelationshipsAvailableFreeBundles,
        )
        from ..models.pos_torders_response_201_data_relationships_available_free_skus import (
            POSTordersResponse201DataRelationshipsAvailableFreeSkus,
        )
        from ..models.pos_torders_response_201_data_relationships_available_payment_methods import (
            POSTordersResponse201DataRelationshipsAvailablePaymentMethods,
        )
        from ..models.pos_torders_response_201_data_relationships_billing_address import (
            POSTordersResponse201DataRelationshipsBillingAddress,
        )
        from ..models.pos_torders_response_201_data_relationships_captures import (
            POSTordersResponse201DataRelationshipsCaptures,
        )
        from ..models.pos_torders_response_201_data_relationships_customer import (
            POSTordersResponse201DataRelationshipsCustomer,
        )
        from ..models.pos_torders_response_201_data_relationships_events import (
            POSTordersResponse201DataRelationshipsEvents,
        )
        from ..models.pos_torders_response_201_data_relationships_line_items import (
            POSTordersResponse201DataRelationshipsLineItems,
        )
        from ..models.pos_torders_response_201_data_relationships_market import (
            POSTordersResponse201DataRelationshipsMarket,
        )
        from ..models.pos_torders_response_201_data_relationships_order_copies import (
            POSTordersResponse201DataRelationshipsOrderCopies,
        )
        from ..models.pos_torders_response_201_data_relationships_order_subscriptions import (
            POSTordersResponse201DataRelationshipsOrderSubscriptions,
        )
        from ..models.pos_torders_response_201_data_relationships_payment_method import (
            POSTordersResponse201DataRelationshipsPaymentMethod,
        )
        from ..models.pos_torders_response_201_data_relationships_payment_source import (
            POSTordersResponse201DataRelationshipsPaymentSource,
        )
        from ..models.pos_torders_response_201_data_relationships_refunds import (
            POSTordersResponse201DataRelationshipsRefunds,
        )
        from ..models.pos_torders_response_201_data_relationships_shipments import (
            POSTordersResponse201DataRelationshipsShipments,
        )
        from ..models.pos_torders_response_201_data_relationships_shipping_address import (
            POSTordersResponse201DataRelationshipsShippingAddress,
        )
        from ..models.pos_torders_response_201_data_relationships_transactions import (
            POSTordersResponse201DataRelationshipsTransactions,
        )
        from ..models.pos_torders_response_201_data_relationships_voids import (
            POSTordersResponse201DataRelationshipsVoids,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, POSTordersResponse201DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = POSTordersResponse201DataRelationshipsMarket.from_dict(_market)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, POSTordersResponse201DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = POSTordersResponse201DataRelationshipsCustomer.from_dict(_customer)

        _shipping_address = d.pop("shipping_address", UNSET)
        shipping_address: Union[Unset, POSTordersResponse201DataRelationshipsShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = POSTordersResponse201DataRelationshipsShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, POSTordersResponse201DataRelationshipsBillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = POSTordersResponse201DataRelationshipsBillingAddress.from_dict(_billing_address)

        _available_payment_methods = d.pop("available_payment_methods", UNSET)
        available_payment_methods: Union[Unset, POSTordersResponse201DataRelationshipsAvailablePaymentMethods]
        if isinstance(_available_payment_methods, Unset):
            available_payment_methods = UNSET
        else:
            available_payment_methods = POSTordersResponse201DataRelationshipsAvailablePaymentMethods.from_dict(
                _available_payment_methods
            )

        _available_customer_payment_sources = d.pop("available_customer_payment_sources", UNSET)
        available_customer_payment_sources: Union[
            Unset, POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources
        ]
        if isinstance(_available_customer_payment_sources, Unset):
            available_customer_payment_sources = UNSET
        else:
            available_customer_payment_sources = (
                POSTordersResponse201DataRelationshipsAvailableCustomerPaymentSources.from_dict(
                    _available_customer_payment_sources
                )
            )

        _available_free_skus = d.pop("available_free_skus", UNSET)
        available_free_skus: Union[Unset, POSTordersResponse201DataRelationshipsAvailableFreeSkus]
        if isinstance(_available_free_skus, Unset):
            available_free_skus = UNSET
        else:
            available_free_skus = POSTordersResponse201DataRelationshipsAvailableFreeSkus.from_dict(
                _available_free_skus
            )

        _available_free_bundles = d.pop("available_free_bundles", UNSET)
        available_free_bundles: Union[Unset, POSTordersResponse201DataRelationshipsAvailableFreeBundles]
        if isinstance(_available_free_bundles, Unset):
            available_free_bundles = UNSET
        else:
            available_free_bundles = POSTordersResponse201DataRelationshipsAvailableFreeBundles.from_dict(
                _available_free_bundles
            )

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, POSTordersResponse201DataRelationshipsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = POSTordersResponse201DataRelationshipsPaymentMethod.from_dict(_payment_method)

        _payment_source = d.pop("payment_source", UNSET)
        payment_source: Union[Unset, POSTordersResponse201DataRelationshipsPaymentSource]
        if isinstance(_payment_source, Unset):
            payment_source = UNSET
        else:
            payment_source = POSTordersResponse201DataRelationshipsPaymentSource.from_dict(_payment_source)

        _line_items = d.pop("line_items", UNSET)
        line_items: Union[Unset, POSTordersResponse201DataRelationshipsLineItems]
        if isinstance(_line_items, Unset):
            line_items = UNSET
        else:
            line_items = POSTordersResponse201DataRelationshipsLineItems.from_dict(_line_items)

        _shipments = d.pop("shipments", UNSET)
        shipments: Union[Unset, POSTordersResponse201DataRelationshipsShipments]
        if isinstance(_shipments, Unset):
            shipments = UNSET
        else:
            shipments = POSTordersResponse201DataRelationshipsShipments.from_dict(_shipments)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, POSTordersResponse201DataRelationshipsTransactions]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = POSTordersResponse201DataRelationshipsTransactions.from_dict(_transactions)

        _authorizations = d.pop("authorizations", UNSET)
        authorizations: Union[Unset, POSTordersResponse201DataRelationshipsAuthorizations]
        if isinstance(_authorizations, Unset):
            authorizations = UNSET
        else:
            authorizations = POSTordersResponse201DataRelationshipsAuthorizations.from_dict(_authorizations)

        _captures = d.pop("captures", UNSET)
        captures: Union[Unset, POSTordersResponse201DataRelationshipsCaptures]
        if isinstance(_captures, Unset):
            captures = UNSET
        else:
            captures = POSTordersResponse201DataRelationshipsCaptures.from_dict(_captures)

        _voids = d.pop("voids", UNSET)
        voids: Union[Unset, POSTordersResponse201DataRelationshipsVoids]
        if isinstance(_voids, Unset):
            voids = UNSET
        else:
            voids = POSTordersResponse201DataRelationshipsVoids.from_dict(_voids)

        _refunds = d.pop("refunds", UNSET)
        refunds: Union[Unset, POSTordersResponse201DataRelationshipsRefunds]
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = POSTordersResponse201DataRelationshipsRefunds.from_dict(_refunds)

        _order_subscriptions = d.pop("order_subscriptions", UNSET)
        order_subscriptions: Union[Unset, POSTordersResponse201DataRelationshipsOrderSubscriptions]
        if isinstance(_order_subscriptions, Unset):
            order_subscriptions = UNSET
        else:
            order_subscriptions = POSTordersResponse201DataRelationshipsOrderSubscriptions.from_dict(
                _order_subscriptions
            )

        _order_copies = d.pop("order_copies", UNSET)
        order_copies: Union[Unset, POSTordersResponse201DataRelationshipsOrderCopies]
        if isinstance(_order_copies, Unset):
            order_copies = UNSET
        else:
            order_copies = POSTordersResponse201DataRelationshipsOrderCopies.from_dict(_order_copies)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTordersResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTordersResponse201DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, POSTordersResponse201DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = POSTordersResponse201DataRelationshipsEvents.from_dict(_events)

        pos_torders_response_201_data_relationships = cls(
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

        pos_torders_response_201_data_relationships.additional_properties = d
        return pos_torders_response_201_data_relationships

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
