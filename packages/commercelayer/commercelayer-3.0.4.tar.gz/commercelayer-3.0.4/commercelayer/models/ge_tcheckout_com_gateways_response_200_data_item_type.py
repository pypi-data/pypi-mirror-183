from enum import Enum


class GETcheckoutComGatewaysResponse200DataItemType(str, Enum):
    CHECKOUT_COM_GATEWAYS = "checkout_com_gateways"

    def __str__(self) -> str:
        return str(self.value)
