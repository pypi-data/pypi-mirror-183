from enum import Enum


class POSTordersResponse201DataRelationshipsAuthorizationsDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
