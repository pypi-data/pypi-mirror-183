from enum import Enum


class GETparcelsResponse200DataItemRelationshipsPackageDataType(str, Enum):
    PACKAGE = "package"

    def __str__(self) -> str:
        return str(self.value)
