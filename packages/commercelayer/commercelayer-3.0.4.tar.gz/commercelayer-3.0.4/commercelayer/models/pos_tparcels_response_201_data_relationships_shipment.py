from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tparcels_response_201_data_relationships_shipment_data import (
        POSTparcelsResponse201DataRelationshipsShipmentData,
    )
    from ..models.pos_tparcels_response_201_data_relationships_shipment_links import (
        POSTparcelsResponse201DataRelationshipsShipmentLinks,
    )


T = TypeVar("T", bound="POSTparcelsResponse201DataRelationshipsShipment")


@attr.s(auto_attribs=True)
class POSTparcelsResponse201DataRelationshipsShipment:
    """
    Attributes:
        links (Union[Unset, POSTparcelsResponse201DataRelationshipsShipmentLinks]):
        data (Union[Unset, POSTparcelsResponse201DataRelationshipsShipmentData]):
    """

    links: Union[Unset, "POSTparcelsResponse201DataRelationshipsShipmentLinks"] = UNSET
    data: Union[Unset, "POSTparcelsResponse201DataRelationshipsShipmentData"] = UNSET
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
        from ..models.pos_tparcels_response_201_data_relationships_shipment_data import (
            POSTparcelsResponse201DataRelationshipsShipmentData,
        )
        from ..models.pos_tparcels_response_201_data_relationships_shipment_links import (
            POSTparcelsResponse201DataRelationshipsShipmentLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTparcelsResponse201DataRelationshipsShipmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTparcelsResponse201DataRelationshipsShipmentLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTparcelsResponse201DataRelationshipsShipmentData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTparcelsResponse201DataRelationshipsShipmentData.from_dict(_data)

        pos_tparcels_response_201_data_relationships_shipment = cls(
            links=links,
            data=data,
        )

        pos_tparcels_response_201_data_relationships_shipment.additional_properties = d
        return pos_tparcels_response_201_data_relationships_shipment

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
