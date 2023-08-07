from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_returns_data import (
        PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData,
    )
    from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_returns_links import (
        PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks,
    )


T = TypeVar("T", bound="PATCHcustomerscustomerIdResponse200DataRelationshipsReturns")


@attr.s(auto_attribs=True)
class PATCHcustomerscustomerIdResponse200DataRelationshipsReturns:
    """
    Attributes:
        links (Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks]):
        data (Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData]):
    """

    links: Union[Unset, "PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks"] = UNSET
    data: Union[Unset, "PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData"] = UNSET
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
        from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_returns_data import (
            PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData,
        )
        from ..models.patc_hcustomerscustomer_id_response_200_data_relationships_returns_links import (
            PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsData.from_dict(_data)

        patc_hcustomerscustomer_id_response_200_data_relationships_returns = cls(
            links=links,
            data=data,
        )

        patc_hcustomerscustomer_id_response_200_data_relationships_returns.additional_properties = d
        return patc_hcustomerscustomer_id_response_200_data_relationships_returns

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
