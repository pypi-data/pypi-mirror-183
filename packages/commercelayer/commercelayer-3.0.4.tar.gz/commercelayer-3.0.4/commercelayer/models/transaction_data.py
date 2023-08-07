from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_data_type import TransactionDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_data_attributes import TransactionDataAttributes
    from ..models.transaction_data_relationships import TransactionDataRelationships


T = TypeVar("T", bound="TransactionData")


@attr.s(auto_attribs=True)
class TransactionData:
    """
    Attributes:
        type (TransactionDataType): The resource's type
        attributes (TransactionDataAttributes):
        relationships (Union[Unset, TransactionDataRelationships]):
    """

    type: TransactionDataType
    attributes: "TransactionDataAttributes"
    relationships: Union[Unset, "TransactionDataRelationships"] = UNSET
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
        from ..models.transaction_data_attributes import TransactionDataAttributes
        from ..models.transaction_data_relationships import TransactionDataRelationships

        d = src_dict.copy()
        type = TransactionDataType(d.pop("type"))

        attributes = TransactionDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, TransactionDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = TransactionDataRelationships.from_dict(_relationships)

        transaction_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        transaction_data.additional_properties = d
        return transaction_data

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
