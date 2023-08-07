from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_create_data_relationships_shipping_address_data_type import (
    OrderCreateDataRelationshipsShippingAddressDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCreateDataRelationshipsShippingAddressData")


@attr.s(auto_attribs=True)
class OrderCreateDataRelationshipsShippingAddressData:
    """
    Attributes:
        type (Union[Unset, OrderCreateDataRelationshipsShippingAddressDataType]): The resource's type
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
    """

    type: Union[Unset, OrderCreateDataRelationshipsShippingAddressDataType] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OrderCreateDataRelationshipsShippingAddressDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OrderCreateDataRelationshipsShippingAddressDataType(_type)

        id = d.pop("id", UNSET)

        order_create_data_relationships_shipping_address_data = cls(
            type=type,
            id=id,
        )

        order_create_data_relationships_shipping_address_data.additional_properties = d
        return order_create_data_relationships_shipping_address_data

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
