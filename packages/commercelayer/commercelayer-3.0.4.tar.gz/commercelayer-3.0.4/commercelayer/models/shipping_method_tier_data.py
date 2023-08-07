from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipping_method_tier_data_type import ShippingMethodTierDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipping_method_tier_data_attributes import ShippingMethodTierDataAttributes
    from ..models.shipping_method_tier_data_relationships import ShippingMethodTierDataRelationships


T = TypeVar("T", bound="ShippingMethodTierData")


@attr.s(auto_attribs=True)
class ShippingMethodTierData:
    """
    Attributes:
        type (ShippingMethodTierDataType): The resource's type
        attributes (ShippingMethodTierDataAttributes):
        relationships (Union[Unset, ShippingMethodTierDataRelationships]):
    """

    type: ShippingMethodTierDataType
    attributes: "ShippingMethodTierDataAttributes"
    relationships: Union[Unset, "ShippingMethodTierDataRelationships"] = UNSET
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
        from ..models.shipping_method_tier_data_attributes import ShippingMethodTierDataAttributes
        from ..models.shipping_method_tier_data_relationships import ShippingMethodTierDataRelationships

        d = src_dict.copy()
        type = ShippingMethodTierDataType(d.pop("type"))

        attributes = ShippingMethodTierDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, ShippingMethodTierDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ShippingMethodTierDataRelationships.from_dict(_relationships)

        shipping_method_tier_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        shipping_method_tier_data.additional_properties = d
        return shipping_method_tier_data

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
