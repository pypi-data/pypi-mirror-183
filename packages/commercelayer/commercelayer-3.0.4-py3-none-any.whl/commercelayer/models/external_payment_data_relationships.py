from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_payment_data_relationships_order import ExternalPaymentDataRelationshipsOrder
    from ..models.external_payment_data_relationships_payment_gateway import (
        ExternalPaymentDataRelationshipsPaymentGateway,
    )
    from ..models.external_payment_data_relationships_wallet import ExternalPaymentDataRelationshipsWallet


T = TypeVar("T", bound="ExternalPaymentDataRelationships")


@attr.s(auto_attribs=True)
class ExternalPaymentDataRelationships:
    """
    Attributes:
        order (Union[Unset, ExternalPaymentDataRelationshipsOrder]):
        payment_gateway (Union[Unset, ExternalPaymentDataRelationshipsPaymentGateway]):
        wallet (Union[Unset, ExternalPaymentDataRelationshipsWallet]):
    """

    order: Union[Unset, "ExternalPaymentDataRelationshipsOrder"] = UNSET
    payment_gateway: Union[Unset, "ExternalPaymentDataRelationshipsPaymentGateway"] = UNSET
    wallet: Union[Unset, "ExternalPaymentDataRelationshipsWallet"] = UNSET
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
        from ..models.external_payment_data_relationships_order import ExternalPaymentDataRelationshipsOrder
        from ..models.external_payment_data_relationships_payment_gateway import (
            ExternalPaymentDataRelationshipsPaymentGateway,
        )
        from ..models.external_payment_data_relationships_wallet import ExternalPaymentDataRelationshipsWallet

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, ExternalPaymentDataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = ExternalPaymentDataRelationshipsOrder.from_dict(_order)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, ExternalPaymentDataRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = ExternalPaymentDataRelationshipsPaymentGateway.from_dict(_payment_gateway)

        _wallet = d.pop("wallet", UNSET)
        wallet: Union[Unset, ExternalPaymentDataRelationshipsWallet]
        if isinstance(_wallet, Unset):
            wallet = UNSET
        else:
            wallet = ExternalPaymentDataRelationshipsWallet.from_dict(_wallet)

        external_payment_data_relationships = cls(
            order=order,
            payment_gateway=payment_gateway,
            wallet=wallet,
        )

        external_payment_data_relationships.additional_properties = d
        return external_payment_data_relationships

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
