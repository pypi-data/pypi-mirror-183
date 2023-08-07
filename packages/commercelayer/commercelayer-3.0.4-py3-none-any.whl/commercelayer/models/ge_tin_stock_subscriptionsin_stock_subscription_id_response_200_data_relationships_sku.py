from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku_data import (
        GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData,
    )
    from ..models.ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku_links import (
        GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks,
    )


T = TypeVar("T", bound="GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku")


@attr.s(auto_attribs=True)
class GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSku:
    """
    Attributes:
        links (Union[Unset, GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks]):
        data (Union[Unset, GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData]):
    """

    links: Union[Unset, "GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks"] = UNSET
    data: Union[Unset, "GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData"] = UNSET
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
        from ..models.ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku_data import (
            GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData,
        )
        from ..models.ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku_links import (
            GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuData.from_dict(_data)

        ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku = cls(
            links=links,
            data=data,
        )

        ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku.additional_properties = d
        return ge_tin_stock_subscriptionsin_stock_subscription_id_response_200_data_relationships_sku

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
