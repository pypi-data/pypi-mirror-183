from enum import Enum


class GETordersorderIdResponse200DataRelationshipsPaymentSourceDataType(str, Enum):
    PAYMENT_SOURCE = "payment_source"

    def __str__(self) -> str:
        return str(self.value)
