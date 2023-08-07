from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.sku_list_item_create_data import SkuListItemCreateData


T = TypeVar("T", bound="SkuListItemCreate")


@attr.s(auto_attribs=True)
class SkuListItemCreate:
    """
    Attributes:
        data (SkuListItemCreateData):
    """

    data: "SkuListItemCreateData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_list_item_create_data import SkuListItemCreateData

        d = src_dict.copy()
        data = SkuListItemCreateData.from_dict(d.pop("data"))

        sku_list_item_create = cls(
            data=data,
        )

        sku_list_item_create.additional_properties = d
        return sku_list_item_create

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
