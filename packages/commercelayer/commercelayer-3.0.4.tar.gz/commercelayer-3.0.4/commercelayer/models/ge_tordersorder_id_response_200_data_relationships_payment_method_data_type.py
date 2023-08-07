from enum import Enum


class GETordersorderIdResponse200DataRelationshipsPaymentMethodDataType(str, Enum):
    PAYMENT_METHOD = "payment_method"

    def __str__(self) -> str:
        return str(self.value)
