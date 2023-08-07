from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events_data import (
        PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData,
    )
    from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events_links import (
        PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks,
    )


T = TypeVar("T", bound="PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEvents")


@attr.s(auto_attribs=True)
class PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEvents:
    """
    Attributes:
        links (Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks]):
        data (Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData]):
    """

    links: Union[Unset, "PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks"] = UNSET
    data: Union[Unset, "PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData"] = UNSET
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
        from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events_data import (
            PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData,
        )
        from ..models.patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events_links import (
            PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHstockTransfersstockTransferIdResponse200DataRelationshipsEventsData.from_dict(_data)

        patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events = cls(
            links=links,
            data=data,
        )

        patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events.additional_properties = d
        return patc_hstock_transfersstock_transfer_id_response_200_data_relationships_events

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
