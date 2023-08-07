from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tskus_response_201_data_relationships_prices_data import (
        POSTskusResponse201DataRelationshipsPricesData,
    )
    from ..models.pos_tskus_response_201_data_relationships_prices_links import (
        POSTskusResponse201DataRelationshipsPricesLinks,
    )


T = TypeVar("T", bound="POSTskusResponse201DataRelationshipsPrices")


@attr.s(auto_attribs=True)
class POSTskusResponse201DataRelationshipsPrices:
    """
    Attributes:
        links (Union[Unset, POSTskusResponse201DataRelationshipsPricesLinks]):
        data (Union[Unset, POSTskusResponse201DataRelationshipsPricesData]):
    """

    links: Union[Unset, "POSTskusResponse201DataRelationshipsPricesLinks"] = UNSET
    data: Union[Unset, "POSTskusResponse201DataRelationshipsPricesData"] = UNSET
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
        from ..models.pos_tskus_response_201_data_relationships_prices_data import (
            POSTskusResponse201DataRelationshipsPricesData,
        )
        from ..models.pos_tskus_response_201_data_relationships_prices_links import (
            POSTskusResponse201DataRelationshipsPricesLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTskusResponse201DataRelationshipsPricesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTskusResponse201DataRelationshipsPricesLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTskusResponse201DataRelationshipsPricesData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTskusResponse201DataRelationshipsPricesData.from_dict(_data)

        pos_tskus_response_201_data_relationships_prices = cls(
            links=links,
            data=data,
        )

        pos_tskus_response_201_data_relationships_prices.additional_properties = d
        return pos_tskus_response_201_data_relationships_prices

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
