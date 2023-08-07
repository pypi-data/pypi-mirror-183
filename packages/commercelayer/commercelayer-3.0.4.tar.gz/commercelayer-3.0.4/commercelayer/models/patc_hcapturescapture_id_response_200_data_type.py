from enum import Enum


class PATCHcapturescaptureIdResponse200DataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
