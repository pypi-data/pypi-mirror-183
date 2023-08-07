from enum import Enum


class PATCHstockTransfersstockTransferIdResponse200DataRelationshipsLineItemDataType(str, Enum):
    LINE_ITEM = "line_item"

    def __str__(self) -> str:
        return str(self.value)
