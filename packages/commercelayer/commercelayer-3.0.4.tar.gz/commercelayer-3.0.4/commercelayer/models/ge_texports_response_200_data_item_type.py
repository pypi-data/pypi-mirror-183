from enum import Enum


class GETexportsResponse200DataItemType(str, Enum):
    EXPORTS = "exports"

    def __str__(self) -> str:
        return str(self.value)
