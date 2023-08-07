from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsPaymentSourceDataType(str, Enum):
    PAYMENT_SOURCE = "payment_source"

    def __str__(self) -> str:
        return str(self.value)
