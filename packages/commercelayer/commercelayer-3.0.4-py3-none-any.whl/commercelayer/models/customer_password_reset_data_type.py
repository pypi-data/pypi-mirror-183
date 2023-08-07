from enum import Enum


class CustomerPasswordResetDataType(str, Enum):
    CUSTOMER_PASSWORD_RESETS = "customer_password_resets"

    def __str__(self) -> str:
        return str(self.value)
