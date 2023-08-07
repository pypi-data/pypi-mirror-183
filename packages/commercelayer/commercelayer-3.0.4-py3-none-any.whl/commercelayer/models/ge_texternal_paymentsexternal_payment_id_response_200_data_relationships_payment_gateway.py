from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway_data import (
        GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData,
    )
    from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway_links import (
        GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks,
    )


T = TypeVar("T", bound="GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway")


@attr.s(auto_attribs=True)
class GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway:
    """
    Attributes:
        links (Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks]):
        data (Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData]):
    """

    links: Union[Unset, "GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks"] = UNSET
    data: Union[Unset, "GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData"] = UNSET
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
        from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway_data import (
            GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData,
        )
        from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway_links import (
            GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGatewayData.from_dict(_data)

        ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway = cls(
            links=links,
            data=data,
        )

        ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway.additional_properties = (
            d
        )
        return ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway

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
