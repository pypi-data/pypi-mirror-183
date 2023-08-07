from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_password_resets_response_200_data_item_relationships_customer import (
        GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_password_resets_response_200_data_item_relationships_events import (
        GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents,
    )


T = TypeVar("T", bound="GETcustomerPasswordResetsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcustomerPasswordResetsResponse200DataItemRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer]):
        events (Union[Unset, GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents]):
    """

    customer: Union[Unset, "GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer"] = UNSET
    events: Union[Unset, "GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_tcustomer_password_resets_response_200_data_item_relationships_customer import (
            GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_password_resets_response_200_data_item_relationships_events import (
            GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerPasswordResetsResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETcustomerPasswordResetsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tcustomer_password_resets_response_200_data_item_relationships = cls(
            customer=customer,
            events=events,
        )

        ge_tcustomer_password_resets_response_200_data_item_relationships.additional_properties = d
        return ge_tcustomer_password_resets_response_200_data_item_relationships

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
