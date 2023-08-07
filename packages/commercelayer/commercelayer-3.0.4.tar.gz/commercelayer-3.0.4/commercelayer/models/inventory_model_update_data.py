from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.inventory_model_update_data_type import InventoryModelUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_model_update_data_attributes import InventoryModelUpdateDataAttributes
    from ..models.inventory_model_update_data_relationships import InventoryModelUpdateDataRelationships


T = TypeVar("T", bound="InventoryModelUpdateData")


@attr.s(auto_attribs=True)
class InventoryModelUpdateData:
    """
    Attributes:
        type (InventoryModelUpdateDataType): The resource's type
        id (str): The resource's id Example: XGZwpOSrWL.
        attributes (InventoryModelUpdateDataAttributes):
        relationships (Union[Unset, InventoryModelUpdateDataRelationships]):
    """

    type: InventoryModelUpdateDataType
    id: str
    attributes: "InventoryModelUpdateDataAttributes"
    relationships: Union[Unset, "InventoryModelUpdateDataRelationships"] = UNSET
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
        from ..models.inventory_model_update_data_attributes import InventoryModelUpdateDataAttributes
        from ..models.inventory_model_update_data_relationships import InventoryModelUpdateDataRelationships

        d = src_dict.copy()
        type = InventoryModelUpdateDataType(d.pop("type"))

        id = d.pop("id")

        attributes = InventoryModelUpdateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, InventoryModelUpdateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = InventoryModelUpdateDataRelationships.from_dict(_relationships)

        inventory_model_update_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        inventory_model_update_data.additional_properties = d
        return inventory_model_update_data

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
