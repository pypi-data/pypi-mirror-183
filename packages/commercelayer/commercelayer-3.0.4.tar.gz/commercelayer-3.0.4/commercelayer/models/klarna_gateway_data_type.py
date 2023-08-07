from enum import Enum


class KlarnaGatewayDataType(str, Enum):
    KLARNA_GATEWAYS = "klarna_gateways"

    def __str__(self) -> str:
        return str(self.value)
