from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_payment_sources_response_200_data_item_relationships_customer import (
        GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_payment_sources_response_200_data_item_relationships_payment_source import (
        GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource,
    )


T = TypeVar("T", bound="GETcustomerPaymentSourcesResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETcustomerPaymentSourcesResponse200DataItemRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer]):
        payment_source (Union[Unset, GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource]):
    """

    customer: Union[Unset, "GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer"] = UNSET
    payment_source: Union[Unset, "GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        payment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_source, Unset):
            payment_source = self.payment_source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if payment_source is not UNSET:
            field_dict["payment_source"] = payment_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcustomer_payment_sources_response_200_data_item_relationships_customer import (
            GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_payment_sources_response_200_data_item_relationships_payment_source import (
            GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerPaymentSourcesResponse200DataItemRelationshipsCustomer.from_dict(_customer)

        _payment_source = d.pop("payment_source", UNSET)
        payment_source: Union[Unset, GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource]
        if isinstance(_payment_source, Unset):
            payment_source = UNSET
        else:
            payment_source = GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSource.from_dict(
                _payment_source
            )

        ge_tcustomer_payment_sources_response_200_data_item_relationships = cls(
            customer=customer,
            payment_source=payment_source,
        )

        ge_tcustomer_payment_sources_response_200_data_item_relationships.additional_properties = d
        return ge_tcustomer_payment_sources_response_200_data_item_relationships

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
