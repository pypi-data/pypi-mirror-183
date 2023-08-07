from enum import Enum


class PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200DataType(str, Enum):
    CHECKOUT_COM_GATEWAYS = "checkout_com_gateways"

    def __str__(self) -> str:
        return str(self.value)
