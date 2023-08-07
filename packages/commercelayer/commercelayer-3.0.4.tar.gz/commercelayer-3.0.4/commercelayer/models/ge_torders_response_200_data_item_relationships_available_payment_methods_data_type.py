from enum import Enum


class GETordersResponse200DataItemRelationshipsAvailablePaymentMethodsDataType(str, Enum):
    AVAILABLE_PAYMENT_METHODS = "available_payment_methods"

    def __str__(self) -> str:
        return str(self.value)
