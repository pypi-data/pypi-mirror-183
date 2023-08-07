from enum import Enum


class POSTinStockSubscriptionsResponse201DataRelationshipsSkuDataType(str, Enum):
    SKU = "sku"

    def __str__(self) -> str:
        return str(self.value)
