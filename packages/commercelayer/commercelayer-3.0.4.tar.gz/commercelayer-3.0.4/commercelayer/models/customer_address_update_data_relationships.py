from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_address_update_data_relationships_address import (
        CustomerAddressUpdateDataRelationshipsAddress,
    )
    from ..models.customer_address_update_data_relationships_customer import (
        CustomerAddressUpdateDataRelationshipsCustomer,
    )


T = TypeVar("T", bound="CustomerAddressUpdateDataRelationships")


@attr.s(auto_attribs=True)
class CustomerAddressUpdateDataRelationships:
    """
    Attributes:
        customer (Union[Unset, CustomerAddressUpdateDataRelationshipsCustomer]):
        address (Union[Unset, CustomerAddressUpdateDataRelationshipsAddress]):
    """

    customer: Union[Unset, "CustomerAddressUpdateDataRelationshipsCustomer"] = UNSET
    address: Union[Unset, "CustomerAddressUpdateDataRelationshipsAddress"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_address_update_data_relationships_address import (
            CustomerAddressUpdateDataRelationshipsAddress,
        )
        from ..models.customer_address_update_data_relationships_customer import (
            CustomerAddressUpdateDataRelationshipsCustomer,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CustomerAddressUpdateDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CustomerAddressUpdateDataRelationshipsCustomer.from_dict(_customer)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CustomerAddressUpdateDataRelationshipsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CustomerAddressUpdateDataRelationshipsAddress.from_dict(_address)

        customer_address_update_data_relationships = cls(
            customer=customer,
            address=address,
        )

        customer_address_update_data_relationships.additional_properties = d
        return customer_address_update_data_relationships

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
