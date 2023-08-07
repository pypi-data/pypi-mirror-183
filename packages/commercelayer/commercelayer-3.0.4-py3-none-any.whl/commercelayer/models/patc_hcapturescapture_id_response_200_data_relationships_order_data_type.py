from enum import Enum


class PATCHcapturescaptureIdResponse200DataRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
