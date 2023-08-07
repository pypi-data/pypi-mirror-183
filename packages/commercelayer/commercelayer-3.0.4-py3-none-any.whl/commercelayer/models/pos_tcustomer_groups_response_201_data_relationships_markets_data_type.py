from enum import Enum


class POSTcustomerGroupsResponse201DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
