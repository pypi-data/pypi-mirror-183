from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_create_data_relationships_customer_group import CustomerCreateDataRelationshipsCustomerGroup


T = TypeVar("T", bound="CustomerCreateDataRelationships")


@attr.s(auto_attribs=True)
class CustomerCreateDataRelationships:
    """
    Attributes:
        customer_group (Union[Unset, CustomerCreateDataRelationshipsCustomerGroup]):
    """

    customer_group: Union[Unset, "CustomerCreateDataRelationshipsCustomerGroup"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_group, Unset):
            customer_group = self.customer_group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_group is not UNSET:
            field_dict["customer_group"] = customer_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_create_data_relationships_customer_group import (
            CustomerCreateDataRelationshipsCustomerGroup,
        )

        d = src_dict.copy()
        _customer_group = d.pop("customer_group", UNSET)
        customer_group: Union[Unset, CustomerCreateDataRelationshipsCustomerGroup]
        if isinstance(_customer_group, Unset):
            customer_group = UNSET
        else:
            customer_group = CustomerCreateDataRelationshipsCustomerGroup.from_dict(_customer_group)

        customer_create_data_relationships = cls(
            customer_group=customer_group,
        )

        customer_create_data_relationships.additional_properties = d
        return customer_create_data_relationships

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
