from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tsku_options_response_200_data_item_relationships_attachments import (
        GETskuOptionsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tsku_options_response_200_data_item_relationships_market import (
        GETskuOptionsResponse200DataItemRelationshipsMarket,
    )


T = TypeVar("T", bound="GETskuOptionsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETskuOptionsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETskuOptionsResponse200DataItemRelationshipsMarket]):
        attachments (Union[Unset, GETskuOptionsResponse200DataItemRelationshipsAttachments]):
    """

    market: Union[Unset, "GETskuOptionsResponse200DataItemRelationshipsMarket"] = UNSET
    attachments: Union[Unset, "GETskuOptionsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tsku_options_response_200_data_item_relationships_attachments import (
            GETskuOptionsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tsku_options_response_200_data_item_relationships_market import (
            GETskuOptionsResponse200DataItemRelationshipsMarket,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETskuOptionsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETskuOptionsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETskuOptionsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETskuOptionsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tsku_options_response_200_data_item_relationships = cls(
            market=market,
            attachments=attachments,
        )

        ge_tsku_options_response_200_data_item_relationships.additional_properties = d
        return ge_tsku_options_response_200_data_item_relationships

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
