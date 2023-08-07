from enum import Enum


class POSTcouponCodesPromotionRulesResponse201DataRelationshipsCouponsDataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
