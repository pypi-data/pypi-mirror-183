from enum import Enum


class GETcarrierAccountsResponse200DataItemRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
