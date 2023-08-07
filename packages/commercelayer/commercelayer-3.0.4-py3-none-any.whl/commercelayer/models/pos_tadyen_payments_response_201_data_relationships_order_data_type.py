from enum import Enum


class POSTadyenPaymentsResponse201DataRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
