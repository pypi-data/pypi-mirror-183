from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hsku_list_itemssku_list_item_id_response_200_data_relationships_sku import (
        PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku,
    )
    from ..models.patc_hsku_list_itemssku_list_item_id_response_200_data_relationships_sku_list import (
        PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList,
    )


T = TypeVar("T", bound="PATCHskuListItemsskuListItemIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHskuListItemsskuListItemIdResponse200DataRelationships:
    """
    Attributes:
        sku_list (Union[Unset, PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList]):
        sku (Union[Unset, PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku]):
    """

    sku_list: Union[Unset, "PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList"] = UNSET
    sku: Union[Unset, "PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku"] = UNSET
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
        from ..models.patc_hsku_list_itemssku_list_item_id_response_200_data_relationships_sku import (
            PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku,
        )
        from ..models.patc_hsku_list_itemssku_list_item_id_response_200_data_relationships_sku_list import (
            PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList,
        )

        d = src_dict.copy()
        _sku_list = d.pop("sku_list", UNSET)
        sku_list: Union[Unset, PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList]
        if isinstance(_sku_list, Unset):
            sku_list = UNSET
        else:
            sku_list = PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSkuList.from_dict(_sku_list)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = PATCHskuListItemsskuListItemIdResponse200DataRelationshipsSku.from_dict(_sku)

        patc_hsku_list_itemssku_list_item_id_response_200_data_relationships = cls(
            sku_list=sku_list,
            sku=sku,
        )

        patc_hsku_list_itemssku_list_item_id_response_200_data_relationships.additional_properties = d
        return patc_hsku_list_itemssku_list_item_id_response_200_data_relationships

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
