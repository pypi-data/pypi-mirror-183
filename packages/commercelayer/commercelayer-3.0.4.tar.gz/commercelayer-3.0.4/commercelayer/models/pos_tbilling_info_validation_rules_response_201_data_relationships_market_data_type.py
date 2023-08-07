from enum import Enum


class POSTbillingInfoValidationRulesResponse201DataRelationshipsMarketDataType(str, Enum):
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
