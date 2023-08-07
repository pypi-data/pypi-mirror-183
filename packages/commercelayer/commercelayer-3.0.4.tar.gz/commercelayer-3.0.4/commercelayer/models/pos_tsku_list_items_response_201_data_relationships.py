from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tsku_list_items_response_201_data_relationships_sku import (
        POSTskuListItemsResponse201DataRelationshipsSku,
    )
    from ..models.pos_tsku_list_items_response_201_data_relationships_sku_list import (
        POSTskuListItemsResponse201DataRelationshipsSkuList,
    )


T = TypeVar("T", bound="POSTskuListItemsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTskuListItemsResponse201DataRelationships:
    """
    Attributes:
        sku_list (Union[Unset, POSTskuListItemsResponse201DataRelationshipsSkuList]):
        sku (Union[Unset, POSTskuListItemsResponse201DataRelationshipsSku]):
    """

    sku_list: Union[Unset, "POSTskuListItemsResponse201DataRelationshipsSkuList"] = UNSET
    sku: Union[Unset, "POSTskuListItemsResponse201DataRelationshipsSku"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sku_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_list, Unset):
            sku_list = self.sku_list.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_list is not UNSET:
            field_dict["sku_list"] = sku_list
        if sku is not UNSET:
            field_dict["sku"] = sku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tsku_list_items_response_201_data_relationships_sku import (
            POSTskuListItemsResponse201DataRelationshipsSku,
        )
        from ..models.pos_tsku_list_items_response_201_data_relationships_sku_list import (
            POSTskuListItemsResponse201DataRelationshipsSkuList,
        )

        d = src_dict.copy()
        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, POSTskuListItemsResponse201DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = POSTskuListItemsResponse201DataRelationshipsSkuList.from_dict(_sku_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, POSTskuListItemsResponse201DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = POSTskuListItemsResponse201DataRelationshipsSku.from_dict(_sku)

        pos_tsku_list_items_response_201_data_relationships = cls(
            sku_list=sku_list,
            sku=sku,
        )

        pos_tsku_list_items_response_201_data_relationships.additional_properties = d
        return pos_tsku_list_items_response_201_data_relationships

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
