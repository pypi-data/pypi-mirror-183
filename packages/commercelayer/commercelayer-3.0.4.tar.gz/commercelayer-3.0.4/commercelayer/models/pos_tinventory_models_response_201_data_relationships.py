from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tinventory_models_response_201_data_relationships_attachments import (
        POSTinventoryModelsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tinventory_models_response_201_data_relationships_inventory_return_locations import (
        POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations,
    )
    from ..models.pos_tinventory_models_response_201_data_relationships_inventory_stock_locations import (
        POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations,
    )


T = TypeVar("T", bound="POSTinventoryModelsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTinventoryModelsResponse201DataRelationships:
    """
    Attributes:
        inventory_stock_locations (Union[Unset,
            POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations]):
        inventory_return_locations (Union[Unset,
            POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations]):
        attachments (Union[Unset, POSTinventoryModelsResponse201DataRelationshipsAttachments]):
    """

    inventory_stock_locations: Union[
        Unset, "POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations"
    ] = UNSET
    inventory_return_locations: Union[
        Unset, "POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations"
    ] = UNSET
    attachments: Union[Unset, "POSTinventoryModelsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tinventory_models_response_201_data_relationships_attachments import (
            POSTinventoryModelsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tinventory_models_response_201_data_relationships_inventory_return_locations import (
            POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations,
        )
        from ..models.pos_tinventory_models_response_201_data_relationships_inventory_stock_locations import (
            POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations,
        )

        d = src_dict.copy()
        _inventory_stock_locations = d.pop("inventory_stock_locations", UNSET)
        inventory_stock_locations: Union[Unset, POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations]
        if isinstance(_inventory_stock_locations, Unset):
            inventory_stock_locations = UNSET
        else:
            inventory_stock_locations = (
                POSTinventoryModelsResponse201DataRelationshipsInventoryStockLocations.from_dict(
                    _inventory_stock_locations
                )
            )

        _inventory_return_locations = d.pop("inventory_return_locations", UNSET)
        inventory_return_locations: Union[
            Unset, POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations
        ]
        if isinstance(_inventory_return_locations, Unset):
            inventory_return_locations = UNSET
        else:
            inventory_return_locations = (
                POSTinventoryModelsResponse201DataRelationshipsInventoryReturnLocations.from_dict(
                    _inventory_return_locations
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTinventoryModelsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTinventoryModelsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tinventory_models_response_201_data_relationships = cls(
            inventory_stock_locations=inventory_stock_locations,
            inventory_return_locations=inventory_return_locations,
            attachments=attachments,
        )

        pos_tinventory_models_response_201_data_relationships.additional_properties = d
        return pos_tinventory_models_response_201_data_relationships

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
