from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments_data import (
        POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData,
    )
    from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments_links import (
        POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks,
    )


T = TypeVar("T", bound="POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments")


@attr.s(auto_attribs=True)
class POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPayments:
    """
    Attributes:
        links (Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks]):
        data (Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData]):
    """

    links: Union[Unset, "POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks"] = UNSET
    data: Union[Unset, "POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData"] = UNSET
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
        from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments_data import (
            POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData,
        )
        from ..models.pos_tklarna_gateways_response_201_data_relationships_klarna_payments_links import (
            POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTklarnaGatewaysResponse201DataRelationshipsKlarnaPaymentsData.from_dict(_data)

        pos_tklarna_gateways_response_201_data_relationships_klarna_payments = cls(
            links=links,
            data=data,
        )

        pos_tklarna_gateways_response_201_data_relationships_klarna_payments.additional_properties = d
        return pos_tklarna_gateways_response_201_data_relationships_klarna_payments

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
