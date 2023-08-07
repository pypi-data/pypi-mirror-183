from enum import Enum


class GETordersorderIdResponse200DataRelationshipsAuthorizationsDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
