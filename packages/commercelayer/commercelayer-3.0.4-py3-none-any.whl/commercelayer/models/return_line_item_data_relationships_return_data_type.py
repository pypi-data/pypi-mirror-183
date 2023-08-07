from enum import Enum


class ReturnLineItemDataRelationshipsReturnDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
