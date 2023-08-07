from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torder_copies_response_201_data_relationships_order_subscription_data import (
        POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData,
    )
    from ..models.pos_torder_copies_response_201_data_relationships_order_subscription_links import (
        POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks,
    )


T = TypeVar("T", bound="POSTorderCopiesResponse201DataRelationshipsOrderSubscription")


@attr.s(auto_attribs=True)
class POSTorderCopiesResponse201DataRelationshipsOrderSubscription:
    """
    Attributes:
        links (Union[Unset, POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks]):
        data (Union[Unset, POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData]):
    """

    links: Union[Unset, "POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks"] = UNSET
    data: Union[Unset, "POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData"] = UNSET
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
        from ..models.pos_torder_copies_response_201_data_relationships_order_subscription_data import (
            POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData,
        )
        from ..models.pos_torder_copies_response_201_data_relationships_order_subscription_links import (
            POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTorderCopiesResponse201DataRelationshipsOrderSubscriptionData.from_dict(_data)

        pos_torder_copies_response_201_data_relationships_order_subscription = cls(
            links=links,
            data=data,
        )

        pos_torder_copies_response_201_data_relationships_order_subscription.additional_properties = d
        return pos_torder_copies_response_201_data_relationships_order_subscription

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
