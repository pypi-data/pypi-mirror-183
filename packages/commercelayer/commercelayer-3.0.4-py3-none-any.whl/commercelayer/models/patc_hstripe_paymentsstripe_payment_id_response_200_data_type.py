from enum import Enum


class PATCHstripePaymentsstripePaymentIdResponse200DataType(str, Enum):
    STRIPE_PAYMENTS = "stripe_payments"

    def __str__(self) -> str:
        return str(self.value)
