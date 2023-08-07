from enum import Enum


class GETpaypalGatewaysResponse200DataItemType(str, Enum):
    PAYPAL_GATEWAYS = "paypal_gateways"

    def __str__(self) -> str:
        return str(self.value)
