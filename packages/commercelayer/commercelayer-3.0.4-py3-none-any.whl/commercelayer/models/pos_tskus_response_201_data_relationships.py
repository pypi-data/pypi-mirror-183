from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tskus_response_201_data_relationships_attachments import (
        POSTskusResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tskus_response_201_data_relationships_delivery_lead_times import (
        POSTskusResponse201DataRelationshipsDeliveryLeadTimes,
    )
    from ..models.pos_tskus_response_201_data_relationships_prices import POSTskusResponse201DataRelationshipsPrices
    from ..models.pos_tskus_response_201_data_relationships_shipping_category import (
        POSTskusResponse201DataRelationshipsShippingCategory,
    )
    from ..models.pos_tskus_response_201_data_relationships_sku_options import (
        POSTskusResponse201DataRelationshipsSkuOptions,
    )
    from ..models.pos_tskus_response_201_data_relationships_stock_items import (
        POSTskusResponse201DataRelationshipsStockItems,
    )


T = TypeVar("T", bound="POSTskusResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTskusResponse201DataRelationships:
    """
    Attributes:
        shipping_category (Union[Unset, POSTskusResponse201DataRelationshipsShippingCategory]):
        prices (Union[Unset, POSTskusResponse201DataRelationshipsPrices]):
        stock_items (Union[Unset, POSTskusResponse201DataRelationshipsStockItems]):
        delivery_lead_times (Union[Unset, POSTskusResponse201DataRelationshipsDeliveryLeadTimes]):
        sku_options (Union[Unset, POSTskusResponse201DataRelationshipsSkuOptions]):
        attachments (Union[Unset, POSTskusResponse201DataRelationshipsAttachments]):
    """

    shipping_category: Union[Unset, "POSTskusResponse201DataRelationshipsShippingCategory"] = UNSET
    prices: Union[Unset, "POSTskusResponse201DataRelationshipsPrices"] = UNSET
    stock_items: Union[Unset, "POSTskusResponse201DataRelationshipsStockItems"] = UNSET
    delivery_lead_times: Union[Unset, "POSTskusResponse201DataRelationshipsDeliveryLeadTimes"] = UNSET
    sku_options: Union[Unset, "POSTskusResponse201DataRelationshipsSkuOptions"] = UNSET
    attachments: Union[Unset, "POSTskusResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tskus_response_201_data_relationships_attachments import (
            POSTskusResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tskus_response_201_data_relationships_delivery_lead_times import (
            POSTskusResponse201DataRelationshipsDeliveryLeadTimes,
        )
        from ..models.pos_tskus_response_201_data_relationships_prices import POSTskusResponse201DataRelationshipsPrices
        from ..models.pos_tskus_response_201_data_relationships_shipping_category import (
            POSTskusResponse201DataRelationshipsShippingCategory,
        )
        from ..models.pos_tskus_response_201_data_relationships_sku_options import (
            POSTskusResponse201DataRelationshipsSkuOptions,
        )
        from ..models.pos_tskus_response_201_data_relationships_stock_items import (
            POSTskusResponse201DataRelationshipsStockItems,
        )

        d = src_dict.copy()
        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, POSTskusResponse201DataRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = POSTskusResponse201DataRelationshipsShippingCategory.from_dict(_shipping_category)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, POSTskusResponse201DataRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = POSTskusResponse201DataRelationshipsPrices.from_dict(_prices)

        _stock_items = d.pop("stock_items", UNSET)
        stock_items: Union[Unset, POSTskusResponse201DataRelationshipsStockItems]
        if isinstance(_stock_items, Unset):
            stock_items = UNSET
        else:
            stock_items = POSTskusResponse201DataRelationshipsStockItems.from_dict(_stock_items)

        _delivery_lead_times = d.pop("delivery_lead_times", UNSET)
        delivery_lead_times: Union[Unset, POSTskusResponse201DataRelationshipsDeliveryLeadTimes]
        if isinstance(_delivery_lead_times, Unset):
            delivery_lead_times = UNSET
        else:
            delivery_lead_times = POSTskusResponse201DataRelationshipsDeliveryLeadTimes.from_dict(_delivery_lead_times)

        _sku_options = d.pop("sku_options", UNSET)
        sku_options: Union[Unset, POSTskusResponse201DataRelationshipsSkuOptions]
        if isinstance(_sku_options, Unset):
            sku_options = UNSET
        else:
            sku_options = POSTskusResponse201DataRelationshipsSkuOptions.from_dict(_sku_options)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTskusResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTskusResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tskus_response_201_data_relationships = cls(
            shipping_category=shipping_category,
            prices=prices,
            stock_items=stock_items,
            delivery_lead_times=delivery_lead_times,
            sku_options=sku_options,
            attachments=attachments,
        )

        pos_tskus_response_201_data_relationships.additional_properties = d
        return pos_tskus_response_201_data_relationships

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
