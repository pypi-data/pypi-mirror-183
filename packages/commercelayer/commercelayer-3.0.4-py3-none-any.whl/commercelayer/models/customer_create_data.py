from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_create_data_type import CustomerCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_create_data_attributes import CustomerCreateDataAttributes
    from ..models.customer_create_data_relationships import CustomerCreateDataRelationships


T = TypeVar("T", bound="CustomerCreateData")


@attr.s(auto_attribs=True)
class CustomerCreateData:
    """
    Attributes:
        type (CustomerCreateDataType): The resource's type
        attributes (CustomerCreateDataAttributes):
        relationships (Union[Unset, CustomerCreateDataRelationships]):
    """

    type: CustomerCreateDataType
    attributes: "CustomerCreateDataAttributes"
    relationships: Union[Unset, "CustomerCreateDataRelationships"] = UNSET
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
        from ..models.customer_create_data_attributes import CustomerCreateDataAttributes
        from ..models.customer_create_data_relationships import CustomerCreateDataRelationships

        d = src_dict.copy()
        type = CustomerCreateDataType(d.pop("type"))

        attributes = CustomerCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, CustomerCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = CustomerCreateDataRelationships.from_dict(_relationships)

        customer_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        customer_create_data.additional_properties = d
        return customer_create_data

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
