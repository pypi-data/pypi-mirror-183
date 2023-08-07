from enum import Enum


class POSTmanualTaxCalculatorsResponse201DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
