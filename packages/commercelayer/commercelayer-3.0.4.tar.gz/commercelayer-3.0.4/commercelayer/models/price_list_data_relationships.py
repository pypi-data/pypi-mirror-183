from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_list_data_relationships_attachments import PriceListDataRelationshipsAttachments
    from ..models.price_list_data_relationships_prices import PriceListDataRelationshipsPrices


T = TypeVar("T", bound="PriceListDataRelationships")


@attr.s(auto_attribs=True)
class PriceListDataRelationships:
    """
    Attributes:
        prices (Union[Unset, PriceListDataRelationshipsPrices]):
        attachments (Union[Unset, PriceListDataRelationshipsAttachments]):
    """

    prices: Union[Unset, "PriceListDataRelationshipsPrices"] = UNSET
    attachments: Union[Unset, "PriceListDataRelationshipsAttachments"] = UNSET
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
        from ..models.price_list_data_relationships_attachments import PriceListDataRelationshipsAttachments
        from ..models.price_list_data_relationships_prices import PriceListDataRelationshipsPrices

        d = src_dict.copy()
        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, PriceListDataRelationshipsPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = PriceListDataRelationshipsPrices.from_dict(_prices)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PriceListDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PriceListDataRelationshipsAttachments.from_dict(_attachments)

        price_list_data_relationships = cls(
            prices=prices,
            attachments=attachments,
        )

        price_list_data_relationships.additional_properties = d
        return price_list_data_relationships

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
