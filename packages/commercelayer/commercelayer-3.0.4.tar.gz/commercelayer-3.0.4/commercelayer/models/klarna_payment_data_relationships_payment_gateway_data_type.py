from enum import Enum


class KlarnaPaymentDataRelationshipsPaymentGatewayDataType(str, Enum):
    PAYMENT_GATEWAYS = "payment_gateways"

    def __str__(self) -> str:
        return str(self.value)
