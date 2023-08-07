from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_create_data_relationships_market import PaymentMethodCreateDataRelationshipsMarket
    from ..models.payment_method_create_data_relationships_payment_gateway import (
        PaymentMethodCreateDataRelationshipsPaymentGateway,
    )


T = TypeVar("T", bound="PaymentMethodCreateDataRelationships")


@attr.s(auto_attribs=True)
class PaymentMethodCreateDataRelationships:
    """
    Attributes:
        payment_gateway (PaymentMethodCreateDataRelationshipsPaymentGateway):
        market (Union[Unset, PaymentMethodCreateDataRelationshipsMarket]):
    """

    payment_gateway: "PaymentMethodCreateDataRelationshipsPaymentGateway"
    market: Union[Unset, "PaymentMethodCreateDataRelationshipsMarket"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_gateway = self.payment_gateway.to_dict()

        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_gateway": payment_gateway,
            }
        )
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_create_data_relationships_market import PaymentMethodCreateDataRelationshipsMarket
        from ..models.payment_method_create_data_relationships_payment_gateway import (
            PaymentMethodCreateDataRelationshipsPaymentGateway,
        )

        d = src_dict.copy()
        payment_gateway = PaymentMethodCreateDataRelationshipsPaymentGateway.from_dict(d.pop("payment_gateway"))

        _market = d.pop("market", UNSET)
        market: Union[Unset, PaymentMethodCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PaymentMethodCreateDataRelationshipsMarket.from_dict(_market)

        payment_method_create_data_relationships = cls(
            payment_gateway=payment_gateway,
            market=market,
        )

        payment_method_create_data_relationships.additional_properties = d
        return payment_method_create_data_relationships

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
