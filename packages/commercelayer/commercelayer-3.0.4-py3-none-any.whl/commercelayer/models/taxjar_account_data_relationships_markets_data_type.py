from enum import Enum


class TaxjarAccountDataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
