from enum import Enum


class PATCHmarketsmarketIdResponse200DataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
