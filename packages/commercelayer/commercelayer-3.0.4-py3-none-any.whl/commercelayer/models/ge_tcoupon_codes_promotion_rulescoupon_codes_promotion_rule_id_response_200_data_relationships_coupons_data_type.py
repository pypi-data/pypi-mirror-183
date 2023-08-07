from enum import Enum


class GETcouponCodesPromotionRulescouponCodesPromotionRuleIdResponse200DataRelationshipsCouponsDataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
