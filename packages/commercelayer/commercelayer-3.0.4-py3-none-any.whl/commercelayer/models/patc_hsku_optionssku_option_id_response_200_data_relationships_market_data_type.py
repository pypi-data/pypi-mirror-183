from enum import Enum


class PATCHskuOptionsskuOptionIdResponse200DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
