from enum import Enum


class AuthorizationUpdateDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
