from enum import Enum


class GETcheckoutComPaymentsResponse200DataItemRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
