from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments_data import (
        GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData,
    )
    from ..models.ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments_links import (
        GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks,
    )


T = TypeVar("T", bound="GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPayments")


@attr.s(auto_attribs=True)
class GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPayments:
    """
    Attributes:
        links (Union[Unset, GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks]):
        data (Union[Unset, GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData]):
    """

    links: Union[Unset, "GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks"] = UNSET
    data: Union[Unset, "GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData"] = UNSET
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
        from ..models.ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments_data import (
            GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData,
        )
        from ..models.ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments_links import (
            GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETklarnaGatewaysResponse200DataItemRelationshipsKlarnaPaymentsData.from_dict(_data)

        ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments = cls(
            links=links,
            data=data,
        )

        ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments.additional_properties = d
        return ge_tklarna_gateways_response_200_data_item_relationships_klarna_payments

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
