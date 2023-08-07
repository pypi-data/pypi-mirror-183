from enum import Enum


class GETpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsOrderAmountPromotionRuleDataType(
    str, Enum
):
    ORDER_AMOUNT_PROMOTION_RULE = "order_amount_promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
