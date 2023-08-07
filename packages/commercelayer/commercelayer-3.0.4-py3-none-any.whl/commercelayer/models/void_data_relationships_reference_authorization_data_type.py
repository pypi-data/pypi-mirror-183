from enum import Enum


class VoidDataRelationshipsReferenceAuthorizationDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
