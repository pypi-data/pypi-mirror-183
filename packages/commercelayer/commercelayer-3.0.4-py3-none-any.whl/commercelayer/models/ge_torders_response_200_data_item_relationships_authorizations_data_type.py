from enum import Enum


class GETordersResponse200DataItemRelationshipsAuthorizationsDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
