from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_torders_response_201_data_relationships_captures_data import (
        POSTordersResponse201DataRelationshipsCapturesData,
    )
    from ..models.pos_torders_response_201_data_relationships_captures_links import (
        POSTordersResponse201DataRelationshipsCapturesLinks,
    )


T = TypeVar("T", bound="POSTordersResponse201DataRelationshipsCaptures")


@attr.s(auto_attribs=True)
class POSTordersResponse201DataRelationshipsCaptures:
    """
    Attributes:
        links (Union[Unset, POSTordersResponse201DataRelationshipsCapturesLinks]):
        data (Union[Unset, POSTordersResponse201DataRelationshipsCapturesData]):
    """

    links: Union[Unset, "POSTordersResponse201DataRelationshipsCapturesLinks"] = UNSET
    data: Union[Unset, "POSTordersResponse201DataRelationshipsCapturesData"] = UNSET
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
        from ..models.pos_torders_response_201_data_relationships_captures_data import (
            POSTordersResponse201DataRelationshipsCapturesData,
        )
        from ..models.pos_torders_response_201_data_relationships_captures_links import (
            POSTordersResponse201DataRelationshipsCapturesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTordersResponse201DataRelationshipsCapturesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTordersResponse201DataRelationshipsCapturesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTordersResponse201DataRelationshipsCapturesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTordersResponse201DataRelationshipsCapturesData.from_dict(_data)

        pos_torders_response_201_data_relationships_captures = cls(
            links=links,
            data=data,
        )

        pos_torders_response_201_data_relationships_captures.additional_properties = d
        return pos_torders_response_201_data_relationships_captures

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
