from enum import Enum


class PATCHorderAmountPromotionRulesorderAmountPromotionRuleIdResponse200DataRelationshipsPromotionDataType(str, Enum):
    PROMOTION = "promotion"

    def __str__(self) -> str:
        return str(self.value)
