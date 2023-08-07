from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_list_item_data_relationships_sku_data import SkuListItemDataRelationshipsSkuData


T = TypeVar("T", bound="SkuListItemDataRelationshipsSku")


@attr.s(auto_attribs=True)
class SkuListItemDataRelationshipsSku:
    """
    Attributes:
        data (Union[Unset, SkuListItemDataRelationshipsSkuData]):
    """

    data: Union[Unset, "SkuListItemDataRelationshipsSkuData"] = UNSET
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
        from ..models.sku_list_item_data_relationships_sku_data import SkuListItemDataRelationshipsSkuData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SkuListItemDataRelationshipsSkuData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SkuListItemDataRelationshipsSkuData.from_dict(_data)

        sku_list_item_data_relationships_sku = cls(
            data=data,
        )

        sku_list_item_data_relationships_sku.additional_properties = d
        return sku_list_item_data_relationships_sku

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
