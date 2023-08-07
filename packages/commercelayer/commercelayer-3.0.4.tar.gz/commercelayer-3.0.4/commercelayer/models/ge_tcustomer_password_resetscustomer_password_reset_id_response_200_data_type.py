from enum import Enum


class GETcustomerPasswordResetscustomerPasswordResetIdResponse200DataType(str, Enum):
    CUSTOMER_PASSWORD_RESETS = "customer_password_resets"

    def __str__(self) -> str:
        return str(self.value)
