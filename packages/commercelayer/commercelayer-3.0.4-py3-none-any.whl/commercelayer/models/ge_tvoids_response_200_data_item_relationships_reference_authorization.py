from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tvoids_response_200_data_item_relationships_reference_authorization_data import (
        GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData,
    )
    from ..models.ge_tvoids_response_200_data_item_relationships_reference_authorization_links import (
        GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks,
    )


T = TypeVar("T", bound="GETvoidsResponse200DataItemRelationshipsReferenceAuthorization")


@attr.s(auto_attribs=True)
class GETvoidsResponse200DataItemRelationshipsReferenceAuthorization:
    """
    Attributes:
        links (Union[Unset, GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks]):
        data (Union[Unset, GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData]):
    """

    links: Union[Unset, "GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks"] = UNSET
    data: Union[Unset, "GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData"] = UNSET
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
        from ..models.ge_tvoids_response_200_data_item_relationships_reference_authorization_data import (
            GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData,
        )
        from ..models.ge_tvoids_response_200_data_item_relationships_reference_authorization_links import (
            GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationData.from_dict(_data)

        ge_tvoids_response_200_data_item_relationships_reference_authorization = cls(
            links=links,
            data=data,
        )

        ge_tvoids_response_200_data_item_relationships_reference_authorization.additional_properties = d
        return ge_tvoids_response_200_data_item_relationships_reference_authorization

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
