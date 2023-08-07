from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations_data import (
        GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData,
    )
    from ..models.ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations_links import (
        GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks,
    )


T = TypeVar("T", bound="GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocations")


@attr.s(auto_attribs=True)
class GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocations:
    """
    Attributes:
        links (Union[Unset,
            GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks]):
        data (Union[Unset, GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData]):
    """

    links: Union[
        Unset, "GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks"
    ] = UNSET
    data: Union[
        Unset, "GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData"
    ] = UNSET
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
        from ..models.ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations_data import (
            GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData,
        )
        from ..models.ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations_links import (
            GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = (
                GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsLinks.from_dict(
                    _links
                )
            )

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETinventoryModelsinventoryModelIdResponse200DataRelationshipsInventoryReturnLocationsData.from_dict(
                _data
            )

        ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations = cls(
            links=links,
            data=data,
        )

        ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations.additional_properties = (
            d
        )
        return ge_tinventory_modelsinventory_model_id_response_200_data_relationships_inventory_return_locations

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
