from enum import Enum


class InStockSubscriptionUpdateDataType(str, Enum):
    IN_STOCK_SUBSCRIPTIONS = "in_stock_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
