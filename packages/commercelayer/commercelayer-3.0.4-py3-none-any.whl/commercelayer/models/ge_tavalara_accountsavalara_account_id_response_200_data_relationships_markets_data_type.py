from enum import Enum


class GETavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
