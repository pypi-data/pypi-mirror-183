from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_address import (
        GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress,
    )
    from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_customer import (
        GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_events import (
        GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents,
    )


T = TypeVar("T", bound="GETcustomerAddressescustomerAddressIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcustomerAddressescustomerAddressIdResponse200DataRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer]):
        address (Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress]):
        events (Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents]):
    """

    customer: Union[Unset, "GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer"] = UNSET
    address: Union[Unset, "GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress"] = UNSET
    events: Union[Unset, "GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_address import (
            GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress,
        )
        from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_customer import (
            GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_addressescustomer_address_id_response_200_data_relationships_events import (
            GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsCustomer.from_dict(_customer)

        _address = d.pop("address", UNSET)
        address: Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsAddress.from_dict(_address)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETcustomerAddressescustomerAddressIdResponse200DataRelationshipsEvents.from_dict(_events)

        ge_tcustomer_addressescustomer_address_id_response_200_data_relationships = cls(
            customer=customer,
            address=address,
            events=events,
        )

        ge_tcustomer_addressescustomer_address_id_response_200_data_relationships.additional_properties = d
        return ge_tcustomer_addressescustomer_address_id_response_200_data_relationships

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
