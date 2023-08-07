from enum import Enum


class POSTcouponsResponse201DataType(str, Enum):
    COUPONS = "coupons"

    def __str__(self) -> str:
        return str(self.value)
