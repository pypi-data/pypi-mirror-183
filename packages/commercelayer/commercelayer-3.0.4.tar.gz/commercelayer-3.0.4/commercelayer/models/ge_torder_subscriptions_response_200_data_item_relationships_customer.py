from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer_data import (
        GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData,
    )
    from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer_links import (
        GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks,
    )


T = TypeVar("T", bound="GETorderSubscriptionsResponse200DataItemRelationshipsCustomer")


@attr.s(auto_attribs=True)
class GETorderSubscriptionsResponse200DataItemRelationshipsCustomer:
    """
    Attributes:
        links (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks]):
        data (Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData]):
    """

    links: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks"] = UNSET
    data: Union[Unset, "GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData"] = UNSET
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
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer_data import (
            GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData,
        )
        from ..models.ge_torder_subscriptions_response_200_data_item_relationships_customer_links import (
            GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETorderSubscriptionsResponse200DataItemRelationshipsCustomerLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETorderSubscriptionsResponse200DataItemRelationshipsCustomerData.from_dict(_data)

        ge_torder_subscriptions_response_200_data_item_relationships_customer = cls(
            links=links,
            data=data,
        )

        ge_torder_subscriptions_response_200_data_item_relationships_customer.additional_properties = d
        return ge_torder_subscriptions_response_200_data_item_relationships_customer

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
