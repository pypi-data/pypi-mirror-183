from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment_data import (
        POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData,
    )
    from ..models.pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment_links import (
        POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks,
    )


T = TypeVar("T", bound="POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipment")


@attr.s(auto_attribs=True)
class POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipment:
    """
    Attributes:
        links (Union[Unset, POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks]):
        data (Union[Unset, POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData]):
    """

    links: Union[Unset, "POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks"] = UNSET
    data: Union[Unset, "POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData"] = UNSET
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
        from ..models.pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment_data import (
            POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData,
        )
        from ..models.pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment_links import (
            POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTshippingMethodsResponse201DataRelationshipsDeliveryLeadTimeForShipmentData.from_dict(_data)

        pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment = cls(
            links=links,
            data=data,
        )

        pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment.additional_properties = d
        return pos_tshipping_methods_response_201_data_relationships_delivery_lead_time_for_shipment

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
