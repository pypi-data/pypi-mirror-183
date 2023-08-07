from enum import Enum


class ParcelCreateDataRelationshipsPackageDataType(str, Enum):
    PACKAGES = "packages"

    def __str__(self) -> str:
        return str(self.value)
