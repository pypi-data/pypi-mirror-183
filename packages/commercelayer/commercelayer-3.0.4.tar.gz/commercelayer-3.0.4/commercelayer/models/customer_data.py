from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_data_type import CustomerDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_data_attributes import CustomerDataAttributes
    from ..models.customer_data_relationships import CustomerDataRelationships


T = TypeVar("T", bound="CustomerData")


@attr.s(auto_attribs=True)
class CustomerData:
    """
    Attributes:
        type (CustomerDataType): The resource's type
        attributes (CustomerDataAttributes):
        relationships (Union[Unset, CustomerDataRelationships]):
    """

    type: CustomerDataType
    attributes: "CustomerDataAttributes"
    relationships: Union[Unset, "CustomerDataRelationships"] = UNSET
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
        from ..models.customer_data_attributes import CustomerDataAttributes
        from ..models.customer_data_relationships import CustomerDataRelationships

        d = src_dict.copy()
        type = CustomerDataType(d.pop("type"))

        attributes = CustomerDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, CustomerDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = CustomerDataRelationships.from_dict(_relationships)

        customer_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        customer_data.additional_properties = d
        return customer_data

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
