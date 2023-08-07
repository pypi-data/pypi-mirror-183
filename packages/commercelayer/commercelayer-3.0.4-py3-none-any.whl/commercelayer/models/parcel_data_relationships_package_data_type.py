from enum import Enum


class ParcelDataRelationshipsPackageDataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
