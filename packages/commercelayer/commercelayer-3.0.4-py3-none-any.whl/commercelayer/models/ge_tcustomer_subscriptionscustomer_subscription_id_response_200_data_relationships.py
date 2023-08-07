from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships_customer import (
        GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships_events import (
        GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents,
    )


T = TypeVar("T", bound="GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer]):
        events (Union[Unset, GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents]):
    """

    customer: Union[Unset, "GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer"] = UNSET
    events: Union[Unset, "GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships_customer import (
            GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships_events import (
            GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomer.from_dict(
                _customer
            )

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsEvents.from_dict(_events)

        ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships = cls(
            customer=customer,
            events=events,
        )

        ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships.additional_properties = d
        return ge_tcustomer_subscriptionscustomer_subscription_id_response_200_data_relationships

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
