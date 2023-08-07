from enum import Enum


class CouponRecipientCreateDataType(str, Enum):
    COUPON_RECIPIENTS = "coupon_recipients"

    def __str__(self) -> str:
        return str(self.value)
