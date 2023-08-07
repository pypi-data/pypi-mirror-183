from enum import Enum


class ReturnLineItemDataType(str, Enum):
    RETURN_LINE_ITEMS = "return_line_items"

    def __str__(self) -> str:
        return str(self.value)
