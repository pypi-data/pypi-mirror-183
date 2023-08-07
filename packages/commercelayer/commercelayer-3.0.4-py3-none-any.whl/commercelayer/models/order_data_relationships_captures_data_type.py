from enum import Enum


class OrderDataRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
