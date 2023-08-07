from enum import Enum


class POSTexternalPaymentsResponse201DataType(str, Enum):
    EXTERNAL_PAYMENTS = "external_payments"

    def __str__(self) -> str:
        return str(self.value)
