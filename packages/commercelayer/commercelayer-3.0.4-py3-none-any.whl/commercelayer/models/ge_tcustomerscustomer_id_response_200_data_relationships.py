from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_attachments import (
        GETcustomerscustomerIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_addresses import (
        GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_group import (
        GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_payment_sources import (
        GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_subscriptions import (
        GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_events import (
        GETcustomerscustomerIdResponse200DataRelationshipsEvents,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_order_subscriptions import (
        GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_orders import (
        GETcustomerscustomerIdResponse200DataRelationshipsOrders,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_returns import (
        GETcustomerscustomerIdResponse200DataRelationshipsReturns,
    )
    from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_sku_lists import (
        GETcustomerscustomerIdResponse200DataRelationshipsSkuLists,
    )


T = TypeVar("T", bound="GETcustomerscustomerIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcustomerscustomerIdResponse200DataRelationships:
    """
    Attributes:
        customer_group (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup]):
        customer_addresses (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses]):
        customer_payment_sources (Union[Unset,
            GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources]):
        customer_subscriptions (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions]):
        orders (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsOrders]):
        order_subscriptions (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions]):
        returns (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsReturns]):
        sku_lists (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsSkuLists]):
        attachments (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsEvents]):
    """

    customer_group: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup"] = UNSET
    customer_addresses: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses"] = UNSET
    customer_payment_sources: Union[
        Unset, "GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources"
    ] = UNSET
    customer_subscriptions: Union[
        Unset, "GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions"
    ] = UNSET
    orders: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsOrders"] = UNSET
    order_subscriptions: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions"] = UNSET
    returns: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsReturns"] = UNSET
    sku_lists: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsSkuLists"] = UNSET
    attachments: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETcustomerscustomerIdResponse200DataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_group, Unset):
            customer_group = self.customer_group.to_dict()

        customer_addresses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_addresses, Unset):
            customer_addresses = self.customer_addresses.to_dict()

        customer_payment_sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_payment_sources, Unset):
            customer_payment_sources = self.customer_payment_sources.to_dict()

        customer_subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_subscriptions, Unset):
            customer_subscriptions = self.customer_subscriptions.to_dict()

        orders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = self.orders.to_dict()

        order_subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_subscriptions, Unset):
            order_subscriptions = self.order_subscriptions.to_dict()

        returns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.returns, Unset):
            returns = self.returns.to_dict()

        sku_lists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_lists, Unset):
            sku_lists = self.sku_lists.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_group is not UNSET:
            field_dict["customer_group"] = customer_group
        if customer_addresses is not UNSET:
            field_dict["customer_addresses"] = customer_addresses
        if customer_payment_sources is not UNSET:
            field_dict["customer_payment_sources"] = customer_payment_sources
        if customer_subscriptions is not UNSET:
            field_dict["customer_subscriptions"] = customer_subscriptions
        if orders is not UNSET:
            field_dict["orders"] = orders
        if order_subscriptions is not UNSET:
            field_dict["order_subscriptions"] = order_subscriptions
        if returns is not UNSET:
            field_dict["returns"] = returns
        if sku_lists is not UNSET:
            field_dict["sku_lists"] = sku_lists
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_attachments import (
            GETcustomerscustomerIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_addresses import (
            GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_group import (
            GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_payment_sources import (
            GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_customer_subscriptions import (
            GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_events import (
            GETcustomerscustomerIdResponse200DataRelationshipsEvents,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_order_subscriptions import (
            GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_orders import (
            GETcustomerscustomerIdResponse200DataRelationshipsOrders,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_returns import (
            GETcustomerscustomerIdResponse200DataRelationshipsReturns,
        )
        from ..models.ge_tcustomerscustomer_id_response_200_data_relationships_sku_lists import (
            GETcustomerscustomerIdResponse200DataRelationshipsSkuLists,
        )

        d = src_dict.copy()
        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = GETcustomerscustomerIdResponse200DataRelationshipsCustomerGroup.from_dict(_customer_group)

        _customer_addresses = d.pop("customer_addresses", UNSET)
        customer_addresses: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses]
        if isinstance(_customer_addresses, Unset):
            customer_addresses = UNSET
        else:
            customer_addresses = GETcustomerscustomerIdResponse200DataRelationshipsCustomerAddresses.from_dict(
                _customer_addresses
            )

        _customer_payment_sources = d.pop("customer_payment_sources", UNSET)
        customer_payment_sources: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources]
        if isinstance(_customer_payment_sources, Unset):
            customer_payment_sources = UNSET
        else:
            customer_payment_sources = (
                GETcustomerscustomerIdResponse200DataRelationshipsCustomerPaymentSources.from_dict(
                    _customer_payment_sources
                )
            )

        _customer_subscriptions = d.pop("customer_subscriptions", UNSET)
        customer_subscriptions: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions]
        if isinstance(_customer_subscriptions, Unset):
            customer_subscriptions = UNSET
        else:
            customer_subscriptions = GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptions.from_dict(
                _customer_subscriptions
            )

        _orders = d.pop("orders", UNSET)
        orders: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsOrders]
        if isinstance(_orders, Unset):
            orders = UNSET
        else:
            orders = GETcustomerscustomerIdResponse200DataRelationshipsOrders.from_dict(_orders)

        _order_subscriptions = d.pop("order_subscriptions", UNSET)
        order_subscriptions: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions]
        if isinstance(_order_subscriptions, Unset):
            order_subscriptions = UNSET
        else:
            order_subscriptions = GETcustomerscustomerIdResponse200DataRelationshipsOrderSubscriptions.from_dict(
                _order_subscriptions
            )

        _returns = d.pop("returns", UNSET)
        returns: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsReturns]
        if isinstance(_returns, Unset):
            returns = UNSET
        else:
            returns = GETcustomerscustomerIdResponse200DataRelationshipsReturns.from_dict(_returns)

        _sku_lists = d.pop("sku_lists", UNSET)
        sku_lists: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsSkuLists]
        if isinstance(_sku_lists, Unset):
            sku_lists = UNSET
        else:
            sku_lists = GETcustomerscustomerIdResponse200DataRelationshipsSkuLists.from_dict(_sku_lists)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETcustomerscustomerIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETcustomerscustomerIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETcustomerscustomerIdResponse200DataRelationshipsEvents.from_dict(_events)

        ge_tcustomerscustomer_id_response_200_data_relationships = cls(
            customer_group=customer_group,
            customer_addresses=customer_addresses,
            customer_payment_sources=customer_payment_sources,
            customer_subscriptions=customer_subscriptions,
            orders=orders,
            order_subscriptions=order_subscriptions,
            returns=returns,
            sku_lists=sku_lists,
            attachments=attachments,
            events=events,
        )

        ge_tcustomerscustomer_id_response_200_data_relationships.additional_properties = d
        return ge_tcustomerscustomer_id_response_200_data_relationships

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
