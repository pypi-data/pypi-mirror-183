from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tstock_items_response_201_data_relationships_attachments import (
        POSTstockItemsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tstock_items_response_201_data_relationships_sku import (
        POSTstockItemsResponse201DataRelationshipsSku,
    )
    from ..models.pos_tstock_items_response_201_data_relationships_stock_location import (
        POSTstockItemsResponse201DataRelationshipsStockLocation,
    )


T = TypeVar("T", bound="POSTstockItemsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTstockItemsResponse201DataRelationships:
    """
    Attributes:
        stock_location (Union[Unset, POSTstockItemsResponse201DataRelationshipsStockLocation]):
        sku (Union[Unset, POSTstockItemsResponse201DataRelationshipsSku]):
        attachments (Union[Unset, POSTstockItemsResponse201DataRelationshipsAttachments]):
    """

    stock_location: Union[Unset, "POSTstockItemsResponse201DataRelationshipsStockLocation"] = UNSET
    sku: Union[Unset, "POSTstockItemsResponse201DataRelationshipsSku"] = UNSET
    attachments: Union[Unset, "POSTstockItemsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tstock_items_response_201_data_relationships_attachments import (
            POSTstockItemsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tstock_items_response_201_data_relationships_sku import (
            POSTstockItemsResponse201DataRelationshipsSku,
        )
        from ..models.pos_tstock_items_response_201_data_relationships_stock_location import (
            POSTstockItemsResponse201DataRelationshipsStockLocation,
        )

        d = src_dict.copy()
        _stock_location = d.pop("stock_location", UNSET)
        stock_location: Union[Unset, POSTstockItemsResponse201DataRelationshipsStockLocation]
        if isinstance(_stock_location, Unset):
            stock_location = UNSET
        else:
            stock_location = POSTstockItemsResponse201DataRelationshipsStockLocation.from_dict(_stock_location)

        _sku = d.pop("sku", UNSET)
        sku: Union[Unset, POSTstockItemsResponse201DataRelationshipsSku]
        if isinstance(_sku, Unset):
            sku = UNSET
        else:
            sku = POSTstockItemsResponse201DataRelationshipsSku.from_dict(_sku)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTstockItemsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTstockItemsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tstock_items_response_201_data_relationships = cls(
            stock_location=stock_location,
            sku=sku,
            attachments=attachments,
        )

        pos_tstock_items_response_201_data_relationships.additional_properties = d
        return pos_tstock_items_response_201_data_relationships

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
