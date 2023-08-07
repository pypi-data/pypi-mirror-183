from enum import Enum


class InStockSubscriptionDataRelationshipsMarketDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
