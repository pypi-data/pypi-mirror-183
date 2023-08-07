from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcustomer_payment_sources_response_201_data_relationships_customer_data import (
        POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData,
    )
    from ..models.pos_tcustomer_payment_sources_response_201_data_relationships_customer_links import (
        POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks,
    )


T = TypeVar("T", bound="POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomer")


@attr.s(auto_attribs=True)
class POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomer:
    """
    Attributes:
        links (Union[Unset, POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks]):
        data (Union[Unset, POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData]):
    """

    links: Union[Unset, "POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks"] = UNSET
    data: Union[Unset, "POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcustomer_payment_sources_response_201_data_relationships_customer_data import (
            POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData,
        )
        from ..models.pos_tcustomer_payment_sources_response_201_data_relationships_customer_links import (
            POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTcustomerPaymentSourcesResponse201DataRelationshipsCustomerData.from_dict(_data)

        pos_tcustomer_payment_sources_response_201_data_relationships_customer = cls(
            links=links,
            data=data,
        )

        pos_tcustomer_payment_sources_response_201_data_relationships_customer.additional_properties = d
        return pos_tcustomer_payment_sources_response_201_data_relationships_customer

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
