from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tcustomers_response_201_data_relationships_order_subscriptions_data import (
        POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData,
    )
    from ..models.pos_tcustomers_response_201_data_relationships_order_subscriptions_links import (
        POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks,
    )


T = TypeVar("T", bound="POSTcustomersResponse201DataRelationshipsOrderSubscriptions")


@attr.s(auto_attribs=True)
class POSTcustomersResponse201DataRelationshipsOrderSubscriptions:
    """
    Attributes:
        links (Union[Unset, POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks]):
        data (Union[Unset, POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData]):
    """

    links: Union[Unset, "POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks"] = UNSET
    data: Union[Unset, "POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tcustomers_response_201_data_relationships_order_subscriptions_data import (
            POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData,
        )
        from ..models.pos_tcustomers_response_201_data_relationships_order_subscriptions_links import (
            POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTcustomersResponse201DataRelationshipsOrderSubscriptionsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTcustomersResponse201DataRelationshipsOrderSubscriptionsData.from_dict(_data)

        pos_tcustomers_response_201_data_relationships_order_subscriptions = cls(
            links=links,
            data=data,
        )

        pos_tcustomers_response_201_data_relationships_order_subscriptions.additional_properties = d
        return pos_tcustomers_response_201_data_relationships_order_subscriptions

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
