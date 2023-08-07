from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tskussku_id_response_200_data_relationships_attachments import (
        GETskusskuIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_delivery_lead_times import (
        GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_prices import (
        GETskusskuIdResponse200DataRelationshipsPrices,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_shipping_category import (
        GETskusskuIdResponse200DataRelationshipsShippingCategory,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_sku_options import (
        GETskusskuIdResponse200DataRelationshipsSkuOptions,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_stock_items import (
        GETskusskuIdResponse200DataRelationshipsStockItems,
    )


T = TypeVar("T", bound="GETskusskuIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETskusskuIdResponse200DataRelationships:
    """
    Attributes:
        shipping_category (Union[Unset, GETskusskuIdResponse200DataRelationshipsShippingCategory]):
        prices (Union[Unset, GETskusskuIdResponse200DataRelationshipsPrices]):
        stock_items (Union[Unset, GETskusskuIdResponse200DataRelationshipsStockItems]):
        delivery_lead_times (Union[Unset, GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes]):
        sku_options (Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptions]):
        attachments (Union[Unset, GETskusskuIdResponse200DataRelationshipsAttachments]):
    """

    shipping_category: Union[Unset, "GETskusskuIdResponse200DataRelationshipsShippingCategory"] = UNSET
    prices: Union[Unset, "GETskusskuIdResponse200DataRelationshipsPrices"] = UNSET
    stock_items: Union[Unset, "GETskusskuIdResponse200DataRelationshipsStockItems"] = UNSET
    delivery_lead_times: Union[Unset, "GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes"] = UNSET
    sku_options: Union[Unset, "GETskusskuIdResponse200DataRelationshipsSkuOptions"] = UNSET
    attachments: Union[Unset, "GETskusskuIdResponse200DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_category, Unset):
            shipping_category = self.shipping_category.to_dict()

        prices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict()

        stock_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_items, Unset):
            stock_items = self.stock_items.to_dict()

        delivery_lead_times: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_lead_times, Unset):
            delivery_lead_times = self.delivery_lead_times.to_dict()

        sku_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_options, Unset):
            sku_options = self.sku_options.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_category is not UNSET:
            field_dict["shipping_category"] = shipping_category
        if prices is not UNSET:
            field_dict["prices"] = prices
        if stock_items is not UNSET:
            field_dict["stock_items"] = stock_items
        if delivery_lead_times is not UNSET:
            field_dict["delivery_lead_times"] = delivery_lead_times
        if sku_options is not UNSET:
            field_dict["sku_options"] = sku_options
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tskussku_id_response_200_data_relationships_attachments import (
            GETskusskuIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_delivery_lead_times import (
            GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_prices import (
            GETskusskuIdResponse200DataRelationshipsPrices,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_shipping_category import (
            GETskusskuIdResponse200DataRelationshipsShippingCategory,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_sku_options import (
            GETskusskuIdResponse200DataRelationshipsSkuOptions,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_stock_items import (
            GETskusskuIdResponse200DataRelationshipsStockItems,
        )

        d = src_dict.copy()
        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, GETskusskuIdResponse200DataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = GETskusskuIdResponse200DataRelationshipsShippingCategory.from_dict(_shipping_category)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, GETskusskuIdResponse200DataRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = GETskusskuIdResponse200DataRelationshipsPrices.from_dict(_prices)

        _stock_items = d.pop("stock_items", UNSET)
        stock_items: Union[Unset, GETskusskuIdResponse200DataRelationshipsStockItems]
        if isinstance(_stock_items, Unset):
            stock_items = UNSET
        else:
            stock_items = GETskusskuIdResponse200DataRelationshipsStockItems.from_dict(_stock_items)

        _delivery_lead_times = d.pop("delivery_lead_times", UNSET)
        delivery_lead_times: Union[Unset, GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes]
        if isinstance(_delivery_lead_times, Unset):
            delivery_lead_times = UNSET
        else:
            delivery_lead_times = GETskusskuIdResponse200DataRelationshipsDeliveryLeadTimes.from_dict(
                _delivery_lead_times
            )

        _sku_options = d.pop("sku_options", UNSET)
        sku_options: Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptions]
        if isinstance(_sku_options, Unset):
            sku_options = UNSET
        else:
            sku_options = GETskusskuIdResponse200DataRelationshipsSkuOptions.from_dict(_sku_options)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETskusskuIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETskusskuIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tskussku_id_response_200_data_relationships = cls(
            shipping_category=shipping_category,
            prices=prices,
            stock_items=stock_items,
            delivery_lead_times=delivery_lead_times,
            sku_options=sku_options,
            attachments=attachments,
        )

        ge_tskussku_id_response_200_data_relationships.additional_properties = d
        return ge_tskussku_id_response_200_data_relationships

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
