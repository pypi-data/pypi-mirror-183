from enum import Enum


class GETpaymentGatewaysResponse200DataItemType(str, Enum):
    PAYMENT_GATEWAYS = "payment_gateways"

    def __str__(self) -> str:
        return str(self.value)
