from enum import Enum


class GETorganizationorganizationIdResponse200DataType(str, Enum):
    ORGANIZATION = "organization"

    def __str__(self) -> str:
        return str(self.value)
