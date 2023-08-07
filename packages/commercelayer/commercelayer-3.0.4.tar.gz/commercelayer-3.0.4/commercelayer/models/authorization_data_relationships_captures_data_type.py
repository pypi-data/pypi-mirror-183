from enum import Enum


class AuthorizationDataRelationshipsCapturesDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
