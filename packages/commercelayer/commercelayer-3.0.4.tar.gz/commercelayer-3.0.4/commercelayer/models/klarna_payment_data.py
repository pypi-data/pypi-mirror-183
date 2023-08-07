from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.klarna_payment_data_type import KlarnaPaymentDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.klarna_payment_data_attributes import KlarnaPaymentDataAttributes
    from ..models.klarna_payment_data_relationships import KlarnaPaymentDataRelationships


T = TypeVar("T", bound="KlarnaPaymentData")


@attr.s(auto_attribs=True)
class KlarnaPaymentData:
    """
    Attributes:
        type (KlarnaPaymentDataType): The resource's type
        attributes (KlarnaPaymentDataAttributes):
        relationships (Union[Unset, KlarnaPaymentDataRelationships]):
    """

    type: KlarnaPaymentDataType
    attributes: "KlarnaPaymentDataAttributes"
    relationships: Union[Unset, "KlarnaPaymentDataRelationships"] = UNSET
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
        from ..models.klarna_payment_data_attributes import KlarnaPaymentDataAttributes
        from ..models.klarna_payment_data_relationships import KlarnaPaymentDataRelationships

        d = src_dict.copy()
        type = KlarnaPaymentDataType(d.pop("type"))

        attributes = KlarnaPaymentDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, KlarnaPaymentDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = KlarnaPaymentDataRelationships.from_dict(_relationships)

        klarna_payment_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        klarna_payment_data.additional_properties = d
        return klarna_payment_data

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
