from enum import Enum


class POSTmarketsResponse201DataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
