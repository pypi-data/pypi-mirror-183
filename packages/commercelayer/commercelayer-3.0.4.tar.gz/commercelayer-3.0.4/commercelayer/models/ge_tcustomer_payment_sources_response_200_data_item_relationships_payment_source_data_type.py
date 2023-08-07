from enum import Enum


class GETcustomerPaymentSourcesResponse200DataItemRelationshipsPaymentSourceDataType(str, Enum):
    PAYMENT_SOURCE = "payment_source"

    def __str__(self) -> str:
        return str(self.value)
