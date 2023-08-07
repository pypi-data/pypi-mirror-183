from enum import Enum


class GETfreeShippingPromotionsResponse200DataItemRelationshipsPromotionRulesDataType(str, Enum):
    PROMOTION_RULES = "promotion_rules"

    def __str__(self) -> str:
        return str(self.value)
