from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model_data import (
        PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData,
    )
    from ..models.patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model_links import (
        PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks,
    )


T = TypeVar(
    "T", bound="PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModel"
)


@attr.s(auto_attribs=True)
class PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModel:
    """
    Attributes:
        links (Union[Unset,
            PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks]):
        data (Union[Unset,
            PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData]):
    """

    links: Union[
        Unset, "PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks"
    ] = UNSET
    data: Union[
        Unset, "PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData"
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
        from ..models.patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model_data import (
            PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData,
        )
        from ..models.patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model_links import (
            PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[
            Unset, PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks
        ]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelLinks.from_dict(
                _links
            )

        _data = d.pop("data", UNSET)
        data: Union[
            Unset, PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData
        ]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200DataRelationshipsInventoryModelData.from_dict(
                _data
            )

        patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model = (
            cls(
                links=links,
                data=data,
            )
        )

        patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model.additional_properties = (
            d
        )
        return (
            patc_hinventory_return_locationsinventory_return_location_id_response_200_data_relationships_inventory_model
        )

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
