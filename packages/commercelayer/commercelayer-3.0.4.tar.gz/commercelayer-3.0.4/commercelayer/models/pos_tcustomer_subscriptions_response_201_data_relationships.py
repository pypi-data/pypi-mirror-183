from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcustomer_subscriptions_response_201_data_relationships_customer import (
        POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer,
    )
    from ..models.pos_tcustomer_subscriptions_response_201_data_relationships_events import (
        POSTcustomerSubscriptionsResponse201DataRelationshipsEvents,
    )


T = TypeVar("T", bound="POSTcustomerSubscriptionsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTcustomerSubscriptionsResponse201DataRelationships:
    """
    Attributes:
        customer (Union[Unset, POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer]):
        events (Union[Unset, POSTcustomerSubscriptionsResponse201DataRelationshipsEvents]):
    """

    customer: Union[Unset, "POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer"] = UNSET
    events: Union[Unset, "POSTcustomerSubscriptionsResponse201DataRelationshipsEvents"] = UNSET
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
        from ..models.pos_tcustomer_subscriptions_response_201_data_relationships_customer import (
            POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer,
        )
        from ..models.pos_tcustomer_subscriptions_response_201_data_relationships_events import (
            POSTcustomerSubscriptionsResponse201DataRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = POSTcustomerSubscriptionsResponse201DataRelationshipsCustomer.from_dict(_customer)

        _events = d.pop("events", UNSET)
        events: Union[Unset, POSTcustomerSubscriptionsResponse201DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = POSTcustomerSubscriptionsResponse201DataRelationshipsEvents.from_dict(_events)

        pos_tcustomer_subscriptions_response_201_data_relationships = cls(
            customer=customer,
            events=events,
        )

        pos_tcustomer_subscriptions_response_201_data_relationships.additional_properties = d
        return pos_tcustomer_subscriptions_response_201_data_relationships

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
