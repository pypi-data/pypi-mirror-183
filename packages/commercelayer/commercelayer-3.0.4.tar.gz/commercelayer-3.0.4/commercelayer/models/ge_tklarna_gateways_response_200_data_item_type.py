from enum import Enum


class GETklarnaGatewaysResponse200DataItemType(str, Enum):
    KLARNA_GATEWAYS = "klarna_gateways"

    def __str__(self) -> str:
        return str(self.value)
