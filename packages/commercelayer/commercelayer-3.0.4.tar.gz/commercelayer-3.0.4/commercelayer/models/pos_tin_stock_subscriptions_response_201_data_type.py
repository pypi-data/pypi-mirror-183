from enum import Enum


class POSTinStockSubscriptionsResponse201DataType(str, Enum):
    IN_STOCK_SUBSCRIPTIONS = "in_stock_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
