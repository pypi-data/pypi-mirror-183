from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_groups_response_200_data_item_relationships_attachments import (
        GETcustomerGroupsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tcustomer_groups_response_200_data_item_relationships_customers import (
        GETcustomerGroupsResponse200DataItemRelationshipsCustomers,
    )
    from ..models.ge_tcustomer_groups_response_200_data_item_relationships_markets import (
        GETcustomerGroupsResponse200DataItemRelationshipsMarkets,
    )


T = TypeVar("T", bound="GETcustomerGroupsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcustomerGroupsResponse200DataItemRelationships:
    """
    Attributes:
        customers (Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsCustomers]):
        markets (Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsMarkets]):
        attachments (Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsAttachments]):
    """

    customers: Union[Unset, "GETcustomerGroupsResponse200DataItemRelationshipsCustomers"] = UNSET
    markets: Union[Unset, "GETcustomerGroupsResponse200DataItemRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "GETcustomerGroupsResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tcustomer_groups_response_200_data_item_relationships_attachments import (
            GETcustomerGroupsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tcustomer_groups_response_200_data_item_relationships_customers import (
            GETcustomerGroupsResponse200DataItemRelationshipsCustomers,
        )
        from ..models.ge_tcustomer_groups_response_200_data_item_relationships_markets import (
            GETcustomerGroupsResponse200DataItemRelationshipsMarkets,
        )

        d = src_dict.copy()
        _customers = d.pop("customers", UNSET)
        customers: Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsCustomers]
        if isinstance(_customers, Unset):
            customers = UNSET
        else:
            customers = GETcustomerGroupsResponse200DataItemRelationshipsCustomers.from_dict(_customers)

        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = GETcustomerGroupsResponse200DataItemRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETcustomerGroupsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETcustomerGroupsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tcustomer_groups_response_200_data_item_relationships = cls(
            customers=customers,
            markets=markets,
            attachments=attachments,
        )

        ge_tcustomer_groups_response_200_data_item_relationships.additional_properties = d
        return ge_tcustomer_groups_response_200_data_item_relationships

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
