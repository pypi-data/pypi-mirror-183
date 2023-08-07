from enum import Enum


class OrderAmountPromotionRuleDataType(str, Enum):
    ORDER_AMOUNT_PROMOTION_RULES = "order_amount_promotion_rules"

    def __str__(self) -> str:
        return str(self.value)
