from enum import Enum


class StripeGatewayDataRelationshipsStripePaymentsDataType(str, Enum):
    STRIPE_PAYMENTS = "stripe_payments"

    def __str__(self) -> str:
        return str(self.value)
