from enum import Enum


class POSTfreeShippingPromotionsResponse201DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
