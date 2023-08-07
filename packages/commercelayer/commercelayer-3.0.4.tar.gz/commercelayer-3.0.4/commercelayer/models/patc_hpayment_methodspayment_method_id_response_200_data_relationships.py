from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_attachments import (
        PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_market import (
        PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket,
    )
    from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_payment_gateway import (
        PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway,
    )


T = TypeVar("T", bound="PATCHpaymentMethodspaymentMethodIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHpaymentMethodspaymentMethodIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket]):
        payment_gateway (Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway]):
        attachments (Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments]):
    """

    market: Union[Unset, "PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket"] = UNSET
    payment_gateway: Union[
        Unset, "PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway"
    ] = UNSET
    attachments: Union[Unset, "PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_attachments import (
            PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_market import (
            PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket,
        )
        from ..models.patc_hpayment_methodspayment_method_id_response_200_data_relationships_payment_gateway import (
            PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarket.from_dict(_market)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsPaymentGateway.from_dict(
                _payment_gateway
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hpayment_methodspayment_method_id_response_200_data_relationships = cls(
            market=market,
            payment_gateway=payment_gateway,
            attachments=attachments,
        )

        patc_hpayment_methodspayment_method_id_response_200_data_relationships.additional_properties = d
        return patc_hpayment_methodspayment_method_id_response_200_data_relationships

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
