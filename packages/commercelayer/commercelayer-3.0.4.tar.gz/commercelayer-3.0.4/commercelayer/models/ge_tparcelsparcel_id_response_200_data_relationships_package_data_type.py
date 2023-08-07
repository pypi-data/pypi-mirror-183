from enum import Enum


class GETparcelsparcelIdResponse200DataRelationshipsPackageDataType(str, Enum):
    PACKAGE = "package"

    def __str__(self) -> str:
        return str(self.value)
