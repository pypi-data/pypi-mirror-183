from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_attachments import (
        GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_shipping_method import (
        GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod,
    )
    from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_stock_location import (
        GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation]):
        shipping_method (Union[Unset,
            GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod]):
        attachments (Union[Unset, GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments]):
    """

    stock_location: Union[
        Unset, "GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation"
    ] = UNSET
    shipping_method: Union[
        Unset, "GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod"
    ] = UNSET
    attachments: Union[Unset, "GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        shipping_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method, Unset):
            shipping_method = self.shipping_method.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_attachments import (
            GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_shipping_method import (
            GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod,
        )
        from ..models.ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships_stock_location import (
            GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsStockLocation.from_dict(
                _stock_location
            )

        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = (
                GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsShippingMethod.from_dict(
                    _shipping_method
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETdeliveryLeadTimesdeliveryLeadTimeIdResponse200DataRelationshipsAttachments.from_dict(
                _attachments
            )

        ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships = cls(
            stock_location=stock_location,
            shipping_method=shipping_method,
            attachments=attachments,
        )

        ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships.additional_properties = d
        return ge_tdelivery_lead_timesdelivery_lead_time_id_response_200_data_relationships

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
