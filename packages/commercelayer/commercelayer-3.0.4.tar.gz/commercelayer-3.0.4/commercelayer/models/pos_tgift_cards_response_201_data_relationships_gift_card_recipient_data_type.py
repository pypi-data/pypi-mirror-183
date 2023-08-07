from enum import Enum


class POSTgiftCardsResponse201DataRelationshipsGiftCardRecipientDataType(str, Enum):
    GIFT_CARD_RECIPIENT = "gift_card_recipient"

    def __str__(self) -> str:
        return str(self.value)
