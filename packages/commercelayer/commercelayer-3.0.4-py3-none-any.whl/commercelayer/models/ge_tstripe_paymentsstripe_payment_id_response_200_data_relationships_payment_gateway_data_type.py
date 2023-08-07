from enum import Enum


class GETstripePaymentsstripePaymentIdResponse200DataRelationshipsPaymentGatewayDataType(str, Enum):
    PAYMENT_GATEWAY = "payment_gateway"

    def __str__(self) -> str:
        return str(self.value)
