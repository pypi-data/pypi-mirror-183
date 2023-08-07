from enum import Enum


class POSTcouponsResponse201DataRelationshipsPromotionRuleDataType(str, Enum):
    PROMOTION_RULE = "promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
