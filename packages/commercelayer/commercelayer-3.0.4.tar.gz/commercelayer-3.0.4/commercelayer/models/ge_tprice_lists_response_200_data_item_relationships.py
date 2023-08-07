from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tprice_lists_response_200_data_item_relationships_attachments import (
        GETpriceListsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tprice_lists_response_200_data_item_relationships_prices import (
        GETpriceListsResponse200DataItemRelationshipsPrices,
    )


T = TypeVar("T", bound="GETpriceListsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETpriceListsResponse200DataItemRelationships:
    """
    Attributes:
        prices (Union[Unset, GETpriceListsResponse200DataItemRelationshipsPrices]):
        attachments (Union[Unset, GETpriceListsResponse200DataItemRelationshipsAttachments]):
    """

    prices: Union[Unset, "GETpriceListsResponse200DataItemRelationshipsPrices"] = UNSET
    attachments: Union[Unset, "GETpriceListsResponse200DataItemRelationshipsAttachments"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prices is not UNSET:
            field_dict["prices"] = prices
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ge_tprice_lists_response_200_data_item_relationships_attachments import (
            GETpriceListsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tprice_lists_response_200_data_item_relationships_prices import (
            GETpriceListsResponse200DataItemRelationshipsPrices,
        )

        d = src_dict.copy()
        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, GETpriceListsResponse200DataItemRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = GETpriceListsResponse200DataItemRelationshipsPrices.from_dict(_prices)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETpriceListsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETpriceListsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        ge_tprice_lists_response_200_data_item_relationships = cls(
            prices=prices,
            attachments=attachments,
        )

        ge_tprice_lists_response_200_data_item_relationships.additional_properties = d
        return ge_tprice_lists_response_200_data_item_relationships

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
