from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hskussku_id_response_200_data_relationships_delivery_lead_times_data import (
        PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData,
    )
    from ..models.patc_hskussku_id_response_200_data_relationships_delivery_lead_times_links import (
        PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks,
    )


T = TypeVar("T", bound="PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimes")


@attr.s(auto_attribs=True)
class PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimes:
    """
    Attributes:
        links (Union[Unset, PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks]):
        data (Union[Unset, PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData]):
    """

    links: Union[Unset, "PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks"] = UNSET
    data: Union[Unset, "PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData"] = UNSET
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
        from ..models.patc_hskussku_id_response_200_data_relationships_delivery_lead_times_data import (
            PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData,
        )
        from ..models.patc_hskussku_id_response_200_data_relationships_delivery_lead_times_links import (
            PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHskusskuIdResponse200DataRelationshipsDeliveryLeadTimesData.from_dict(_data)

        patc_hskussku_id_response_200_data_relationships_delivery_lead_times = cls(
            links=links,
            data=data,
        )

        patc_hskussku_id_response_200_data_relationships_delivery_lead_times.additional_properties = d
        return patc_hskussku_id_response_200_data_relationships_delivery_lead_times

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
