from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paypal_payment_data import PaypalPaymentData


T = TypeVar("T", bound="PaypalPayment")


@attr.s(auto_attribs=True)
class PaypalPayment:
    """
    Attributes:
        data (Union[Unset, PaypalPaymentData]):
    """

    data: Union[Unset, "PaypalPaymentData"] = UNSET
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
        from ..models.paypal_payment_data import PaypalPaymentData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PaypalPaymentData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PaypalPaymentData.from_dict(_data)

        paypal_payment = cls(
            data=data,
        )

        paypal_payment.additional_properties = d
        return paypal_payment

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
