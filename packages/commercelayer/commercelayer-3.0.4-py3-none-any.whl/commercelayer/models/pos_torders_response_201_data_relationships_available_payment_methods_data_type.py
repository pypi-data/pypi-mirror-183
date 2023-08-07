from enum import Enum


class POSTordersResponse201DataRelationshipsAvailablePaymentMethodsDataType(str, Enum):
    AVAILABLE_PAYMENT_METHODS = "available_payment_methods"

    def __str__(self) -> str:
        return str(self.value)
