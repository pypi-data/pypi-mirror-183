from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sku_list_promotion_rule_update_data_type import SkuListPromotionRuleUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_list_promotion_rule_update_data_attributes import SkuListPromotionRuleUpdateDataAttributes
    from ..models.sku_list_promotion_rule_update_data_relationships import SkuListPromotionRuleUpdateDataRelationships


T = TypeVar("T", bound="SkuListPromotionRuleUpdateData")


@attr.s(auto_attribs=True)
class SkuListPromotionRuleUpdateData:
    """
    Attributes:
        type (SkuListPromotionRuleUpdateDataType): The resource's type
        id (str): The resource's id Example: XGZwpOSrWL.
        attributes (SkuListPromotionRuleUpdateDataAttributes):
        relationships (Union[Unset, SkuListPromotionRuleUpdateDataRelationships]):
    """

    type: SkuListPromotionRuleUpdateDataType
    id: str
    attributes: "SkuListPromotionRuleUpdateDataAttributes"
    relationships: Union[Unset, "SkuListPromotionRuleUpdateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sku_list_promotion_rule_update_data_attributes import SkuListPromotionRuleUpdateDataAttributes
        from ..models.sku_list_promotion_rule_update_data_relationships import (
            SkuListPromotionRuleUpdateDataRelationships,
        )

        d = src_dict.copy()
        type = SkuListPromotionRuleUpdateDataType(d.pop("type"))

        id = d.pop("id")

        attributes = SkuListPromotionRuleUpdateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, SkuListPromotionRuleUpdateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = SkuListPromotionRuleUpdateDataRelationships.from_dict(_relationships)

        sku_list_promotion_rule_update_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        sku_list_promotion_rule_update_data.additional_properties = d
        return sku_list_promotion_rule_update_data

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
