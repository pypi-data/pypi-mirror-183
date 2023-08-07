from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_group_data_relationships_attachments import CustomerGroupDataRelationshipsAttachments
    from ..models.customer_group_data_relationships_customers import CustomerGroupDataRelationshipsCustomers
    from ..models.customer_group_data_relationships_markets import CustomerGroupDataRelationshipsMarkets


T = TypeVar("T", bound="CustomerGroupDataRelationships")


@attr.s(auto_attribs=True)
class CustomerGroupDataRelationships:
    """
    Attributes:
        customers (Union[Unset, CustomerGroupDataRelationshipsCustomers]):
        markets (Union[Unset, CustomerGroupDataRelationshipsMarkets]):
        attachments (Union[Unset, CustomerGroupDataRelationshipsAttachments]):
    """

    customers: Union[Unset, "CustomerGroupDataRelationshipsCustomers"] = UNSET
    markets: Union[Unset, "CustomerGroupDataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "CustomerGroupDataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customers, Unset):
            customers = self.customers.to_dict()

        markets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customers is not UNSET:
            field_dict["customers"] = customers
        if markets is not UNSET:
            field_dict["markets"] = markets
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_group_data_relationships_attachments import CustomerGroupDataRelationshipsAttachments
        from ..models.customer_group_data_relationships_customers import CustomerGroupDataRelationshipsCustomers
        from ..models.customer_group_data_relationships_markets import CustomerGroupDataRelationshipsMarkets

        d = src_dict.copy()
        _customers = d.pop("customers", UNSET)
        customers: Union[Unset, CustomerGroupDataRelationshipsCustomers]
        if isinstance(_customers, Unset):
            customers = UNSET
        else:
            customers = CustomerGroupDataRelationshipsCustomers.from_dict(_customers)

        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, CustomerGroupDataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = CustomerGroupDataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, CustomerGroupDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = CustomerGroupDataRelationshipsAttachments.from_dict(_attachments)

        customer_group_data_relationships = cls(
            customers=customers,
            markets=markets,
            attachments=attachments,
        )

        customer_group_data_relationships.additional_properties = d
        return customer_group_data_relationships

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
