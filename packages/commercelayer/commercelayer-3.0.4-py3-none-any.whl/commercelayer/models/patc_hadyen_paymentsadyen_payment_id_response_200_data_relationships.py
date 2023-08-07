from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships_order import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder,
    )
    from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships_payment_gateway import (
        PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway,
    )


T = TypeVar("T", bound="PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationships:
    """
    Attributes:
        order (Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder]):
        payment_gateway (Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway]):
    """

    order: Union[Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder"] = UNSET
    payment_gateway: Union[Unset, "PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway"] = UNSET
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
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships_order import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder,
        )
        from ..models.patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships_payment_gateway import (
            PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsOrder.from_dict(_order)

        _payment_gateway = d.pop("payment_gateway", UNSET)
        payment_gateway: Union[Unset, PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway]
        if isinstance(_payment_gateway, Unset):
            payment_gateway = UNSET
        else:
            payment_gateway = PATCHadyenPaymentsadyenPaymentIdResponse200DataRelationshipsPaymentGateway.from_dict(
                _payment_gateway
            )

        patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships = cls(
            order=order,
            payment_gateway=payment_gateway,
        )

        patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships.additional_properties = d
        return patc_hadyen_paymentsadyen_payment_id_response_200_data_relationships

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
