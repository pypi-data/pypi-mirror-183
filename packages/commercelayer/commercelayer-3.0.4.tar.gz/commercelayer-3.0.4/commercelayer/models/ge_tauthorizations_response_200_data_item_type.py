from enum import Enum


class GETauthorizationsResponse200DataItemType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
