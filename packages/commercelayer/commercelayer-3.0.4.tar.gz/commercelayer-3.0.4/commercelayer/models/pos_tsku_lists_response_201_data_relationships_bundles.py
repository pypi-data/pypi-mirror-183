from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tsku_lists_response_201_data_relationships_bundles_data import (
        POSTskuListsResponse201DataRelationshipsBundlesData,
    )
    from ..models.pos_tsku_lists_response_201_data_relationships_bundles_links import (
        POSTskuListsResponse201DataRelationshipsBundlesLinks,
    )


T = TypeVar("T", bound="POSTskuListsResponse201DataRelationshipsBundles")


@attr.s(auto_attribs=True)
class POSTskuListsResponse201DataRelationshipsBundles:
    """
    Attributes:
        links (Union[Unset, POSTskuListsResponse201DataRelationshipsBundlesLinks]):
        data (Union[Unset, POSTskuListsResponse201DataRelationshipsBundlesData]):
    """

    links: Union[Unset, "POSTskuListsResponse201DataRelationshipsBundlesLinks"] = UNSET
    data: Union[Unset, "POSTskuListsResponse201DataRelationshipsBundlesData"] = UNSET
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
        from ..models.pos_tsku_lists_response_201_data_relationships_bundles_data import (
            POSTskuListsResponse201DataRelationshipsBundlesData,
        )
        from ..models.pos_tsku_lists_response_201_data_relationships_bundles_links import (
            POSTskuListsResponse201DataRelationshipsBundlesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTskuListsResponse201DataRelationshipsBundlesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTskuListsResponse201DataRelationshipsBundlesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTskuListsResponse201DataRelationshipsBundlesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTskuListsResponse201DataRelationshipsBundlesData.from_dict(_data)

        pos_tsku_lists_response_201_data_relationships_bundles = cls(
            links=links,
            data=data,
        )

        pos_tsku_lists_response_201_data_relationships_bundles.additional_properties = d
        return pos_tsku_lists_response_201_data_relationships_bundles

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
