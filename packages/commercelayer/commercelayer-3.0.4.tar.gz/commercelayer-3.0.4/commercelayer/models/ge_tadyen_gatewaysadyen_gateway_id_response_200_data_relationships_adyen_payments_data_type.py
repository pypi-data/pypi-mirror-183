from enum import Enum


class GETadyenGatewaysadyenGatewayIdResponse200DataRelationshipsAdyenPaymentsDataType(str, Enum):
    ADYEN_PAYMENTS = "adyen_payments"

    def __str__(self) -> str:
        return str(self.value)
