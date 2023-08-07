from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.parcel_line_item_create_data_relationships_shipment_line_item_data import (
        ParcelLineItemCreateDataRelationshipsShipmentLineItemData,
    )


T = TypeVar("T", bound="ParcelLineItemCreateDataRelationshipsShipmentLineItem")


@attr.s(auto_attribs=True)
class ParcelLineItemCreateDataRelationshipsShipmentLineItem:
    """
    Attributes:
        data (ParcelLineItemCreateDataRelationshipsShipmentLineItemData):
    """

    data: "ParcelLineItemCreateDataRelationshipsShipmentLineItemData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parcel_line_item_create_data_relationships_shipment_line_item_data import (
            ParcelLineItemCreateDataRelationshipsShipmentLineItemData,
        )

        d = src_dict.copy()
        data = ParcelLineItemCreateDataRelationshipsShipmentLineItemData.from_dict(d.pop("data"))

        parcel_line_item_create_data_relationships_shipment_line_item = cls(
            data=data,
        )

        parcel_line_item_create_data_relationships_shipment_line_item.additional_properties = d
        return parcel_line_item_create_data_relationships_shipment_line_item

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
