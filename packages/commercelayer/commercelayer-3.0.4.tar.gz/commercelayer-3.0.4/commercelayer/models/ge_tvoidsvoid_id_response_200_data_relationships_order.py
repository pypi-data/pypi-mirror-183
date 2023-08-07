from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tvoidsvoid_id_response_200_data_relationships_order_data import (
        GETvoidsvoidIdResponse200DataRelationshipsOrderData,
    )
    from ..models.ge_tvoidsvoid_id_response_200_data_relationships_order_links import (
        GETvoidsvoidIdResponse200DataRelationshipsOrderLinks,
    )


T = TypeVar("T", bound="GETvoidsvoidIdResponse200DataRelationshipsOrder")


@attr.s(auto_attribs=True)
class GETvoidsvoidIdResponse200DataRelationshipsOrder:
    """
    Attributes:
        links (Union[Unset, GETvoidsvoidIdResponse200DataRelationshipsOrderLinks]):
        data (Union[Unset, GETvoidsvoidIdResponse200DataRelationshipsOrderData]):
    """

    links: Union[Unset, "GETvoidsvoidIdResponse200DataRelationshipsOrderLinks"] = UNSET
    data: Union[Unset, "GETvoidsvoidIdResponse200DataRelationshipsOrderData"] = UNSET
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
        from ..models.ge_tvoidsvoid_id_response_200_data_relationships_order_data import (
            GETvoidsvoidIdResponse200DataRelationshipsOrderData,
        )
        from ..models.ge_tvoidsvoid_id_response_200_data_relationships_order_links import (
            GETvoidsvoidIdResponse200DataRelationshipsOrderLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETvoidsvoidIdResponse200DataRelationshipsOrderLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETvoidsvoidIdResponse200DataRelationshipsOrderLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETvoidsvoidIdResponse200DataRelationshipsOrderData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETvoidsvoidIdResponse200DataRelationshipsOrderData.from_dict(_data)

        ge_tvoidsvoid_id_response_200_data_relationships_order = cls(
            links=links,
            data=data,
        )

        ge_tvoidsvoid_id_response_200_data_relationships_order.additional_properties = d
        return ge_tvoidsvoid_id_response_200_data_relationships_order

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
