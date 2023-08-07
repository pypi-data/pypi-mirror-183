from enum import Enum


class POSTordersResponse201DataRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
