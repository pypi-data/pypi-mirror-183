from enum import Enum


class StockItemCreateDataRelationshipsSkuDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
