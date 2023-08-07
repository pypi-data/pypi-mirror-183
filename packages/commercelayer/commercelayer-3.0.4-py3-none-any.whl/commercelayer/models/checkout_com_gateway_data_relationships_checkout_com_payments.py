from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_com_gateway_data_relationships_checkout_com_payments_data import (
        CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData,
    )


T = TypeVar("T", bound="CheckoutComGatewayDataRelationshipsCheckoutComPayments")


@attr.s(auto_attribs=True)
class CheckoutComGatewayDataRelationshipsCheckoutComPayments:
    """
    Attributes:
        data (Union[Unset, CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData]):
    """

    data: Union[Unset, "CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData"] = UNSET
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
        from ..models.checkout_com_gateway_data_relationships_checkout_com_payments_data import (
            CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CheckoutComGatewayDataRelationshipsCheckoutComPaymentsData.from_dict(_data)

        checkout_com_gateway_data_relationships_checkout_com_payments = cls(
            data=data,
        )

        checkout_com_gateway_data_relationships_checkout_com_payments.additional_properties = d
        return checkout_com_gateway_data_relationships_checkout_com_payments

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
