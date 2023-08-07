from enum import Enum


class CheckoutComGatewayCreateDataType(str, Enum):
    CHECKOUT_COM_GATEWAYS = "checkout_com_gateways"

    def __str__(self) -> str:
        return str(self.value)
