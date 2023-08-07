from enum import Enum


class StripeGatewayUpdateDataType(str, Enum):
    STRIPE_GATEWAYS = "stripe_gateways"

    def __str__(self) -> str:
        return str(self.value)
