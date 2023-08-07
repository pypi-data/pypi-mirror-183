from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delivery_lead_time_create_data_type import DeliveryLeadTimeCreateDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_lead_time_create_data_attributes import DeliveryLeadTimeCreateDataAttributes
    from ..models.delivery_lead_time_create_data_relationships import DeliveryLeadTimeCreateDataRelationships


T = TypeVar("T", bound="DeliveryLeadTimeCreateData")


@attr.s(auto_attribs=True)
class DeliveryLeadTimeCreateData:
    """
    Attributes:
        type (DeliveryLeadTimeCreateDataType): The resource's type
        attributes (DeliveryLeadTimeCreateDataAttributes):
        relationships (Union[Unset, DeliveryLeadTimeCreateDataRelationships]):
    """

    type: DeliveryLeadTimeCreateDataType
    attributes: "DeliveryLeadTimeCreateDataAttributes"
    relationships: Union[Unset, "DeliveryLeadTimeCreateDataRelationships"] = UNSET
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
        from ..models.delivery_lead_time_create_data_attributes import DeliveryLeadTimeCreateDataAttributes
        from ..models.delivery_lead_time_create_data_relationships import DeliveryLeadTimeCreateDataRelationships

        d = src_dict.copy()
        type = DeliveryLeadTimeCreateDataType(d.pop("type"))

        attributes = DeliveryLeadTimeCreateDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, DeliveryLeadTimeCreateDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = DeliveryLeadTimeCreateDataRelationships.from_dict(_relationships)

        delivery_lead_time_create_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        delivery_lead_time_create_data.additional_properties = d
        return delivery_lead_time_create_data

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
