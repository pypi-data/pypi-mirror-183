from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tskussku_id_response_200_data_relationships_prices_data import (
        GETskusskuIdResponse200DataRelationshipsPricesData,
    )
    from ..models.ge_tskussku_id_response_200_data_relationships_prices_links import (
        GETskusskuIdResponse200DataRelationshipsPricesLinks,
    )


T = TypeVar("T", bound="GETskusskuIdResponse200DataRelationshipsPrices")


@attr.s(auto_attribs=True)
class GETskusskuIdResponse200DataRelationshipsPrices:
    """
    Attributes:
        links (Union[Unset, GETskusskuIdResponse200DataRelationshipsPricesLinks]):
        data (Union[Unset, GETskusskuIdResponse200DataRelationshipsPricesData]):
    """

    links: Union[Unset, "GETskusskuIdResponse200DataRelationshipsPricesLinks"] = UNSET
    data: Union[Unset, "GETskusskuIdResponse200DataRelationshipsPricesData"] = UNSET
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
        from ..models.ge_tskussku_id_response_200_data_relationships_prices_data import (
            GETskusskuIdResponse200DataRelationshipsPricesData,
        )
        from ..models.ge_tskussku_id_response_200_data_relationships_prices_links import (
            GETskusskuIdResponse200DataRelationshipsPricesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, GETskusskuIdResponse200DataRelationshipsPricesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GETskusskuIdResponse200DataRelationshipsPricesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GETskusskuIdResponse200DataRelationshipsPricesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GETskusskuIdResponse200DataRelationshipsPricesData.from_dict(_data)

        ge_tskussku_id_response_200_data_relationships_prices = cls(
            links=links,
            data=data,
        )

        ge_tskussku_id_response_200_data_relationships_prices.additional_properties = d
        return ge_tskussku_id_response_200_data_relationships_prices

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
