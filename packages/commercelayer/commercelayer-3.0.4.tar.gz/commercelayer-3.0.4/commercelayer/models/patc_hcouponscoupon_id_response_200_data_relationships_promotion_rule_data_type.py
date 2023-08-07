from enum import Enum


class PATCHcouponscouponIdResponse200DataRelationshipsPromotionRuleDataType(str, Enum):
    PROMOTION_RULE = "promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
