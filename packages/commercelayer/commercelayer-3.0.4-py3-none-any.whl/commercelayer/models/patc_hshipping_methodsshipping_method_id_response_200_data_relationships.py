from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_attachments import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_delivery_lead_time_for_shipment import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_market import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_category import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_method_tiers import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_weight_tiers import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_zone import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone,
    )
    from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_stock_location import (
        PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="PATCHshippingMethodsshippingMethodIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHshippingMethodsshippingMethodIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket]):
        shipping_zone (Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone]):
        shipping_category (Union[Unset,
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory]):
        stock_location (Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation]):
        delivery_lead_time_for_shipment (Union[Unset,
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment]):
        shipping_method_tiers (Union[Unset,
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers]):
        shipping_weight_tiers (Union[Unset,
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers]):
        attachments (Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments]):
    """

    market: Union[Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket"] = UNSET
    shipping_zone: Union[Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone"] = UNSET
    shipping_category: Union[
        Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory"
    ] = UNSET
    stock_location: Union[
        Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation"
    ] = UNSET
    delivery_lead_time_for_shipment: Union[
        Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment"
    ] = UNSET
    shipping_method_tiers: Union[
        Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers"
    ] = UNSET
    shipping_weight_tiers: Union[
        Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers"
    ] = UNSET
    attachments: Union[Unset, "PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_attachments import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_delivery_lead_time_for_shipment import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_market import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_category import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_method_tiers import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_weight_tiers import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_shipping_zone import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone,
        )
        from ..models.patc_hshipping_methodsshipping_method_id_response_200_data_relationships_stock_location import (
            PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsMarket.from_dict(_market)

        _shipping_zone = d.pop("shipping_zone", UNSET)
        shipping_zone: Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone]
        if isinstance(_shipping_zone, Unset):
            shipping_zone = UNSET
        else:
            shipping_zone = PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingZone.from_dict(
                _shipping_zone
            )

        _shipping_category = d.pop("shipping_category", UNSET)
        shipping_category: Union[
            Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory
        ]
        if isinstance(_shipping_category, Unset):
            shipping_category = UNSET
        else:
            shipping_category = (
                PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingCategory.from_dict(
                    _shipping_category
                )
            )

        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsStockLocation.from_dict(
                _stock_location
            )

        _delivery_lead_time_for_shipment = d.pop("delivery_lead_time_for_shipment", UNSET)
        delivery_lead_time_for_shipment: Union[
            Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment
        ]
        if isinstance(_delivery_lead_time_for_shipment, Unset):
            delivery_lead_time_for_shipment = UNSET
        else:
            delivery_lead_time_for_shipment = (
                PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsDeliveryLeadTimeForShipment.from_dict(
                    _delivery_lead_time_for_shipment
                )
            )

        _shipping_method_tiers = d.pop("shipping_method_tiers", UNSET)
        shipping_method_tiers: Union[
            Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers
        ]
        if isinstance(_shipping_method_tiers, Unset):
            shipping_method_tiers = UNSET
        else:
            shipping_method_tiers = (
                PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingMethodTiers.from_dict(
                    _shipping_method_tiers
                )
            )

        _shipping_weight_tiers = d.pop("shipping_weight_tiers", UNSET)
        shipping_weight_tiers: Union[
            Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers
        ]
        if isinstance(_shipping_weight_tiers, Unset):
            shipping_weight_tiers = UNSET
        else:
            shipping_weight_tiers = (
                PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsShippingWeightTiers.from_dict(
                    _shipping_weight_tiers
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHshippingMethodsshippingMethodIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        patc_hshipping_methodsshipping_method_id_response_200_data_relationships = cls(
            market=market,
            shipping_zone=shipping_zone,
            shipping_category=shipping_category,
            stock_location=stock_location,
            delivery_lead_time_for_shipment=delivery_lead_time_for_shipment,
            shipping_method_tiers=shipping_method_tiers,
            shipping_weight_tiers=shipping_weight_tiers,
            attachments=attachments,
        )

        patc_hshipping_methodsshipping_method_id_response_200_data_relationships.additional_properties = d
        return patc_hshipping_methodsshipping_method_id_response_200_data_relationships

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
