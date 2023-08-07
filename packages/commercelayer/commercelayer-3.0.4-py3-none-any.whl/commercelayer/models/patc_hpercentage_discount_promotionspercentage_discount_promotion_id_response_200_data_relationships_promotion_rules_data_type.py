from enum import Enum


class PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsPromotionRulesDataType(
    str, Enum
):
    PROMOTION_RULES = "promotion_rules"

    def __str__(self) -> str:
        return str(self.value)
