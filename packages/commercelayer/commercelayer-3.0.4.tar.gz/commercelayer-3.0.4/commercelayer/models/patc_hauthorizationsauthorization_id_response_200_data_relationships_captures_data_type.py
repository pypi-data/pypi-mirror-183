from enum import Enum


class PATCHauthorizationsauthorizationIdResponse200DataRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
