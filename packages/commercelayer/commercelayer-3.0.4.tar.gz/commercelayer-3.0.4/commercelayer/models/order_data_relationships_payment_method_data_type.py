from enum import Enum


class OrderDataRelationshipsPaymentMethodDataType(str, Enum):
    PAYMENT_METHODS = "payment_methods"

    def __str__(self) -> str:
        return str(self.value)
