from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pos_tgift_cards_response_201_data_relationships_gift_card_recipient_data import (
        POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData,
    )
    from ..models.pos_tgift_cards_response_201_data_relationships_gift_card_recipient_links import (
        POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks,
    )


T = TypeVar("T", bound="POSTgiftCardsResponse201DataRelationshipsGiftCardRecipient")


@attr.s(auto_attribs=True)
class POSTgiftCardsResponse201DataRelationshipsGiftCardRecipient:
    """
    Attributes:
        links (Union[Unset, POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks]):
        data (Union[Unset, POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData]):
    """

    links: Union[Unset, "POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks"] = UNSET
    data: Union[Unset, "POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pos_tgift_cards_response_201_data_relationships_gift_card_recipient_data import (
            POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData,
        )
        from ..models.pos_tgift_cards_response_201_data_relationships_gift_card_recipient_links import (
            POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientLinks.from_dict(_links)

        _data = d.pop("data", UNSET)
        data: Union[Unset, POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientData.from_dict(_data)

        pos_tgift_cards_response_201_data_relationships_gift_card_recipient = cls(
            links=links,
            data=data,
        )

        pos_tgift_cards_response_201_data_relationships_gift_card_recipient.additional_properties = d
        return pos_tgift_cards_response_201_data_relationships_gift_card_recipient

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
