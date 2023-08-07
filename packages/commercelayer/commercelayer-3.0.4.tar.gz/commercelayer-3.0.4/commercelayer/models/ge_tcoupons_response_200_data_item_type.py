from enum import Enum


class GETcouponsResponse200DataItemType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
