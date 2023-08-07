from enum import Enum


class GETordersResponse200DataItemRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
