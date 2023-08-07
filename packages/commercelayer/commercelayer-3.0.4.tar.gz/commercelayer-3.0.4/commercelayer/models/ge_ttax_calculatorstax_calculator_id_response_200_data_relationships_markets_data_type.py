from enum import Enum


class GETtaxCalculatorstaxCalculatorIdResponse200DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
