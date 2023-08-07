from enum import Enum


class PromotionDataRelationshipsMarketDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
