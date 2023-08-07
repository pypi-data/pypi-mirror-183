from enum import Enum


class GETstripePaymentsResponse200DataItemType(str, Enum):
    STRIPE_PAYMENTS = "stripe_payments"

    def __str__(self) -> str:
        return str(self.value)
