from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hprice_listsprice_list_id_response_200_data_relationships_attachments import (
        PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hprice_listsprice_list_id_response_200_data_relationships_prices import (
        PATCHpriceListspriceListIdResponse200DataRelationshipsPrices,
    )


T = TypeVar("T", bound="PATCHpriceListspriceListIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHpriceListspriceListIdResponse200DataRelationships:
    """
    Attributes:
        prices (Union[Unset, PATCHpriceListspriceListIdResponse200DataRelationshipsPrices]):
        attachments (Union[Unset, PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments]):
    """

    prices: Union[Unset, "PATCHpriceListspriceListIdResponse200DataRelationshipsPrices"] = UNSET
    attachments: Union[Unset, "PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments"] = UNSET
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
        from ..models.patc_hprice_listsprice_list_id_response_200_data_relationships_attachments import (
            PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hprice_listsprice_list_id_response_200_data_relationships_prices import (
            PATCHpriceListspriceListIdResponse200DataRelationshipsPrices,
        )

        d = src_dict.copy()
        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, PATCHpriceListspriceListIdResponse200DataRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = PATCHpriceListspriceListIdResponse200DataRelationshipsPrices.from_dict(_prices)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHpriceListspriceListIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        patc_hprice_listsprice_list_id_response_200_data_relationships = cls(
            prices=prices,
            attachments=attachments,
        )

        patc_hprice_listsprice_list_id_response_200_data_relationships.additional_properties = d
        return patc_hprice_listsprice_list_id_response_200_data_relationships

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
