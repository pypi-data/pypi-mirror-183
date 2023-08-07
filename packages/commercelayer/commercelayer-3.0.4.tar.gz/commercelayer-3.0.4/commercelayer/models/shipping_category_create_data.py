from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipping_category_create_data_type import ShippingCategoryCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_category_create_data_attributes import ShippingCategoryCreateDataAttributes
    from ..models.shipping_category_create_data_relationships import ShippingCategoryCreateDataRelationships


T = TypeVar("T", bound="ShippingCategoryCreateData")


@attr.s(auto_attribs=True)
class ShippingCategoryCreateData:
    """
    Attributes:
        type (ShippingCategoryCreateDataType): The resource's type
        attributes (ShippingCategoryCreateDataAttributes):
        relationships (Union[Unset, ShippingCategoryCreateDataRelationships]):
    """

    type: ShippingCategoryCreateDataType
    attributes: "ShippingCategoryCreateDataAttributes"
    relationships: Union[Unset, "ShippingCategoryCreateDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipping_category_create_data_attributes import ShippingCategoryCreateDataAttributes
        from ..models.shipping_category_create_data_relationships import ShippingCategoryCreateDataRelationships

        d = src_dict.copy()
        type = ShippingCategoryCreateDataType(d.pop("type"))

        attributes = ShippingCategoryCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, ShippingCategoryCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ShippingCategoryCreateDataRelationships.from_dict(_relationships)

        shipping_category_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        shipping_category_create_data.additional_properties = d
        return shipping_category_create_data

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
