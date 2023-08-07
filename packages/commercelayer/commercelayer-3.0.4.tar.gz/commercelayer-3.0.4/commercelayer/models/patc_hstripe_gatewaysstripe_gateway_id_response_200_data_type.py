from enum import Enum


class PATCHstripeGatewaysstripeGatewayIdResponse200DataType(str, Enum):
    STRIPE_GATEWAYS = "stripe_gateways"

    def __str__(self) -> str:
        return str(self.value)
