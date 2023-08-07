from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpayment_methods_response_200_data_item_relationships_attachments import (
        GETpaymentMethodsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tpayment_methods_response_200_data_item_relationships_market import (
        GETpaymentMethodsResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_tpayment_methods_response_200_data_item_relationships_payment_gateway import (
        GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway,
    )


T = TypeVar("T", bound="GETpaymentMethodsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpaymentMethodsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsMarket]):
        payment_gateway (Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway]):
        attachments (Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsAttachments]):
    """

    market: Union[Unset, "GETpaymentMethodsResponse200DataItemRelationshipsMarket"] = UNSET
    payment_gateway: Union[Unset, "GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway"] = UNSET
    attachments: Union[Unset, "GETpaymentMethodsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        payment_gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_gateway, Unset):
            payment_gateway = self.payment_gateway.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if payment_gateway is not UNSET:
            field_dict["payment_gateway"] = payment_gateway
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tpayment_methods_response_200_data_item_relationships_attachments import (
            GETpaymentMethodsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tpayment_methods_response_200_data_item_relationships_market import (
            GETpaymentMethodsResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_tpayment_methods_response_200_data_item_relationships_payment_gateway import (
            GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETpaymentMethodsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = GETpaymentMethodsResponse200DataItemRelationshipsPaymentGateway.from_dict(
                _payment_gateway
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpaymentMethodsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpaymentMethodsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tpayment_methods_response_200_data_item_relationships = cls(
            market=market,
            payment_gateway=payment_gateway,
            attachments=attachments,
        )

        ge_tpayment_methods_response_200_data_item_relationships.additional_properties = d
        return ge_tpayment_methods_response_200_data_item_relationships

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
