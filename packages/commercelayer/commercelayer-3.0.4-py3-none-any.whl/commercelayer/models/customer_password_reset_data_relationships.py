from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_password_reset_data_relationships_customer import (
        CustomerPasswordResetDataRelationshipsCustomer,
    )
    from ..models.customer_password_reset_data_relationships_events import CustomerPasswordResetDataRelationshipsEvents


T = TypeVar("T", bound="CustomerPasswordResetDataRelationships")


@attr.s(auto_attribs=True)
class CustomerPasswordResetDataRelationships:
    """
    Attributes:
        customer (Union[Unset, CustomerPasswordResetDataRelationshipsCustomer]):
        events (Union[Unset, CustomerPasswordResetDataRelationshipsEvents]):
    """

    customer: Union[Unset, "CustomerPasswordResetDataRelationshipsCustomer"] = UNSET
    events: Union[Unset, "CustomerPasswordResetDataRelationshipsEvents"] = UNSET
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
        from ..models.customer_password_reset_data_relationships_customer import (
            CustomerPasswordResetDataRelationshipsCustomer,
        )
        from ..models.customer_password_reset_data_relationships_events import (
            CustomerPasswordResetDataRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CustomerPasswordResetDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CustomerPasswordResetDataRelationshipsCustomer.from_dict(_customer)

        _events = d.pop("events", UNSET)
        events: Union[Unset, CustomerPasswordResetDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = CustomerPasswordResetDataRelationshipsEvents.from_dict(_events)

        customer_password_reset_data_relationships = cls(
            customer=customer,
            events=events,
        )

        customer_password_reset_data_relationships.additional_properties = d
        return customer_password_reset_data_relationships

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
