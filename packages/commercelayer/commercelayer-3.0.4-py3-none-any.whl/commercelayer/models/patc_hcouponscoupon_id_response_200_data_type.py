from enum import Enum


class PATCHcouponscouponIdResponse200DataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
