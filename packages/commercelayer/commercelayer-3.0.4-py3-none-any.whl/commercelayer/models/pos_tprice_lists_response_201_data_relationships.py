from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tprice_lists_response_201_data_relationships_attachments import (
        POSTpriceListsResponse201DataRelationshipsAttachments,
    )
    from ..models.pos_tprice_lists_response_201_data_relationships_prices import (
        POSTpriceListsResponse201DataRelationshipsPrices,
    )


T = TypeVar("T", bound="POSTpriceListsResponse201DataRelationships")


@attr.s(auto_attribs=True)
class POSTpriceListsResponse201DataRelationships:
    """
    Attributes:
        prices (Union[Unset, POSTpriceListsResponse201DataRelationshipsPrices]):
        attachments (Union[Unset, POSTpriceListsResponse201DataRelationshipsAttachments]):
    """

    prices: Union[Unset, "POSTpriceListsResponse201DataRelationshipsPrices"] = UNSET
    attachments: Union[Unset, "POSTpriceListsResponse201DataRelationshipsAttachments"] = UNSET
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
        from ..models.pos_tprice_lists_response_201_data_relationships_attachments import (
            POSTpriceListsResponse201DataRelationshipsAttachments,
        )
        from ..models.pos_tprice_lists_response_201_data_relationships_prices import (
            POSTpriceListsResponse201DataRelationshipsPrices,
        )

        d = src_dict.copy()
        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, POSTpriceListsResponse201DataRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = POSTpriceListsResponse201DataRelationshipsPrices.from_dict(_prices)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, POSTpriceListsResponse201DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = POSTpriceListsResponse201DataRelationshipsAttachments.from_dict(_attachments)

        pos_tprice_lists_response_201_data_relationships = cls(
            prices=prices,
            attachments=attachments,
        )

        pos_tprice_lists_response_201_data_relationships.additional_properties = d
        return pos_tprice_lists_response_201_data_relationships

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
