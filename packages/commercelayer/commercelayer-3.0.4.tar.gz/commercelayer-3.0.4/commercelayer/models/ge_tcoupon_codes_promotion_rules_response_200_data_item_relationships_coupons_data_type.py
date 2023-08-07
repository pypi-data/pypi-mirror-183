from enum import Enum


class GETcouponCodesPromotionRulesResponse200DataItemRelationshipsCouponsDataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
