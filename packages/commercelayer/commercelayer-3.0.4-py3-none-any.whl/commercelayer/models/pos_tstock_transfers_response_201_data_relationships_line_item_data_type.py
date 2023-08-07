from enum import Enum


class POSTstockTransfersResponse201DataRelationshipsLineItemDataType(str, Enum):
    LINE_ITEM = "line_item"

    def __str__(self) -> str:
        return str(self.value)
