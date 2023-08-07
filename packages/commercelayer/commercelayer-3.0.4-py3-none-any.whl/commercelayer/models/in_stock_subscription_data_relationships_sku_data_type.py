from enum import Enum


class InStockSubscriptionDataRelationshipsSkuDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
