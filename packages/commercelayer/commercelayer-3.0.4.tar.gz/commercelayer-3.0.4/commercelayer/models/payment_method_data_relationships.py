from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_data_relationships_attachments import PaymentMethodDataRelationshipsAttachments
    from ..models.payment_method_data_relationships_market import PaymentMethodDataRelationshipsMarket
    from ..models.payment_method_data_relationships_payment_gateway import PaymentMethodDataRelationshipsPaymentGateway


T = TypeVar("T", bound="PaymentMethodDataRelationships")


@attr.s(auto_attribs=True)
class PaymentMethodDataRelationships:
    """
    Attributes:
        market (Union[Unset, PaymentMethodDataRelationshipsMarket]):
        payment_gateway (Union[Unset, PaymentMethodDataRelationshipsPaymentGateway]):
        attachments (Union[Unset, PaymentMethodDataRelationshipsAttachments]):
    """

    market: Union[Unset, "PaymentMethodDataRelationshipsMarket"] = UNSET
    payment_gateway: Union[Unset, "PaymentMethodDataRelationshipsPaymentGateway"] = UNSET
    attachments: Union[Unset, "PaymentMethodDataRelationshipsAttachments"] = UNSET
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
        from ..models.payment_method_data_relationships_attachments import PaymentMethodDataRelationshipsAttachments
        from ..models.payment_method_data_relationships_market import PaymentMethodDataRelationshipsMarket
        from ..models.payment_method_data_relationships_payment_gateway import (
            PaymentMethodDataRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PaymentMethodDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PaymentMethodDataRelationshipsMarket.from_dict(_market)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, PaymentMethodDataRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = PaymentMethodDataRelationshipsPaymentGateway.from_dict(_payment_gateway)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PaymentMethodDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PaymentMethodDataRelationshipsAttachments.from_dict(_attachments)

        payment_method_data_relationships = cls(
            market=market,
            payment_gateway=payment_gateway,
            attachments=attachments,
        )

        payment_method_data_relationships.additional_properties = d
        return payment_method_data_relationships

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
