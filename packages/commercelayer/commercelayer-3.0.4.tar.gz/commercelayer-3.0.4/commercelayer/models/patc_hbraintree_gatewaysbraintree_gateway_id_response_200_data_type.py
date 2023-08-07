from enum import Enum


class PATCHbraintreeGatewaysbraintreeGatewayIdResponse200DataType(str, Enum):
    BRAINTREE_GATEWAYS = "braintree_gateways"

    def __str__(self) -> str:
        return str(self.value)
