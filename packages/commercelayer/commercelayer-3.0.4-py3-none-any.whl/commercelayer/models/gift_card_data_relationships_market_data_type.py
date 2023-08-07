from enum import Enum


class GiftCardDataRelationshipsMarketDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
