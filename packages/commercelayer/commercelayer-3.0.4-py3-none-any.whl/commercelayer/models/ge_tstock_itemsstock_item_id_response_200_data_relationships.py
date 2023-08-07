from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_attachments import (
        GETstockItemsstockItemIdResponse200DataRelationshipsAttachments,
    )
    from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_sku import (
        GETstockItemsstockItemIdResponse200DataRelationshipsSku,
    )
    from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_stock_location import (
        GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETstockItemsstockItemIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class GETstockItemsstockItemIdResponse200DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation]):
        sku (Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsSku]):
        attachments (Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation"] = UNSET
    sku: Union[Unset, "GETstockItemsstockItemIdResponse200DataRelationshipsSku"] = UNSET
    attachments: Union[Unset, "GETstockItemsstockItemIdResponse200DataRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_location, Unset):
            stock_location = self.stock_location.to_dict()

        sku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku, Unset):
            sku = self.sku.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if sku is not UNSET:
            field_dict["sku"] = sku
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_attachments import (
            GETstockItemsstockItemIdResponse200DataRelationshipsAttachments,
        )
        from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_sku import (
            GETstockItemsstockItemIdResponse200DataRelationshipsSku,
        )
        from ..models.ge_tstock_itemsstock_item_id_response_200_data_relationships_stock_location import (
            GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETstockItemsstockItemIdResponse200DataRelationshipsStockLocation.from_dict(
                _stock_location
            )

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETstockItemsstockItemIdResponse200DataRelationshipsSku.from_dict(_sku)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETstockItemsstockItemIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETstockItemsstockItemIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        ge_tstock_itemsstock_item_id_response_200_data_relationships = cls(
            stock_location=stock_location,
            sku=sku,
            attachments=attachments,
        )

        ge_tstock_itemsstock_item_id_response_200_data_relationships.additional_properties = d
        return ge_tstock_itemsstock_item_id_response_200_data_relationships

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
