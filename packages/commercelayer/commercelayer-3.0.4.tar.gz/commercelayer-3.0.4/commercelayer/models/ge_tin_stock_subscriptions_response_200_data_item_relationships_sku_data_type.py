from enum import Enum


class GETinStockSubscriptionsResponse200DataItemRelationshipsSkuDataType(str, Enum):
    SKU = "sku"

    def __str__(self) -> str:
        return str(self.value)
