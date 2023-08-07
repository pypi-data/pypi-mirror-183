from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_address import (
        GETcustomerAddressesResponse200DataItemRelationshipsAddress,
    )
    from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_customer import (
        GETcustomerAddressesResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_events import (
        GETcustomerAddressesResponse200DataItemRelationshipsEvents,
    )


T = TypeVar("T", bound="GETcustomerAddressesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcustomerAddressesResponse200DataItemRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsCustomer]):
        address (Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsAddress]):
        events (Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsEvents]):
    """

    customer: Union[Unset, "GETcustomerAddressesResponse200DataItemRelationshipsCustomer"] = UNSET
    address: Union[Unset, "GETcustomerAddressesResponse200DataItemRelationshipsAddress"] = UNSET
    events: Union[Unset, "GETcustomerAddressesResponse200DataItemRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if address is not UNSET:
            field_dict["address"] = address
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_address import (
            GETcustomerAddressesResponse200DataItemRelationshipsAddress,
        )
        from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_customer import (
            GETcustomerAddressesResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_addresses_response_200_data_item_relationships_events import (
            GETcustomerAddressesResponse200DataItemRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerAddressesResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _address = d.pop("address", UNSET)
        address: Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GETcustomerAddressesResponse200DataItemRelationshipsAddress.from_dict(_address)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETcustomerAddressesResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETcustomerAddressesResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tcustomer_addresses_response_200_data_item_relationships = cls(
            customer=customer,
            address=address,
            events=events,
        )

        ge_tcustomer_addresses_response_200_data_item_relationships.additional_properties = d
        return ge_tcustomer_addresses_response_200_data_item_relationships

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
