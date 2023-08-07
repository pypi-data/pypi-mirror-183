from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adyen_payment_data_relationships_payment_gateway_data import (
        AdyenPaymentDataRelationshipsPaymentGatewayData,
    )


T = TypeVar("T", bound="AdyenPaymentDataRelationshipsPaymentGateway")


@attr.s(auto_attribs=True)
class AdyenPaymentDataRelationshipsPaymentGateway:
    """
    Attributes:
        data (Union[Unset, AdyenPaymentDataRelationshipsPaymentGatewayData]):
    """

    data: Union[Unset, "AdyenPaymentDataRelationshipsPaymentGatewayData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adyen_payment_data_relationships_payment_gateway_data import (
            AdyenPaymentDataRelationshipsPaymentGatewayData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, AdyenPaymentDataRelationshipsPaymentGatewayData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AdyenPaymentDataRelationshipsPaymentGatewayData.from_dict(_data)

        adyen_payment_data_relationships_payment_gateway = cls(
            data=data,
        )

        adyen_payment_data_relationships_payment_gateway.additional_properties = d
        return adyen_payment_data_relationships_payment_gateway

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
