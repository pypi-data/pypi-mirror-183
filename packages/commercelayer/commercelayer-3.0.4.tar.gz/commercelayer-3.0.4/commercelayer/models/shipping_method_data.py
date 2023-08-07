from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipping_method_data_type import ShippingMethodDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_method_data_attributes import ShippingMethodDataAttributes
    from ..models.shipping_method_data_relationships import ShippingMethodDataRelationships


T = TypeVar("T", bound="ShippingMethodData")


@attr.s(auto_attribs=True)
class ShippingMethodData:
    """
    Attributes:
        type (ShippingMethodDataType): The resource's type
        attributes (ShippingMethodDataAttributes):
        relationships (Union[Unset, ShippingMethodDataRelationships]):
    """

    type: ShippingMethodDataType
    attributes: "ShippingMethodDataAttributes"
    relationships: Union[Unset, "ShippingMethodDataRelationships"] = UNSET
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
        from ..models.shipping_method_data_attributes import ShippingMethodDataAttributes
        from ..models.shipping_method_data_relationships import ShippingMethodDataRelationships

        d = src_dict.copy()
        type = ShippingMethodDataType(d.pop("type"))

        attributes = ShippingMethodDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, ShippingMethodDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ShippingMethodDataRelationships.from_dict(_relationships)

        shipping_method_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        shipping_method_data.additional_properties = d
        return shipping_method_data

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
