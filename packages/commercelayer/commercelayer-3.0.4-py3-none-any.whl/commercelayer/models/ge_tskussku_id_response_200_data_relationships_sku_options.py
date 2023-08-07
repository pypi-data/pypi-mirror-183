from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tskussku_id_response_200_data_relationships_sku_options_data import (
        GETskusskuIdResponse200DataRelationshipsSkuOptionsData,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_sku_options_links import (
        GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks,
    )


T = TypeVar("T", bound="GETskusskuIdResponse200DataRelationshipsSkuOptions")


@attr.s(auto_attribs=True)
class GETskusskuIdResponse200DataRelationshipsSkuOptions:
    """
    Attributes:
        links (Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks]):
        data (Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptionsData]):
    """

    links: Union[Unset, "GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks"] = UNSET
    data: Union[Unset, "GETskusskuIdResponse200DataRelationshipsSkuOptionsData"] = UNSET
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
        from ..models.ge_tskussku_id_response_200_data_relationships_sku_options_data import (
            GETskusskuIdResponse200DataRelationshipsSkuOptionsData,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_sku_options_links import (
            GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETskusskuIdResponse200DataRelationshipsSkuOptionsLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETskusskuIdResponse200DataRelationshipsSkuOptionsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETskusskuIdResponse200DataRelationshipsSkuOptionsData.from_dict(_data)

        ge_tskussku_id_response_200_data_relationships_sku_options = cls(
            links=links,
            data=data,
        )

        ge_tskussku_id_response_200_data_relationships_sku_options.additional_properties = d
        return ge_tskussku_id_response_200_data_relationships_sku_options

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
