from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.customer_address_create_data_relationships_address import (
        CustomerAddressCreateDataRelationshipsAddress,
    )
    from ..models.customer_address_create_data_relationships_customer import (
        CustomerAddressCreateDataRelationshipsCustomer,
    )


T = TypeVar("T", bound="CustomerAddressCreateDataRelationships")


@attr.s(auto_attribs=True)
class CustomerAddressCreateDataRelationships:
    """
    Attributes:
        customer (CustomerAddressCreateDataRelationshipsCustomer):
        address (CustomerAddressCreateDataRelationshipsAddress):
    """

    customer: "CustomerAddressCreateDataRelationshipsCustomer"
    address: "CustomerAddressCreateDataRelationshipsAddress"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer = self.customer.to_dict()

        address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_address_create_data_relationships_address import (
            CustomerAddressCreateDataRelationshipsAddress,
        )
        from ..models.customer_address_create_data_relationships_customer import (
            CustomerAddressCreateDataRelationshipsCustomer,
        )

        d = src_dict.copy()
        customer = CustomerAddressCreateDataRelationshipsCustomer.from_dict(d.pop("customer"))

        address = CustomerAddressCreateDataRelationshipsAddress.from_dict(d.pop("address"))

        customer_address_create_data_relationships = cls(
            customer=customer,
            address=address,
        )

        customer_address_create_data_relationships.additional_properties = d
        return customer_address_create_data_relationships

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
