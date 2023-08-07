from enum import Enum


class POSTbundlesResponse201DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
