from enum import Enum


class PATCHgiftCardsgiftCardIdResponse200DataType(str, Enum):
    GIFT_CARDS = "gift_cards"

    def __str__(self) -> str:
        return str(self.value)
