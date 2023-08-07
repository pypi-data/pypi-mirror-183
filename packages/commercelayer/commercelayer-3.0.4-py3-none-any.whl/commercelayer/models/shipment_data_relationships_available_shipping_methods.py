from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_data_relationships_available_shipping_methods_data import (
        ShipmentDataRelationshipsAvailableShippingMethodsData,
    )


T = TypeVar("T", bound="ShipmentDataRelationshipsAvailableShippingMethods")


@attr.s(auto_attribs=True)
class ShipmentDataRelationshipsAvailableShippingMethods:
    """
    Attributes:
        data (Union[Unset, ShipmentDataRelationshipsAvailableShippingMethodsData]):
    """

    data: Union[Unset, "ShipmentDataRelationshipsAvailableShippingMethodsData"] = UNSET
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
        from ..models.shipment_data_relationships_available_shipping_methods_data import (
            ShipmentDataRelationshipsAvailableShippingMethodsData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ShipmentDataRelationshipsAvailableShippingMethodsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ShipmentDataRelationshipsAvailableShippingMethodsData.from_dict(_data)

        shipment_data_relationships_available_shipping_methods = cls(
            data=data,
        )

        shipment_data_relationships_available_shipping_methods.additional_properties = d
        return shipment_data_relationships_available_shipping_methods

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
