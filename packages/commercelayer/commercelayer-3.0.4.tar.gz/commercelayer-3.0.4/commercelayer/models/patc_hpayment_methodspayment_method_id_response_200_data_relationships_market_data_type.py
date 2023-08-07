from enum import Enum


class PATCHpaymentMethodspaymentMethodIdResponse200DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
