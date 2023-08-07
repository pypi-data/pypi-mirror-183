from enum import Enum


class PATCHavalaraAccountsavalaraAccountIdResponse200DataRelationshipsMarketsDataType(str, Enum):
    MARKETS = "markets"

    def __str__(self) -> str:
        return str(self.value)
