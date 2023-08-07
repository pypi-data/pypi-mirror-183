from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsAuthorizationsDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
