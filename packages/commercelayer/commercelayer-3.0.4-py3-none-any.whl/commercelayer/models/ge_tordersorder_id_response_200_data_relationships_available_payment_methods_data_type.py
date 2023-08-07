from enum import Enum


class GETordersorderIdResponse200DataRelationshipsAvailablePaymentMethodsDataType(str, Enum):
    AVAILABLE_PAYMENT_METHODS = "available_payment_methods"

    def __str__(self) -> str:
        return str(self.value)
