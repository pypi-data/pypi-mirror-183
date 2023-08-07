from enum import Enum


class LineItemOptionDataType(str, Enum):
    LINE_ITEM_OPTIONS = "line_item_options"

    def __str__(self) -> str:
        return str(self.value)
