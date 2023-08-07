from enum import Enum


class GETordersResponse200DataItemRelationshipsPaymentMethodDataType(str, Enum):
    PAYMENT_METHOD = "payment_method"

    def __str__(self) -> str:
        return str(self.value)
