from enum import Enum


class POSTorderAmountPromotionRulesResponse201DataRelationshipsPromotionDataType(str, Enum):
    PROMOTION = "promotion"

    def __str__(self) -> str:
        return str(self.value)
