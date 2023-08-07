from enum import Enum


class GETtaxCalculatorsResponse200DataItemRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
