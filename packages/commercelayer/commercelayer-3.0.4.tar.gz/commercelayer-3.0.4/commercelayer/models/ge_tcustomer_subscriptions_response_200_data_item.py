from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ge_tcustomer_subscriptions_response_200_data_item_type import (
    GETcustomerSubscriptionsResponse200DataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tcustomer_subscriptions_response_200_data_item_attributes import (
        GETcustomerSubscriptionsResponse200DataItemAttributes,
    )
    from ..models.ge_tcustomer_subscriptions_response_200_data_item_links import (
        GETcustomerSubscriptionsResponse200DataItemLinks,
    )
    from ..models.ge_tcustomer_subscriptions_response_200_data_item_relationships import (
        GETcustomerSubscriptionsResponse200DataItemRelationships,
    )


T = TypeVar("T", bound="GETcustomerSubscriptionsResponse200DataItem")


@attr.s(auto_attribs=True)
class GETcustomerSubscriptionsResponse200DataItem:
    """
    Attributes:
        id (Union[Unset, str]): The resource's id Example: XGZwpOSrWL.
        type (Union[Unset, GETcustomerSubscriptionsResponse200DataItemType]): The resource's type
        links (Union[Unset, GETcustomerSubscriptionsResponse200DataItemLinks]):
        attributes (Union[Unset, GETcustomerSubscriptionsResponse200DataItemAttributes]):
        relationships (Union[Unset, GETcustomerSubscriptionsResponse200DataItemRelationships]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, GETcustomerSubscriptionsResponse200DataItemType] = UNSET
    links: Union[Unset, "GETcustomerSubscriptionsResponse200DataItemLinks"] = UNSET
    attributes: Union[Unset, "GETcustomerSubscriptionsResponse200DataItemAttributes"] = UNSET
    relationships: Union[Unset, "GETcustomerSubscriptionsResponse200DataItemRelationships"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if links is not UNSET:
            field_dict["links"] = links
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tcustomer_subscriptions_response_200_data_item_attributes import (
            GETcustomerSubscriptionsResponse200DataItemAttributes,
        )
        from ..models.ge_tcustomer_subscriptions_response_200_data_item_links import (
            GETcustomerSubscriptionsResponse200DataItemLinks,
        )
        from ..models.ge_tcustomer_subscriptions_response_200_data_item_relationships import (
            GETcustomerSubscriptionsResponse200DataItemRelationships,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GETcustomerSubscriptionsResponse200DataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GETcustomerSubscriptionsResponse200DataItemType(_type)

        _links = d.pop("links", UNSET)
        links: Union[Unset, GETcustomerSubscriptionsResponse200DataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETcustomerSubscriptionsResponse200DataItemLinks.from_dict(_links)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, GETcustomerSubscriptionsResponse200DataItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = GETcustomerSubscriptionsResponse200DataItemAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, GETcustomerSubscriptionsResponse200DataItemRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = GETcustomerSubscriptionsResponse200DataItemRelationships.from_dict(_relationships)

        ge_tcustomer_subscriptions_response_200_data_item = cls(
            id=id,
            type=type,
            links=links,
            attributes=attributes,
            relationships=relationships,
        )

        ge_tcustomer_subscriptions_response_200_data_item.additional_properties = d
        return ge_tcustomer_subscriptions_response_200_data_item

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
