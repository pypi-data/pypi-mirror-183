from enum import Enum


class GiftCardCreateDataRelationshipsGiftCardRecipientDataType(str, Enum):
    GIFT_CARD_RECIPIENTS = "gift_card_recipients"

    def __str__(self) -> str:
        return str(self.value)
