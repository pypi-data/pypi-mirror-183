from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_card_data_relationships_attachments import GiftCardDataRelationshipsAttachments
    from ..models.gift_card_data_relationships_events import GiftCardDataRelationshipsEvents
    from ..models.gift_card_data_relationships_gift_card_recipient import GiftCardDataRelationshipsGiftCardRecipient
    from ..models.gift_card_data_relationships_market import GiftCardDataRelationshipsMarket


T = TypeVar("T", bound="GiftCardDataRelationships")


@attr.s(auto_attribs=True)
class GiftCardDataRelationships:
    """
    Attributes:
        market (Union[Unset, GiftCardDataRelationshipsMarket]):
        gift_card_recipient (Union[Unset, GiftCardDataRelationshipsGiftCardRecipient]):
        attachments (Union[Unset, GiftCardDataRelationshipsAttachments]):
        events (Union[Unset, GiftCardDataRelationshipsEvents]):
    """

    market: Union[Unset, "GiftCardDataRelationshipsMarket"] = UNSET
    gift_card_recipient: Union[Unset, "GiftCardDataRelationshipsGiftCardRecipient"] = UNSET
    attachments: Union[Unset, "GiftCardDataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GiftCardDataRelationshipsEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        gift_card_recipient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_card_recipient, Unset):
            gift_card_recipient = self.gift_card_recipient.to_dict()

        attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if gift_card_recipient is not UNSET:
            field_dict["gift_card_recipient"] = gift_card_recipient
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_card_data_relationships_attachments import GiftCardDataRelationshipsAttachments
        from ..models.gift_card_data_relationships_events import GiftCardDataRelationshipsEvents
        from ..models.gift_card_data_relationships_gift_card_recipient import GiftCardDataRelationshipsGiftCardRecipient
        from ..models.gift_card_data_relationships_market import GiftCardDataRelationshipsMarket

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GiftCardDataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GiftCardDataRelationshipsMarket.from_dict(_market)

        _gift_card_recipient = d.pop("gift_card_recipient", UNSET)
        gift_card_recipient: Union[Unset, GiftCardDataRelationshipsGiftCardRecipient]
        if isinstance(_gift_card_recipient, Unset):
            gift_card_recipient = UNSET
        else:
            gift_card_recipient = GiftCardDataRelationshipsGiftCardRecipient.from_dict(_gift_card_recipient)

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GiftCardDataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GiftCardDataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GiftCardDataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GiftCardDataRelationshipsEvents.from_dict(_events)

        gift_card_data_relationships = cls(
            market=market,
            gift_card_recipient=gift_card_recipient,
            attachments=attachments,
            events=events,
        )

        gift_card_data_relationships.additional_properties = d
        return gift_card_data_relationships

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
