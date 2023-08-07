from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time_data import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData,
    )
    from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time_links import (
        PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks,
    )


T = TypeVar("T", bound="PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime")


@attr.s(auto_attribs=True)
class PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTime:
    """
    Attributes:
        links (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks]):
        data (Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData]):
    """

    links: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks"] = UNSET
    data: Union[Unset, "PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData"] = UNSET
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
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time_data import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData,
        )
        from ..models.patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time_links import (
            PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeData.from_dict(_data)

        patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time = cls(
            links=links,
            data=data,
        )

        patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time.additional_properties = d
        return patc_hshipmentsshipment_id_response_200_data_relationships_delivery_lead_time

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
