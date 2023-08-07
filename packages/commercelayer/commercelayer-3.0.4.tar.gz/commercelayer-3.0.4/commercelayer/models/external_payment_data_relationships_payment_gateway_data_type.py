from enum import Enum


class ExternalPaymentDataRelationshipsPaymentGatewayDataType(str, Enum):
    PAYMENT_GATEWAYS = "payment_gateways"

    def __str__(self) -> str:
        return str(self.value)
