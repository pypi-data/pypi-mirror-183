from enum import Enum


class KlarnaGatewayUpdateDataType(str, Enum):
    KLARNA_GATEWAYS = "klarna_gateways"

    def __str__(self) -> str:
        return str(self.value)
