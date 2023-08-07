from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_attachments import (
        PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments,
    )
    from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_events import (
        PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents,
    )
    from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_gift_card_recipient import (
        PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient,
    )
    from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_market import (
        PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket,
    )


T = TypeVar("T", bound="PATCHgiftCardsgiftCardIdResponse200DataRelationships")


@attr.s(auto_attribs=True)
class PATCHgiftCardsgiftCardIdResponse200DataRelationships:
    """
    Attributes:
        market (Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket]):
        gift_card_recipient (Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient]):
        attachments (Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments]):
        events (Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents]):
    """

    market: Union[Unset, "PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket"] = UNSET
    gift_card_recipient: Union[Unset, "PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient"] = UNSET
    attachments: Union[Unset, "PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments"] = UNSET
    events: Union[Unset, "PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents"] = UNSET
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
        from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_attachments import (
            PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments,
        )
        from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_events import (
            PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents,
        )
        from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_gift_card_recipient import (
            PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient,
        )
        from ..models.patc_hgift_cardsgift_card_id_response_200_data_relationships_market import (
            PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket,
        )

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = PATCHgiftCardsgiftCardIdResponse200DataRelationshipsMarket.from_dict(_market)

        _gift_card_recipient = d.pop("gift_card_recipient", UNSET)
        gift_card_recipient: Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient]
        if isinstance(_gift_card_recipient, Unset):
            gift_card_recipient = UNSET
        else:
            gift_card_recipient = PATCHgiftCardsgiftCardIdResponse200DataRelationshipsGiftCardRecipient.from_dict(
                _gift_card_recipient
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments]
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = PATCHgiftCardsgiftCardIdResponse200DataRelationshipsAttachments.from_dict(_attachments)

        _events = d.pop("events", UNSET)
        events: Union[Unset, PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PATCHgiftCardsgiftCardIdResponse200DataRelationshipsEvents.from_dict(_events)

        patc_hgift_cardsgift_card_id_response_200_data_relationships = cls(
            market=market,
            gift_card_recipient=gift_card_recipient,
            attachments=attachments,
            events=events,
        )

        patc_hgift_cardsgift_card_id_response_200_data_relationships.additional_properties = d
        return patc_hgift_cardsgift_card_id_response_200_data_relationships

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
