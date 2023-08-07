from enum import Enum


class POSTstripeGatewaysResponse201DataRelationshipsStripePaymentsDataType(str, Enum):
    STRIPE_PAYMENTS = "stripe_payments"

    def __str__(self) -> str:
        return str(self.value)
