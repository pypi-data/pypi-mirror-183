from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hline_item_optionsline_item_option_id_response_200_data_relationships_line_item import (
        PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem,
    )
    from ..models.patc_hline_item_optionsline_item_option_id_response_200_data_relationships_sku_option import (
        PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption,
    )


T = TypeVar("T", bound="PATCHlineItemOptionslineItemOptionIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHlineItemOptionslineItemOptionIdResponse200DataRelationships:
    """
    Attributes:
        line_item (Union[Unset, PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem]):
        sku_option (Union[Unset, PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption]):
    """

    line_item: Union[Unset, "PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem"] = UNSET
    sku_option: Union[Unset, "PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_item, Unset):
            line_item = self.line_item.to_dict()

        sku_option: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_option, Unset):
            sku_option = self.sku_option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_item is not UNSET:
            field_dict["line_item"] = line_item
        if sku_option is not UNSET:
            field_dict["sku_option"] = sku_option

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patc_hline_item_optionsline_item_option_id_response_200_data_relationships_line_item import (
            PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem,
        )
        from ..models.patc_hline_item_optionsline_item_option_id_response_200_data_relationships_sku_option import (
            PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption,
        )

        d = src_dict.copy()
        _line_item = d.pop("line_item", UNSET)
        line_item: Union[Unset, PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem]
        if isinstance(_line_item, Unset):
            line_item = UNSET
        else:
            line_item = PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsLineItem.from_dict(_line_item)

        _sku_option = d.pop("sku_option", UNSET)
        sku_option: Union[Unset, PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption]
        if isinstance(_sku_option, Unset):
            sku_option = UNSET
        else:
            sku_option = PATCHlineItemOptionslineItemOptionIdResponse200DataRelationshipsSkuOption.from_dict(
                _sku_option
            )

        patc_hline_item_optionsline_item_option_id_response_200_data_relationships = cls(
            line_item=line_item,
            sku_option=sku_option,
        )

        patc_hline_item_optionsline_item_option_id_response_200_data_relationships.additional_properties = d
        return patc_hline_item_optionsline_item_option_id_response_200_data_relationships

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
