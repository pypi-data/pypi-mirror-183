from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ge_tgift_cards_response_200_data_item_relationships_attachments import (
        GETgiftCardsResponse200DataItemRelationshipsAttachments,
    )
    from ..models.ge_tgift_cards_response_200_data_item_relationships_events import (
        GETgiftCardsResponse200DataItemRelationshipsEvents,
    )
    from ..models.ge_tgift_cards_response_200_data_item_relationships_gift_card_recipient import (
        GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient,
    )
    from ..models.ge_tgift_cards_response_200_data_item_relationships_market import (
        GETgiftCardsResponse200DataItemRelationshipsMarket,
    )


T = TypeVar("T", bound="GETgiftCardsResponse200DataItemRelationships")


@attr.s(auto_attribs=True)
class GETgiftCardsResponse200DataItemRelationships:
    """
    Attributes:
        market (Union[Unset, GETgiftCardsResponse200DataItemRelationshipsMarket]):
        gift_card_recipient (Union[Unset, GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient]):
        attachments (Union[Unset, GETgiftCardsResponse200DataItemRelationshipsAttachments]):
        events (Union[Unset, GETgiftCardsResponse200DataItemRelationshipsEvents]):
    """

    market: Union[Unset, "GETgiftCardsResponse200DataItemRelationshipsMarket"] = UNSET
    gift_card_recipient: Union[Unset, "GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient"] = UNSET
    attachments: Union[Unset, "GETgiftCardsResponse200DataItemRelationshipsAttachments"] = UNSET
    events: Union[Unset, "GETgiftCardsResponse200DataItemRelationshipsEvents"] = UNSET
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
        from ..models.ge_tgift_cards_response_200_data_item_relationships_attachments import (
            GETgiftCardsResponse200DataItemRelationshipsAttachments,
        )
        from ..models.ge_tgift_cards_response_200_data_item_relationships_events import (
            GETgiftCardsResponse200DataItemRelationshipsEvents,
        )
        from ..models.ge_tgift_cards_response_200_data_item_relationships_gift_card_recipient import (
            GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient,
        )
        from ..models.ge_tgift_cards_response_200_data_item_relationships_market import (
            GETgiftCardsResponse200DataItemRelationshipsMarket,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, GETgiftCardsResponse200DataItemRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = GETgiftCardsResponse200DataItemRelationshipsMarket.from_dict(_market)

        _gift_card_recipient = d.pop("gift_card_recipient", UNSET)
        gift_card_recipient: Union[Unset, GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient]
        if isinstance(_gift_card_recipient, Unset):
            gift_card_recipient = UNSET
        else:
            gift_card_recipient = GETgiftCardsResponse200DataItemRelationshipsGiftCardRecipient.from_dict(
                _gift_card_recipient
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, GETgiftCardsResponse200DataItemRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = GETgiftCardsResponse200DataItemRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, GETgiftCardsResponse200DataItemRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = GETgiftCardsResponse200DataItemRelationshipsEvents.from_dict(_events)

        ge_tgift_cards_response_200_data_item_relationships = cls(
            market=market,
            gift_card_recipient=gift_card_recipient,
            attachments=attachments,
            events=events,
        )

        ge_tgift_cards_response_200_data_item_relationships.additional_properties = d
        return ge_tgift_cards_response_200_data_item_relationships

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
