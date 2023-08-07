from enum import Enum


class GETcustomerGroupscustomerGroupIdResponse200DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
