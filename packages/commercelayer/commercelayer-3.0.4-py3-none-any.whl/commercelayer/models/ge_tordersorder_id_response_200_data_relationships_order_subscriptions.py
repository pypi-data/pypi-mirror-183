from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions_data import (
        GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData,
    )
    from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions_links import (
        GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks,
    )


T = TypeVar("T", bound="GETordersorderIdResponse200DataRelationshipsOrderSubscriptions")


@attr.s(auto_attribs=True)
class GETordersorderIdResponse200DataRelationshipsOrderSubscriptions:
    """
    Attributes:
        links (Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks]):
        data (Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData]):
    """

    links: Union[Unset, "GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks"] = UNSET
    data: Union[Unset, "GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData"] = UNSET
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
        from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions_data import (
            GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData,
        )
        from ..models.ge_tordersorder_id_response_200_data_relationships_order_subscriptions_links import (
            GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETordersorderIdResponse200DataRelationshipsOrderSubscriptionsData.from_dict(_data)

        ge_tordersorder_id_response_200_data_relationships_order_subscriptions = cls(
            links=links,
            data=data,
        )

        ge_tordersorder_id_response_200_data_relationships_order_subscriptions.additional_properties = d
        return ge_tordersorder_id_response_200_data_relationships_order_subscriptions

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
