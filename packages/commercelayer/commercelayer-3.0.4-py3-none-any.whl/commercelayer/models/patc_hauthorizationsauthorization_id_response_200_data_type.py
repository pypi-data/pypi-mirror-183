from enum import Enum


class PATCHauthorizationsauthorizationIdResponse200DataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
