from enum import Enum


class GETgiftCardsgiftCardIdResponse200DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
