from enum import Enum


class GETadyenGatewaysResponse200DataItemType(str, Enum):
    ADYEN_GATEWAYS = "adyen_gateways"

    def __str__(self) -> str:
        return str(self.value)
