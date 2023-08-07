from enum import Enum


class POSTpaymentMethodsResponse201DataType(str, Enum):
    PAYMENT_METHODS = "payment_methods"

    def __str__(self) -> str:
        return str(self.value)
