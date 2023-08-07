from enum import Enum


class GETpaypalPaymentspaypalPaymentIdResponse200DataRelationshipsOrderDataType(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
