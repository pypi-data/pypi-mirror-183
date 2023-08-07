from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stock_item_create_data_type import StockItemCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_item_create_data_attributes import StockItemCreateDataAttributes
    from ..models.stock_item_create_data_relationships import StockItemCreateDataRelationships


T = TypeVar("T", bound="StockItemCreateData")


@attr.s(auto_attribs=True)
class StockItemCreateData:
    """
    Attributes:
        type (StockItemCreateDataType): The resource's type
        attributes (StockItemCreateDataAttributes):
        relationships (Union[Unset, StockItemCreateDataRelationships]):
    """

    type: StockItemCreateDataType
    attributes: "StockItemCreateDataAttributes"
    relationships: Union[Unset, "StockItemCreateDataRelationships"] = UNSET
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
        from ..models.stock_item_create_data_attributes import StockItemCreateDataAttributes
        from ..models.stock_item_create_data_relationships import StockItemCreateDataRelationships

        d = src_dict.copy()
        type = StockItemCreateDataType(d.pop("type"))

        attributes = StockItemCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, StockItemCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = StockItemCreateDataRelationships.from_dict(_relationships)

        stock_item_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        stock_item_create_data.additional_properties = d
        return stock_item_create_data

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
