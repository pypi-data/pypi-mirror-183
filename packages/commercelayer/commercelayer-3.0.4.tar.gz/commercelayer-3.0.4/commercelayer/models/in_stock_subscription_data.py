from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.in_stock_subscription_data_type import InStockSubscriptionDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_stock_subscription_data_attributes import InStockSubscriptionDataAttributes
    from ..models.in_stock_subscription_data_relationships import InStockSubscriptionDataRelationships


T = TypeVar("T", bound="InStockSubscriptionData")


@attr.s(auto_attribs=True)
class InStockSubscriptionData:
    """
    Attributes:
        type (InStockSubscriptionDataType): The resource's type
        attributes (InStockSubscriptionDataAttributes):
        relationships (Union[Unset, InStockSubscriptionDataRelationships]):
    """

    type: InStockSubscriptionDataType
    attributes: "InStockSubscriptionDataAttributes"
    relationships: Union[Unset, "InStockSubscriptionDataRelationships"] = UNSET
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
        from ..models.in_stock_subscription_data_attributes import InStockSubscriptionDataAttributes
        from ..models.in_stock_subscription_data_relationships import InStockSubscriptionDataRelationships

        d = src_dict.copy()
        type = InStockSubscriptionDataType(d.pop("type"))

        attributes = InStockSubscriptionDataAttributes.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, InStockSubscriptionDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = InStockSubscriptionDataRelationships.from_dict(_relationships)

        in_stock_subscription_data = cls(
            type=type,
            attributes=attributes,
            relationships=relationships,
        )

        in_stock_subscription_data.additional_properties = d
        return in_stock_subscription_data

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
