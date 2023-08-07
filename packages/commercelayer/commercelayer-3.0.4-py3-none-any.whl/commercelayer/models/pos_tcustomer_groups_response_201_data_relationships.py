from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcustomer_groups_response_201_data_relationships_attachments import (
        POSTcustomerGroupsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tcustomer_groups_response_201_data_relationships_customers import (
        POSTcustomerGroupsResponse201DataRelationshipsCustomers,
    )
    from ..models.pos_tcustomer_groups_response_201_data_relationships_markets import (
        POSTcustomerGroupsResponse201DataRelationshipsMarkets,
    )


T = TypeVar("T", bound="POSTcustomerGroupsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTcustomerGroupsResponse201DataRelationships:
    """
    Attributes:
        customers (Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsCustomers]):
        markets (Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsMarkets]):
        attachments (Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsAttachments]):
    """

    customers: Union[Unset, "POSTcustomerGroupsResponse201DataRelationshipsCustomers"] = UNSET
    markets: Union[Unset, "POSTcustomerGroupsResponse201DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "POSTcustomerGroupsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tcustomer_groups_response_201_data_relationships_attachments import (
            POSTcustomerGroupsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tcustomer_groups_response_201_data_relationships_customers import (
            POSTcustomerGroupsResponse201DataRelationshipsCustomers,
        )
        from ..models.pos_tcustomer_groups_response_201_data_relationships_markets import (
            POSTcustomerGroupsResponse201DataRelationshipsMarkets,
        )

        d = src_dict.copy()
        _customers = d.pop("customers", UNSET)
        customers: Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsCustomers]
        if isinstance(_customers, Unset):
            customers = UNSET
        else:
            customers = POSTcustomerGroupsResponse201DataRelationshipsCustomers.from_dict(_customers)

        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = POSTcustomerGroupsResponse201DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTcustomerGroupsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTcustomerGroupsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tcustomer_groups_response_201_data_relationships = cls(
            customers=customers,
            markets=markets,
            attachments=attachments,
        )

        pos_tcustomer_groups_response_201_data_relationships.additional_properties = d
        return pos_tcustomer_groups_response_201_data_relationships

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
