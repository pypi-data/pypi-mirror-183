from enum import Enum


class GETcarrierAccountscarrierAccountIdResponse200DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
