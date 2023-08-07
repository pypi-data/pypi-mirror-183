from enum import Enum


class POSTexternalGatewaysResponse201DataRelationshipsExternalPaymentsDataType(str, Enum):
    EXTERNAL_PAYMENTS = "external_payments"

    def __str__(self) -> str:
        return str(self.value)
