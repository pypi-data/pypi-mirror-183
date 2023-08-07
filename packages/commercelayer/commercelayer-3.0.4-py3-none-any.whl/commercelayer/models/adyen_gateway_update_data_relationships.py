from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_gateway_update_data_relationships_adyen_payments import (
        AdyenGatewayUpdateDataRelationshipsAdyenPayments,
    )


T = TypeVar("T", bound="AdyenGatewayUpdateDataRelationships")


@attr.s(auto_attribs=True)
class AdyenGatewayUpdateDataRelationships:
    """
    Attributes:
        adyen_payments (Union[Unset, AdyenGatewayUpdateDataRelationshipsAdyenPayments]):
    """

    adyen_payments: Union[Unset, "AdyenGatewayUpdateDataRelationshipsAdyenPayments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adyen_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.adyen_payments, Unset):
            adyen_payments = self.adyen_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adyen_payments is not UNSET:
            field_dict["adyen_payments"] = adyen_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_gateway_update_data_relationships_adyen_payments import (
            AdyenGatewayUpdateDataRelationshipsAdyenPayments,
        )

        d = src_dict.copy()
        _adyen_payments = d.pop("adyen_payments", UNSET)
        adyen_payments: Union[Unset, AdyenGatewayUpdateDataRelationshipsAdyenPayments]
        if isinstance(_adyen_payments, Unset):
            adyen_payments = UNSET
        else:
            adyen_payments = AdyenGatewayUpdateDataRelationshipsAdyenPayments.from_dict(_adyen_payments)

        adyen_gateway_update_data_relationships = cls(
            adyen_payments=adyen_payments,
        )

        adyen_gateway_update_data_relationships.additional_properties = d
        return adyen_gateway_update_data_relationships

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
