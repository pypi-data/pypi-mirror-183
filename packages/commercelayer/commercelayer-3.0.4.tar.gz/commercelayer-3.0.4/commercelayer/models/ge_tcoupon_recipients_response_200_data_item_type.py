from enum import Enum


class GETcouponRecipientsResponse200DataItemType(str, Enum):
    COUPON_RECIPIENTS = "coupon_recipients"

    def __str__(self) -> str:
        return str(self.value)
