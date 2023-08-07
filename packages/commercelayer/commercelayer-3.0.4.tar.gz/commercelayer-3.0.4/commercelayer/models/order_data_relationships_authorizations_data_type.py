from enum import Enum


class OrderDataRelationshipsAuthorizationsDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
