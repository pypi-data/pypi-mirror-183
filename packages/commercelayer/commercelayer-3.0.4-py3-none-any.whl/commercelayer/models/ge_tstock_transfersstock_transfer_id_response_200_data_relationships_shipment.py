from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment_data import (
        GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData,
    )
    from ..models.ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment_links import (
        GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks,
    )


T = TypeVar("T", bound="GETstockTransfersstockTransferIdResponse200DataRelationshipsShipment")


@attr.s(auto_attribs=True)
class GETstockTransfersstockTransferIdResponse200DataRelationshipsShipment:
    """
    Attributes:
        links (Union[Unset, GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks]):
        data (Union[Unset, GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData]):
    """

    links: Union[Unset, "GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks"] = UNSET
    data: Union[Unset, "GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData"] = UNSET
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
        from ..models.ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment_data import (
            GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData,
        )
        from ..models.ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment_links import (
            GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETstockTransfersstockTransferIdResponse200DataRelationshipsShipmentData.from_dict(_data)

        ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment = cls(
            links=links,
            data=data,
        )

        ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment.additional_properties = d
        return ge_tstock_transfersstock_transfer_id_response_200_data_relationships_shipment

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
