from enum import Enum


class GETklarnaPaymentsklarnaPaymentIdResponse200DataType(str, Enum):
    KLARNA_PAYMENTS = "klarna_payments"

    def __str__(self) -> str:
        return str(self.value)
