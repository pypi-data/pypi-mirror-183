from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_list_update_data_relationships_customer import SkuListUpdateDataRelationshipsCustomer


T = TypeVar("T", bound="SkuListUpdateDataRelationships")


@attr.s(auto_attribs=True)
class SkuListUpdateDataRelationships:
    """
    Attributes:
        customer (Union[Unset, SkuListUpdateDataRelationshipsCustomer]):
    """

    customer: Union[Unset, "SkuListUpdateDataRelationshipsCustomer"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_list_update_data_relationships_customer import SkuListUpdateDataRelationshipsCustomer

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, SkuListUpdateDataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = SkuListUpdateDataRelationshipsCustomer.from_dict(_customer)

        sku_list_update_data_relationships = cls(
            customer=customer,
        )

        sku_list_update_data_relationships.additional_properties = d
        return sku_list_update_data_relationships

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
