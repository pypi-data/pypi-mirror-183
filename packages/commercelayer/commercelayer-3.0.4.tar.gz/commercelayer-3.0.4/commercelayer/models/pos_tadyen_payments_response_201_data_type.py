from enum import Enum


class POSTadyenPaymentsResponse201DataType(str, Enum):
    ADYEN_PAYMENTS = "adyen_payments"

    def __str__(self) -> str:
        return str(self.value)
