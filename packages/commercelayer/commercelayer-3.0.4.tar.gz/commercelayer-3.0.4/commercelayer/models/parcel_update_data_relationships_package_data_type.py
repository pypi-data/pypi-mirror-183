from enum import Enum


class ParcelUpdateDataRelationshipsPackageDataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
