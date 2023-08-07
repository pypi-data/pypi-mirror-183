from enum import Enum


class StockItemUpdateDataRelationshipsSkuDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
