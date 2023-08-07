from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sku_create_data_relationships_shipping_category_data_type import (
    SkuCreateDataRelationshipsShippingCategoryDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SkuCreateDataRelationshipsShippingCategoryData")


@attr.s(auto_attribs=True)
class SkuCreateDataRelationshipsShippingCategoryData:
    """
    Attributes:
        type (Union[Unset, SkuCreateDataRelationshipsShippingCategoryDataType]): The resource's type
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
    """

    type: Union[Unset, SkuCreateDataRelationshipsShippingCategoryDataType] = UNSET
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
        type: Union[Unset, SkuCreateDataRelationshipsShippingCategoryDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SkuCreateDataRelationshipsShippingCategoryDataType(_type)

        id = d.pop("id", UNSET)

        sku_create_data_relationships_shipping_category_data = cls(
            type=type,
            id=id,
        )

        sku_create_data_relationships_shipping_category_data.additional_properties = d
        return sku_create_data_relationships_shipping_category_data

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
