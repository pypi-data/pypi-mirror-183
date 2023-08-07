from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_ttax_calculators_response_200_data_item_relationships_attachments import (
        GETtaxCalculatorsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_ttax_calculators_response_200_data_item_relationships_markets import (
        GETtaxCalculatorsResponse200DataItemRelationshipsMarkets,
    )


T = TypeVar("T", bound="GETtaxCalculatorsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETtaxCalculatorsResponse200DataItemRelationships:
    """
    Attributes:
        markets (Union[Unset, GETtaxCalculatorsResponse200DataItemRelationshipsMarkets]):
        attachments (Union[Unset, GETtaxCalculatorsResponse200DataItemRelationshipsAttachments]):
    """

    markets: Union[Unset, "GETtaxCalculatorsResponse200DataItemRelationshipsMarkets"] = UNSET
    attachments: Union[Unset, "GETtaxCalculatorsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markets is not UNSET:
            field_dict["markets"] = markets
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_ttax_calculators_response_200_data_item_relationships_attachments import (
            GETtaxCalculatorsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_ttax_calculators_response_200_data_item_relationships_markets import (
            GETtaxCalculatorsResponse200DataItemRelationshipsMarkets,
        )

        d = src_dict.copy()
        _markets = d.pop("markets", UNSET)
        markets: Union[Unset, GETtaxCalculatorsResponse200DataItemRelationshipsMarkets]
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = GETtaxCalculatorsResponse200DataItemRelationshipsMarkets.from_dict(_markets)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETtaxCalculatorsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETtaxCalculatorsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_ttax_calculators_response_200_data_item_relationships = cls(
            markets=markets,
            attachments=attachments,
        )

        ge_ttax_calculators_response_200_data_item_relationships.additional_properties = d
        return ge_ttax_calculators_response_200_data_item_relationships

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
