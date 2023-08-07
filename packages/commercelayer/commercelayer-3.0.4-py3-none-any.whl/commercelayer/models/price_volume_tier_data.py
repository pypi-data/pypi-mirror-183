from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.price_volume_tier_data_type import PriceVolumeTierDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_volume_tier_data_attributes import PriceVolumeTierDataAttributes
    from ..models.price_volume_tier_data_relationships import PriceVolumeTierDataRelationships


T = TypeVar("T", bound="PriceVolumeTierData")


@attr.s(auto_attribs=True)
class PriceVolumeTierData:
    """
    Attributes:
        type (PriceVolumeTierDataType): The resource's type
        attributes (PriceVolumeTierDataAttributes):
        relationships (Union[Unset, PriceVolumeTierDataRelationships]):
    """

    type: PriceVolumeTierDataType
    attributes: "PriceVolumeTierDataAttributes"
    relationships: Union[Unset, "PriceVolumeTierDataRelationships"] = UNSET
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
        from ..models.price_volume_tier_data_attributes import PriceVolumeTierDataAttributes
        from ..models.price_volume_tier_data_relationships import PriceVolumeTierDataRelationships

        d = src_dict.copy()
        type = PriceVolumeTierDataType(d.pop("type"))

        attributes = PriceVolumeTierDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, PriceVolumeTierDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = PriceVolumeTierDataRelationships.from_dict(_relationships)

        price_volume_tier_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        price_volume_tier_data.additional_properties = d
        return price_volume_tier_data

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
