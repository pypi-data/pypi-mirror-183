from enum import Enum


class GETbraintreeGatewaysResponse200DataItemType(str, Enum):
    BRAINTREE_GATEWAYS = "braintree_gateways"

    def __str__(self) -> str:
        return str(self.value)
