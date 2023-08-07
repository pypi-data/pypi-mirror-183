from enum import Enum


class AdyenGatewayDataType(str, Enum):
    ADYEN_GATEWAYS = "adyen_gateways"

    def __str__(self) -> str:
        return str(self.value)
