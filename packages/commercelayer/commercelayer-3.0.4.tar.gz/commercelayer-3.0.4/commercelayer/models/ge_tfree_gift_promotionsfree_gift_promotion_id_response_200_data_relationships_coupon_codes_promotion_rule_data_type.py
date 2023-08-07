from enum import Enum


class GETfreeGiftPromotionsfreeGiftPromotionIdResponse200DataRelationshipsCouponCodesPromotionRuleDataType(str, Enum):
    COUPON_CODES_PROMOTION_RULE = "coupon_codes_promotion_rule"

    def __str__(self) -> str:
        return str(self.value)
