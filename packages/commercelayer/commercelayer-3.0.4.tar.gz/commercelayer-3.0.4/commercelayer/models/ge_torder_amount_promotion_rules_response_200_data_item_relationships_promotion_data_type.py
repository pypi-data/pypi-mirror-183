from enum import Enum


class GETorderAmountPromotionRulesResponse200DataItemRelationshipsPromotionDataType(str, Enum):
    PROMOTION = "promotion"

    def __str__(self) -> str:
        return str(self.value)
