from enum import Enum


class POSTpaypalGatewaysResponse201DataType(str, Enum):
    PAYPAL_GATEWAYS = "paypal_gateways"

    def __str__(self) -> str:
        return str(self.value)
