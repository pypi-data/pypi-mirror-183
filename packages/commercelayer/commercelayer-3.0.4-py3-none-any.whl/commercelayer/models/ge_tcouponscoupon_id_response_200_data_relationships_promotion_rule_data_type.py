from enum import Enum


class GETcouponscouponIdResponse200DataRelationshipsPromotionRuleDataType(str, Enum):
    PROMOTION_RULE = "promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
