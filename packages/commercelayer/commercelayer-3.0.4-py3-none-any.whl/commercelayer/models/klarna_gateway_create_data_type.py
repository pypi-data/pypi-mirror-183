from enum import Enum


class KlarnaGatewayCreateDataType(str, Enum):
    KLARNA_GATEWAYS = "klarna_gateways"

    def __str__(self) -> str:
        return str(self.value)
