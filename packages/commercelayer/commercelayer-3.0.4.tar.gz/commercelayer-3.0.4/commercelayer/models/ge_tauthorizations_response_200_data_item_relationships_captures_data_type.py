from enum import Enum


class GETauthorizationsResponse200DataItemRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
