from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_payment_source_update_data_type import CustomerPaymentSourceUpdateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_payment_source_update_data_attributes import CustomerPaymentSourceUpdateDataAttributes
    from ..models.customer_payment_source_update_data_relationships import CustomerPaymentSourceUpdateDataRelationships


T = TypeVar("T", bound="CustomerPaymentSourceUpdateData")


@attr.s(auto_attribs=True)
class CustomerPaymentSourceUpdateData:
    """
    Attributes:
        type (CustomerPaymentSourceUpdateDataType): The resource's type
        id (str): The resource's id Example: XGZwpOSrWL.
        attributes (CustomerPaymentSourceUpdateDataAttributes):
        relationships (Union[Unset, CustomerPaymentSourceUpdateDataRelationships]):
    """

    type: CustomerPaymentSourceUpdateDataType
    id: str
    attributes: "CustomerPaymentSourceUpdateDataAttributes"
    relationships: Union[Unset, "CustomerPaymentSourceUpdateDataRelationships"] = UNSET
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
        from ..models.customer_payment_source_update_data_attributes import CustomerPaymentSourceUpdateDataAttributes
        from ..models.customer_payment_source_update_data_relationships import (
            CustomerPaymentSourceUpdateDataRelationships,
        )

        d = src_dict.copy()
        type = CustomerPaymentSourceUpdateDataType(d.pop("type"))

        id = d.pop("id")

        attributes = CustomerPaymentSourceUpdateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, CustomerPaymentSourceUpdateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = CustomerPaymentSourceUpdateDataRelationships.from_dict(_relationships)

        customer_payment_source_update_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        customer_payment_source_update_data.additional_properties = d
        return customer_payment_source_update_data

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
