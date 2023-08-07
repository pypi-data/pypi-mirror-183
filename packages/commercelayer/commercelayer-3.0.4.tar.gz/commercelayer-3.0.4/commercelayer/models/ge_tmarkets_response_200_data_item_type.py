from enum import Enum


class GETmarketsResponse200DataItemType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
