from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization_data import (
        PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData,
    )
    from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization_links import (
        PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks,
    )


T = TypeVar("T", bound="PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization")


@attr.s(auto_attribs=True)
class PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorization:
    """
    Attributes:
        links (Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks]):
        data (Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData]):
    """

    links: Union[Unset, "PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks"] = UNSET
    data: Union[Unset, "PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData"] = UNSET
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
        from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization_data import (
            PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData,
        )
        from ..models.patc_hcapturescapture_id_response_200_data_relationships_reference_authorization_links import (
            PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationData.from_dict(_data)

        patc_hcapturescapture_id_response_200_data_relationships_reference_authorization = cls(
            links=links,
            data=data,
        )

        patc_hcapturescapture_id_response_200_data_relationships_reference_authorization.additional_properties = d
        return patc_hcapturescapture_id_response_200_data_relationships_reference_authorization

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
