from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tinventory_models_response_200_data_item_relationships_attachments import (
        GETinventoryModelsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tinventory_models_response_200_data_item_relationships_inventory_return_locations import (
        GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations,
    )
    from ..models.ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations import (
        GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations,
    )


T = TypeVar("T", bound="GETinventoryModelsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETinventoryModelsResponse200DataItemRelationships:
    """
    Attributes:
        inventory_stock_locations (Union[Unset,
            GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations]):
        inventory_return_locations (Union[Unset,
            GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations]):
        attachments (Union[Unset, GETinventoryModelsResponse200DataItemRelationshipsAttachments]):
    """

    inventory_stock_locations: Union[
        Unset, "GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations"
    ] = UNSET
    inventory_return_locations: Union[
        Unset, "GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations"
    ] = UNSET
    attachments: Union[Unset, "GETinventoryModelsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inventory_stock_locations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_stock_locations, Unset):
            inventory_stock_locations = self.inventory_stock_locations.to_dict()

        inventory_return_locations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_return_locations, Unset):
            inventory_return_locations = self.inventory_return_locations.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_stock_locations is not UNSET:
            field_dict["inventory_stock_locations"] = inventory_stock_locations
        if inventory_return_locations is not UNSET:
            field_dict["inventory_return_locations"] = inventory_return_locations
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tinventory_models_response_200_data_item_relationships_attachments import (
            GETinventoryModelsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tinventory_models_response_200_data_item_relationships_inventory_return_locations import (
            GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations,
        )
        from ..models.ge_tinventory_models_response_200_data_item_relationships_inventory_stock_locations import (
            GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations,
        )

        d = src_dict.copy()
        _inventory_stock_locations = d.pop("inventory_stock_locations", UNSET)
        inventory_stock_locations: Union[
            Unset, GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations
        ]
        if isinstance(_inventory_stock_locations, Unset):
            inventory_stock_locations = UNSET
        else:
            inventory_stock_locations = (
                GETinventoryModelsResponse200DataItemRelationshipsInventoryStockLocations.from_dict(
                    _inventory_stock_locations
                )
            )

        _inventory_return_locations = d.pop("inventory_return_locations", UNSET)
        inventory_return_locations: Union[
            Unset, GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations
        ]
        if isinstance(_inventory_return_locations, Unset):
            inventory_return_locations = UNSET
        else:
            inventory_return_locations = (
                GETinventoryModelsResponse200DataItemRelationshipsInventoryReturnLocations.from_dict(
                    _inventory_return_locations
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETinventoryModelsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETinventoryModelsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tinventory_models_response_200_data_item_relationships = cls(
            inventory_stock_locations=inventory_stock_locations,
            inventory_return_locations=inventory_return_locations,
            attachments=attachments,
        )

        ge_tinventory_models_response_200_data_item_relationships.additional_properties = d
        return ge_tinventory_models_response_200_data_item_relationships

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
