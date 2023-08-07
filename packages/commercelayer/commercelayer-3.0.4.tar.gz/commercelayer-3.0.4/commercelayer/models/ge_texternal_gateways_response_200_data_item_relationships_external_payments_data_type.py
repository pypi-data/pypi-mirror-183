from enum import Enum


class GETexternalGatewaysResponse200DataItemRelationshipsExternalPaymentsDataType(str, Enum):
    EXTERNAL_PAYMENTS = "external_payments"

    def __str__(self) -> str:
        return str(self.value)
