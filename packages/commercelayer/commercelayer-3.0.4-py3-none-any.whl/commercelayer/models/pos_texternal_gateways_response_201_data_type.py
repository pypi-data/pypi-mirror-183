from enum import Enum


class POSTexternalGatewaysResponse201DataType(str, Enum):
    EXTERNAL_GATEWAYS = "external_gateways"

    def __str__(self) -> str:
        return str(self.value)
