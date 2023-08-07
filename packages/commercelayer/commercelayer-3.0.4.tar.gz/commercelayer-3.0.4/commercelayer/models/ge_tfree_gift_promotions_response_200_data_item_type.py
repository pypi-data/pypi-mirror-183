from enum import Enum


class GETfreeGiftPromotionsResponse200DataItemType(str, Enum):
    FREE_GIFT_PROMOTIONS = "free_gift_promotions"

    def __str__(self) -> str:
        return str(self.value)
