from enum import Enum


class CustomerDataRelationshipsReturnsDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
