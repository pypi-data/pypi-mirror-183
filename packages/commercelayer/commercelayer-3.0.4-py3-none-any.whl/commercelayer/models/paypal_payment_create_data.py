from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.paypal_payment_create_data_type import PaypalPaymentCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paypal_payment_create_data_attributes import PaypalPaymentCreateDataAttributes
    from ..models.paypal_payment_create_data_relationships import PaypalPaymentCreateDataRelationships


T = TypeVar("T", bound="PaypalPaymentCreateData")


@attr.s(auto_attribs=True)
class PaypalPaymentCreateData:
    """
    Attributes:
        type (PaypalPaymentCreateDataType): The resource's type
        attributes (PaypalPaymentCreateDataAttributes):
        relationships (Union[Unset, PaypalPaymentCreateDataRelationships]):
    """

    type: PaypalPaymentCreateDataType
    attributes: "PaypalPaymentCreateDataAttributes"
    relationships: Union[Unset, "PaypalPaymentCreateDataRelationships"] = UNSET
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
        from ..models.paypal_payment_create_data_attributes import PaypalPaymentCreateDataAttributes
        from ..models.paypal_payment_create_data_relationships import PaypalPaymentCreateDataRelationships

        d = src_dict.copy()
        type = PaypalPaymentCreateDataType(d.pop("type"))

        attributes = PaypalPaymentCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, PaypalPaymentCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = PaypalPaymentCreateDataRelationships.from_dict(_relationships)

        paypal_payment_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        paypal_payment_create_data.additional_properties = d
        return paypal_payment_create_data

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
