from enum import Enum


class AdyenGatewayCreateDataRelationshipsAdyenPaymentsDataType(str, Enum):
    ADYEN_PAYMENTS = "adyen_payments"

    def __str__(self) -> str:
        return str(self.value)
