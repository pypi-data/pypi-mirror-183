from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_order import (
        GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder,
    )
    from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway import (
        GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway,
    )
    from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_wallet import (
        GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet,
    )


T = TypeVar("T", bound="GETexternalPaymentsexternalPaymentIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETexternalPaymentsexternalPaymentIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder]):
        payment_gateway (Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway]):
        wallet (Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet]):
    """

    order: Union[Unset, "GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder"] = UNSET
    payment_gateway: Union[
        Unset, "GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway"
    ] = UNSET
    wallet: Union[Unset, "GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        payment_gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_gateway, Unset):
            payment_gateway = self.payment_gateway.to_dict()

        wallet: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wallet, Unset):
            wallet = self.wallet.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if payment_gateway is not UNSET:
            field_dict["payment_gateway"] = payment_gateway
        if wallet is not UNSET:
            field_dict["wallet"] = wallet

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_order import (
            GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder,
        )
        from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_payment_gateway import (
            GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway,
        )
        from ..models.ge_texternal_paymentsexternal_payment_id_response_200_data_relationships_wallet import (
            GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsOrder.from_dict(_order)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsPaymentGateway.from_dict(
                _payment_gateway
            )

        _wallet = d.pop("wallet", UNSET)
        wallet: Union[Unset, GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet]
        if isinstance(_wallet, Unset):
            wallet = UNSET
        else:
            wallet = GETexternalPaymentsexternalPaymentIdResponse200DataRelationshipsWallet.from_dict(_wallet)

        ge_texternal_paymentsexternal_payment_id_response_200_data_relationships = cls(
            order=order,
            payment_gateway=payment_gateway,
            wallet=wallet,
        )

        ge_texternal_paymentsexternal_payment_id_response_200_data_relationships.additional_properties = d
        return ge_texternal_paymentsexternal_payment_id_response_200_data_relationships

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
