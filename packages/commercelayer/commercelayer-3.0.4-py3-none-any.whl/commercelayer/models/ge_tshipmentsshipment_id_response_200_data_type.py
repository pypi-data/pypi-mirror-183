from enum import Enum


class GETshipmentsshipmentIdResponse200DataType(str, Enum):
    SHIPMENTS = "shipments"

    def __str__(self) -> str:
        return str(self.value)
