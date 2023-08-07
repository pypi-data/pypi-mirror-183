from enum import Enum


class GETmarketsmarketIdResponse200DataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
