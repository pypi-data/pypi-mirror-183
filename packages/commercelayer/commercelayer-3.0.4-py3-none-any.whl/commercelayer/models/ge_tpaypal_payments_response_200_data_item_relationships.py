from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tpaypal_payments_response_200_data_item_relationships_order import (
        GETpaypalPaymentsResponse200DataItemRelationshipsOrder,
    )
    from ..models.ge_tpaypal_payments_response_200_data_item_relationships_payment_gateway import (
        GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway,
    )


T = TypeVar("T", bound="GETpaypalPaymentsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpaypalPaymentsResponse200DataItemRelationships:
    """
    Attributes:
        order (Union[Unset, GETpaypalPaymentsResponse200DataItemRelationshipsOrder]):
        payment_gateway (Union[Unset, GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway]):
    """

    order: Union[Unset, "GETpaypalPaymentsResponse200DataItemRelationshipsOrder"] = UNSET
    payment_gateway: Union[Unset, "GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        payment_gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_gateway, Unset):
            payment_gateway = self.payment_gateway.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if payment_gateway is not UNSET:
            field_dict["payment_gateway"] = payment_gateway

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tpaypal_payments_response_200_data_item_relationships_order import (
            GETpaypalPaymentsResponse200DataItemRelationshipsOrder,
        )
        from ..models.ge_tpaypal_payments_response_200_data_item_relationships_payment_gateway import (
            GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, GETpaypalPaymentsResponse200DataItemRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = GETpaypalPaymentsResponse200DataItemRelationshipsOrder.from_dict(_order)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = GETpaypalPaymentsResponse200DataItemRelationshipsPaymentGateway.from_dict(
                _payment_gateway
            )

        ge_tpaypal_payments_response_200_data_item_relationships = cls(
            order=order,
            payment_gateway=payment_gateway,
        )

        ge_tpaypal_payments_response_200_data_item_relationships.additional_properties = d
        return ge_tpaypal_payments_response_200_data_item_relationships

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
