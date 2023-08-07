from enum import Enum


class GETinStockSubscriptionsinStockSubscriptionIdResponse200DataRelationshipsSkuDataType(str, Enum):
    SKU = "sku"

    def __str__(self) -> str:
        return str(self.value)
