from enum import Enum


class PercentageDiscountPromotionDataRelationshipsMarketDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
