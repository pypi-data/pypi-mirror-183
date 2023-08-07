from enum import Enum


class POSTparcelsResponse201DataRelationshipsPackageDataType(str, Enum):
    PACKAGE = "package"

    def __str__(self) -> str:
        return str(self.value)
