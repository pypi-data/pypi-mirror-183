from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcustomer_addresses_response_201_data_relationships_address import (
        POSTcustomerAddressesResponse201DataRelationshipsAddress,
    )
    from ..models.pos_tcustomer_addresses_response_201_data_relationships_customer import (
        POSTcustomerAddressesResponse201DataRelationshipsCustomer,
    )
    from ..models.pos_tcustomer_addresses_response_201_data_relationships_events import (
        POSTcustomerAddressesResponse201DataRelationshipsEvents,
    )


T = TypeVar("T", bound="POSTcustomerAddressesResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTcustomerAddressesResponse201DataRelationships:
    """
    Attributes:
        customer (Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsCustomer]):
        address (Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsAddress]):
        events (Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsEvents]):
    """

    customer: Union[Unset, "POSTcustomerAddressesResponse201DataRelationshipsCustomer"] = UNSET
    address: Union[Unset, "POSTcustomerAddressesResponse201DataRelationshipsAddress"] = UNSET
    events: Union[Unset, "POSTcustomerAddressesResponse201DataRelationshipsEvents"] = UNSET
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
        from ..models.pos_tcustomer_addresses_response_201_data_relationships_address import (
            POSTcustomerAddressesResponse201DataRelationshipsAddress,
        )
        from ..models.pos_tcustomer_addresses_response_201_data_relationships_customer import (
            POSTcustomerAddressesResponse201DataRelationshipsCustomer,
        )
        from ..models.pos_tcustomer_addresses_response_201_data_relationships_events import (
            POSTcustomerAddressesResponse201DataRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = POSTcustomerAddressesResponse201DataRelationshipsCustomer.from_dict(_customer)

        _address = d.pop("address", UNSET)
        address: Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = POSTcustomerAddressesResponse201DataRelationshipsAddress.from_dict(_address)

        _events = d.pop("events", UNSET)
        events: Union[Unset, POSTcustomerAddressesResponse201DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = POSTcustomerAddressesResponse201DataRelationshipsEvents.from_dict(_events)

        pos_tcustomer_addresses_response_201_data_relationships = cls(
            customer=customer,
            address=address,
            events=events,
        )

        pos_tcustomer_addresses_response_201_data_relationships.additional_properties = d
        return pos_tcustomer_addresses_response_201_data_relationships

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
