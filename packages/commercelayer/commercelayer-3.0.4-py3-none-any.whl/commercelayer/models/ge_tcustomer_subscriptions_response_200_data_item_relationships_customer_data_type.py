from enum import Enum


class GETcustomerSubscriptionsResponse200DataItemRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
