from enum import Enum


class POSTcouponRecipientsResponse201DataType(str, Enum):
    COUPON_RECIPIENTS = "coupon_recipients"

    def __str__(self) -> str:
        return str(self.value)
