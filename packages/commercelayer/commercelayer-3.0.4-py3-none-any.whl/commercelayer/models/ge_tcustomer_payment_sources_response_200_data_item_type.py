from enum import Enum


class GETcustomerPaymentSourcesResponse200DataItemType(str, Enum):
    CUSTOMER_PAYMENT_SOURCES = "customer_payment_sources"

    def __str__(self) -> str:
        return str(self.value)
