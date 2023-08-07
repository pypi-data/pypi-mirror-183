from enum import Enum


class GETexternalTaxCalculatorsResponse200DataItemRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
