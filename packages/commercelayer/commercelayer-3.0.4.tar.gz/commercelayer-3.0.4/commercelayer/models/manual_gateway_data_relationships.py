from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manual_gateway_data_relationships_payment_methods import ManualGatewayDataRelationshipsPaymentMethods


T = TypeVar("T", bound="ManualGatewayDataRelationships")


@attr.s(auto_attribs=True)
class ManualGatewayDataRelationships:
    """
    Attributes:
        payment_methods (Union[Unset, ManualGatewayDataRelationshipsPaymentMethods]):
    """

    payment_methods: Union[Unset, "ManualGatewayDataRelationshipsPaymentMethods"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.manual_gateway_data_relationships_payment_methods import (
            ManualGatewayDataRelationshipsPaymentMethods,
        )

        d = src_dict.copy()
        _payment_methods = d.pop("payment_methods", UNSET)
        payment_methods: Union[Unset, ManualGatewayDataRelationshipsPaymentMethods]
        if isinstance(_payment_methods, Unset):
            payment_methods = UNSET
        else:
            payment_methods = ManualGatewayDataRelationshipsPaymentMethods.from_dict(_payment_methods)

        manual_gateway_data_relationships = cls(
            payment_methods=payment_methods,
        )

        manual_gateway_data_relationships.additional_properties = d
        return manual_gateway_data_relationships

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
