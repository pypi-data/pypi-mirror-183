from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_attachments import (
        GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_customers import (
        GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers,
    )
    from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_markets import (
        GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets,
    )


T = TypeVar("T", bound="GETcustomerGroupscustomerGroupIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcustomerGroupscustomerGroupIdResponse200DataRelationships:
    """
    Attributes:
        customers (Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers]):
        markets (Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets]):
        attachments (Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments]):
    """

    customers: Union[Unset, "GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers"] = UNSET
    markets: Union[Unset, "GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_attachments import (
            GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_customers import (
            GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers,
        )
        from ..models.ge_tcustomer_groupscustomer_group_id_response_200_data_relationships_markets import (
            GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets,
        )

        d = src_dict.copy()
        _customers = d.pop("customers", UNSET)
        customers: Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers]
        if isinstance(_customers, Unset):
            customers = UNSET
        else:
            customers = GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsCustomers.from_dict(_customers)

        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        ge_tcustomer_groupscustomer_group_id_response_200_data_relationships = cls(
            customers=customers,
            markets=markets,
            attachments=attachments,
        )

        ge_tcustomer_groupscustomer_group_id_response_200_data_relationships.additional_properties = d
        return ge_tcustomer_groupscustomer_group_id_response_200_data_relationships

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
