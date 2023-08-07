from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_card_create_data_relationships_gift_card_recipient import (
        GiftCardCreateDataRelationshipsGiftCardRecipient,
    )
    from ..models.gift_card_create_data_relationships_market import GiftCardCreateDataRelationshipsMarket


T = TypeVar("T", bound="GiftCardCreateDataRelationships")


@attr.s(auto_attribs=True)
class GiftCardCreateDataRelationships:
    """
    Attributes:
        market (Union[Unset, GiftCardCreateDataRelationshipsMarket]):
        gift_card_recipient (Union[Unset, GiftCardCreateDataRelationshipsGiftCardRecipient]):
    """

    market: Union[Unset, "GiftCardCreateDataRelationshipsMarket"] = UNSET
    gift_card_recipient: Union[Unset, "GiftCardCreateDataRelationshipsGiftCardRecipient"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        gift_card_recipient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_card_recipient, Unset):
            gift_card_recipient = self.gift_card_recipient.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if gift_card_recipient is not UNSET:
            field_dict["gift_card_recipient"] = gift_card_recipient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_card_create_data_relationships_gift_card_recipient import (
            GiftCardCreateDataRelationshipsGiftCardRecipient,
        )
        from ..models.gift_card_create_data_relationships_market import GiftCardCreateDataRelationshipsMarket

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GiftCardCreateDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GiftCardCreateDataRelationshipsMarket.from_dict(_market)

        _gift_card_recipient = d.pop("gift_card_recipient", UNSET)
        gift_card_recipient: Union[Unset, GiftCardCreateDataRelationshipsGiftCardRecipient]
        if isinstance(_gift_card_recipient, Unset):
            gift_card_recipient = UNSET
        else:
            gift_card_recipient = GiftCardCreateDataRelationshipsGiftCardRecipient.from_dict(_gift_card_recipient)

        gift_card_create_data_relationships = cls(
            market=market,
            gift_card_recipient=gift_card_recipient,
        )

        gift_card_create_data_relationships.additional_properties = d
        return gift_card_create_data_relationships

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
