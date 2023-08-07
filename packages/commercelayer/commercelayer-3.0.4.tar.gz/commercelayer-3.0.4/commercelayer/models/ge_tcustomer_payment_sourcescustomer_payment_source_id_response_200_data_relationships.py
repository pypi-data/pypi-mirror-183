from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships_customer import (
        GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer,
    )
    from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships_payment_source import (
        GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource,
    )


T = TypeVar("T", bound="GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationships:
    """
    Attributes:
        customer (Union[Unset, GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer]):
        payment_source (Union[Unset,
            GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource]):
    """

    customer: Union[
        Unset, "GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer"
    ] = UNSET
    payment_source: Union[
        Unset, "GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource"
    ] = UNSET
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
        from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships_customer import (
            GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer,
        )
        from ..models.ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships_payment_source import (
            GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource,
        )

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsCustomer.from_dict(
                _customer
            )

        _payment_source = d.pop("payment_source", UNSET)
        payment_source: Union[
            Unset, GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource
        ]
        if isinstance(_payment_source, Unset):
            payment_source = UNSET
        else:
            payment_source = (
                GETcustomerPaymentSourcescustomerPaymentSourceIdResponse200DataRelationshipsPaymentSource.from_dict(
                    _payment_source
                )
            )

        ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships = cls(
            customer=customer,
            payment_source=payment_source,
        )

        ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships.additional_properties = d
        return ge_tcustomer_payment_sourcescustomer_payment_source_id_response_200_data_relationships

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
