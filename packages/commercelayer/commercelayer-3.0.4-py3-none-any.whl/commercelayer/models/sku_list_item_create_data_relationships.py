from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.sku_list_item_create_data_relationships_sku import SkuListItemCreateDataRelationshipsSku
    from ..models.sku_list_item_create_data_relationships_sku_list import SkuListItemCreateDataRelationshipsSkuList


T = TypeVar("T", bound="SkuListItemCreateDataRelationships")


@attr.s(auto_attribs=True)
class SkuListItemCreateDataRelationships:
    """
    Attributes:
        sku_list (SkuListItemCreateDataRelationshipsSkuList):
        sku (SkuListItemCreateDataRelationshipsSku):
    """

    sku_list: "SkuListItemCreateDataRelationshipsSkuList"
    sku: "SkuListItemCreateDataRelationshipsSku"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_list = self.sku_list.to_dict()

        sku = self.sku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku_list": sku_list,
                "sku": sku,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_list_item_create_data_relationships_sku import SkuListItemCreateDataRelationshipsSku
        from ..models.sku_list_item_create_data_relationships_sku_list import SkuListItemCreateDataRelationshipsSkuList

        d = src_dict.copy()
        sku_list = SkuListItemCreateDataRelationshipsSkuList.from_dict(d.pop("sku_list"))

        sku = SkuListItemCreateDataRelationshipsSku.from_dict(d.pop("sku"))

        sku_list_item_create_data_relationships = cls(
            sku_list=sku_list,
            sku=sku,
        )

        sku_list_item_create_data_relationships.additional_properties = d
        return sku_list_item_create_data_relationships

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
