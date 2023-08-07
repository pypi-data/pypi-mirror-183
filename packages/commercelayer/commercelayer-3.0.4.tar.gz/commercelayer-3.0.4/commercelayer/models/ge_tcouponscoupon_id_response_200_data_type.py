from enum import Enum


class GETcouponscouponIdResponse200DataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
