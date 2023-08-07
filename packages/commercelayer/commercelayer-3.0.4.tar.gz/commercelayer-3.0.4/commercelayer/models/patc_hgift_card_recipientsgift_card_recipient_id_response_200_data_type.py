from enum import Enum


class PATCHgiftCardRecipientsgiftCardRecipientIdResponse200DataType(str, Enum):
    GIFT_CARD_RECIPIENTS = "gift_card_recipients"

    def __str__(self) -> str:
        return str(self.value)
