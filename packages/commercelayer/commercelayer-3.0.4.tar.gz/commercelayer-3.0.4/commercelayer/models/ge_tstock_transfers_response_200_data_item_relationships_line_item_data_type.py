from enum import Enum


class GETstockTransfersResponse200DataItemRelationshipsLineItemDataType(str, Enum):
    LINE_ITEM = "line_item"

    def __str__(self) -> str:
        return str(self.value)
