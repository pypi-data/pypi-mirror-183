from enum import Enum


class ManualGatewayUpdateDataType(str, Enum):
    MANUAL_GATEWAYS = "manual_gateways"

    def __str__(self) -> str:
        return str(self.value)
