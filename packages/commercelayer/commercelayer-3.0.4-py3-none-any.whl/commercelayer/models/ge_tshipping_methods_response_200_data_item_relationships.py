from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_attachments import (
        GETshippingMethodsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_delivery_lead_time_for_shipment import (
        GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_market import (
        GETshippingMethodsResponse200DataItemRelationshipsMarket,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_category import (
        GETshippingMethodsResponse200DataItemRelationshipsShippingCategory,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_method_tiers import (
        GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_weight_tiers import (
        GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_zone import (
        GETshippingMethodsResponse200DataItemRelationshipsShippingZone,
    )
    from ..models.ge_tshipping_methods_response_200_data_item_relationships_stock_location import (
        GETshippingMethodsResponse200DataItemRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETshippingMethodsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETshippingMethodsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsMarket]):
        shipping_zone (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingZone]):
        shipping_category (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingCategory]):
        stock_location (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsStockLocation]):
        delivery_lead_time_for_shipment (Union[Unset,
            GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment]):
        shipping_method_tiers (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers]):
        shipping_weight_tiers (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers]):
        attachments (Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsAttachments]):
    """

    market: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsMarket"] = UNSET
    shipping_zone: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsShippingZone"] = UNSET
    shipping_category: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsShippingCategory"] = UNSET
    stock_location: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsStockLocation"] = UNSET
    delivery_lead_time_for_shipment: Union[
        Unset, "GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment"
    ] = UNSET
    shipping_method_tiers: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers"] = UNSET
    shipping_weight_tiers: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers"] = UNSET
    attachments: Union[Unset, "GETshippingMethodsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        shipping_zone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_zone, Unset):
            shipping_zone = self.shipping_zone.to_dict()

        shipping_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_category, Unset):
            shipping_category = self.shipping_category.to_dict()

        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        delivery_lead_time_for_shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_lead_time_for_shipment, Unset):
            delivery_lead_time_for_shipment = self.delivery_lead_time_for_shipment.to_dict()

        shipping_method_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method_tiers, Unset):
            shipping_method_tiers = self.shipping_method_tiers.to_dict()

        shipping_weight_tiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_weight_tiers, Unset):
            shipping_weight_tiers = self.shipping_weight_tiers.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if shipping_zone is not UNSET:
            field_dict["shipping_zone"] = shipping_zone
        if shipping_category is not UNSET:
            field_dict["shipping_category"] = shipping_category
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if delivery_lead_time_for_shipment is not UNSET:
            field_dict["delivery_lead_time_for_shipment"] = delivery_lead_time_for_shipment
        if shipping_method_tiers is not UNSET:
            field_dict["shipping_method_tiers"] = shipping_method_tiers
        if shipping_weight_tiers is not UNSET:
            field_dict["shipping_weight_tiers"] = shipping_weight_tiers
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_attachments import (
            GETshippingMethodsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_delivery_lead_time_for_shipment import (
            GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_market import (
            GETshippingMethodsResponse200DataItemRelationshipsMarket,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_category import (
            GETshippingMethodsResponse200DataItemRelationshipsShippingCategory,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_method_tiers import (
            GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_weight_tiers import (
            GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_shipping_zone import (
            GETshippingMethodsResponse200DataItemRelationshipsShippingZone,
        )
        from ..models.ge_tshipping_methods_response_200_data_item_relationships_stock_location import (
            GETshippingMethodsResponse200DataItemRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETshippingMethodsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _shipping_zone = d.pop("shipping_zone", UNSET)
        shipping_zone: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingZone]
        if isinstance(_shipping_zone, Unset):
            shipping_zone = UNSET
        else:
            shipping_zone = GETshippingMethodsResponse200DataItemRelationshipsShippingZone.from_dict(_shipping_zone)

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingCategory]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = GETshippingMethodsResponse200DataItemRelationshipsShippingCategory.from_dict(
                _shipping_category
            )

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETshippingMethodsResponse200DataItemRelationshipsStockLocation.from_dict(_stock_location)

        _delivery_lead_time_for_shipment = d.pop("delivery_lead_time_for_shipment", UNSET)
        delivery_lead_time_for_shipment: Union[
            Unset, GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment
        ]
        if isinstance(_delivery_lead_time_for_shipment, Unset):
            delivery_lead_time_for_shipment = UNSET
        else:
            delivery_lead_time_for_shipment = (
                GETshippingMethodsResponse200DataItemRelationshipsDeliveryLeadTimeForShipment.from_dict(
                    _delivery_lead_time_for_shipment
                )
            )

        _shipping_method_tiers = d.pop("shipping_method_tiers", UNSET)
        shipping_method_tiers: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers]
        if isinstance(_shipping_method_tiers, Unset):
            shipping_method_tiers = UNSET
        else:
            shipping_method_tiers = GETshippingMethodsResponse200DataItemRelationshipsShippingMethodTiers.from_dict(
                _shipping_method_tiers
            )

        _shipping_weight_tiers = d.pop("shipping_weight_tiers", UNSET)
        shipping_weight_tiers: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers]
        if isinstance(_shipping_weight_tiers, Unset):
            shipping_weight_tiers = UNSET
        else:
            shipping_weight_tiers = GETshippingMethodsResponse200DataItemRelationshipsShippingWeightTiers.from_dict(
                _shipping_weight_tiers
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETshippingMethodsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETshippingMethodsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tshipping_methods_response_200_data_item_relationships = cls(
            market=market,
            shipping_zone=shipping_zone,
            shipping_category=shipping_category,
            stock_location=stock_location,
            delivery_lead_time_for_shipment=delivery_lead_time_for_shipment,
            shipping_method_tiers=shipping_method_tiers,
            shipping_weight_tiers=shipping_weight_tiers,
            attachments=attachments,
        )

        ge_tshipping_methods_response_200_data_item_relationships.additional_properties = d
        return ge_tshipping_methods_response_200_data_item_relationships

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
