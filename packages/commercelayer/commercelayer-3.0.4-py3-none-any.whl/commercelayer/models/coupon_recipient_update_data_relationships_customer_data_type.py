from enum import Enum


class CouponRecipientUpdateDataRelationshipsCustomerDataType(str, Enum):
    CUSTOMERS = "customers"

    def __str__(self) -> str:
        return str(self.value)
