from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_items_response_200_data_item_relationships_attachments import (
        GETstockItemsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tstock_items_response_200_data_item_relationships_sku import (
        GETstockItemsResponse200DataItemRelationshipsSku,
    )
    from ..models.ge_tstock_items_response_200_data_item_relationships_stock_location import (
        GETstockItemsResponse200DataItemRelationshipsStockLocation,
    )


T = TypeVar("T", bound="GETstockItemsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETstockItemsResponse200DataItemRelationships:
    """
    Attributes:
        stock_location (Union[Unset, GETstockItemsResponse200DataItemRelationshipsStockLocation]):
        sku (Union[Unset, GETstockItemsResponse200DataItemRelationshipsSku]):
        attachments (Union[Unset, GETstockItemsResponse200DataItemRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "GETstockItemsResponse200DataItemRelationshipsStockLocation"] = UNSET
    sku: Union[Unset, "GETstockItemsResponse200DataItemRelationshipsSku"] = UNSET
    attachments: Union[Unset, "GETstockItemsResponse200DataItemRelationshipsAttachments"] = UNSET
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
        from ..models.ge_tstock_items_response_200_data_item_relationships_attachments import (
            GETstockItemsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tstock_items_response_200_data_item_relationships_sku import (
            GETstockItemsResponse200DataItemRelationshipsSku,
        )
        from ..models.ge_tstock_items_response_200_data_item_relationships_stock_location import (
            GETstockItemsResponse200DataItemRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, GETstockItemsResponse200DataItemRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = GETstockItemsResponse200DataItemRelationshipsStockLocation.from_dict(_stock_location)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, GETstockItemsResponse200DataItemRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = GETstockItemsResponse200DataItemRelationshipsSku.from_dict(_sku)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETstockItemsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETstockItemsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tstock_items_response_200_data_item_relationships = cls(
            stock_location=stock_location,
            sku=sku,
            attachments=attachments,
        )

        ge_tstock_items_response_200_data_item_relationships.additional_properties = d
        return ge_tstock_items_response_200_data_item_relationships

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
