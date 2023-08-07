from enum import Enum


class POSTmanualGatewaysResponse201DataType(str, Enum):
    MANUAL_GATEWAYS = "manual_gateways"

    def __str__(self) -> str:
        return str(self.value)
