from enum import Enum


class GETcouponRecipientsResponse200DataItemRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
