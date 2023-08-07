from enum import Enum


class PATCHshipmentsshipmentIdResponse200DataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
